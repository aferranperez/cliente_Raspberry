import socket

#Variables Globales
CONNECTION_BROKER = -1  #Estado del la conexion con el MQTT Broker
MQTT_SERVER = "192.168.56.100"
ID_SUSCRIBE = "raspberry_prueba"
IP_ADDRESS = "127.0.0.1" #str(socket.gethostbyname(socket.gethostname()))
TOPICS_SUSCRIBE = [ "config_device/" ]

#Banderas Globales
#global STATE
STATE = False           #Bandera en True cuando se esta realizando el reconocimiento facial
SYNCRONIZED= False      #Comunicacion con .......
HAVE_MODEL = True      #Posee modelo en su carpeta de modelo

