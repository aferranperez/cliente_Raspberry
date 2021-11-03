import json
import socket
from config.data import *
from network import *

PORT_SOCKET = 6190

#Para cuando reciba el ACK del Broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado a MQTT Broker definido en la IP:" + MQTT_SERVER)
    else:
        print("Conexion Fallida")

#Para cuando se recibe un mensaje de los topics a los que se esta suscrito
def on_message(client, userdata, message):
    
    #Cuando recibo un mensaje
    if message.topic == "config_device/":
        payload_decode = json.loads(message.payload)

        print(payload_decode)
        #Accion para cargar modelo
        if payload_decode['action'] == "load_model" and payload_decode['data']['ip_destino'] == IP_ADDRESS:
            print("-------------------")
            print('topic: %s' % message.topic)
            print('payload: %s' % message.payload)
    
            payload = {
                'action' : 'respond_load_model',
                'data':{
                    'ip_address': '%s' % IP_ADDRESS,
                    'port' : '%s' % PORT_SOCKET,
                    'model_id' : '%s' %payload_decode['data']['model_id'],
                    'model_name' : '%s' %payload_decode['data']['model_name'],
                },
            } 

            payload =  json.dumps(payload)
            client.publish(topic="config_device/answer/", payload=payload, qos=0)

            conection = Socket_IoT()
            dir_dest = "models/" + str(payload_decode['data']['model_name']) + ".xml"
            conection.create_server(IP_ADDRESS, PORT_SOCKET, dir_dest)

