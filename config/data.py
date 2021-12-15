import socket

#Variables Globales
CONNECTION_BROKER = -1  #Estado del la conexion con el MQTT Broker
MQTT_SERVER = "192.168.56.100"
ID_SUSCRIBE = "raspberry_prueba"
IP_ADDRESS = "127.0.0.1" #str(socket.gethostbyname(socket.gethostname()))
TOPICS_SUSCRIBE = [ "config_device/" ]

DIR_MODEL = ""

#Banderas Globales
STATE = True#False           #Bandera en True cuando se esta realizando el reconocimiento facial
SYNCRONIZED= False      #Comunicacion con .......
HAVE_MODEL = False       #Posee el modelo seleccionado en el ADMIN, en su carpeta de modelo

