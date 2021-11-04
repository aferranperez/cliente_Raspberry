import cv2
import numpy as np
import os
from PIL import Image
import time

#Clasificar Rostros 
def clasificar_rostro():

    #Cargar modelo de reconocimiento facial
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.read("models/2021-10-6-21-57-49.xml")

    #Crear instancia de captura de video
    cv2.namedWindow("Deteccion facial")
    cap = cv2.VideoCapture(0)

    if cap.isOpened():
        rval, frame = cap.read()
    else:
        rval = False

    while rval:
        caras, gray = detectar_caras(frame)

        if caras is not None:
            for cara in caras:
                (x, y, w, h) = cara
                face = gray[y:y + w, x:x + h]
                label = face_recognizer.predict(face)

                if label is not None:
                    label_text = str(label[0])

                    # Pintar el rectangulo
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    # Poner texto
                    cv2.putText(frame, label_text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0),2)

        #muestro el frame resultante de el proceso
        cv2.imshow('img', frame)
        key = cv2.waitKey(5) #ver que hace???

        if key > 0:
            cv2.destroyAllWindows()
            for i in range(1, 5):
                cv2.waitKey(1)
            return
        time.sleep(0.05)
        rval, frame = cap.read()
    
    return

#Detectar rostros
def detectar_caras(frame):
    #cargar el clasificador
    face_cascade = cv2.CascadeClassifier("config/haarcascade-xml/haarcascade_frontalface_alt.xml")
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #detectando caras en escala de grises
    caras = face_cascade.detectMultiScale(gris, scaleFactor=1.2, minNeighbors=3)

    #Si no se detectan caras en la imagen devolvemos esto
    if(len(caras) == 0 ):
        return None, None

    #devuelvo donde esta la cara
    return caras, gris