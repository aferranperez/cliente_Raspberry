import json
import socket
from config.data import *
import network

PORT = 6190

def on_message(client, userdata, message):
    
    #Cuando recibo un mensaje
    if message.topic == "config_device/":
        payload_decode = json.loads(message.payload)


        #Accion para cargar modelo
        if payload_decode['action'] == "load_model" and payload_decode['data']['ip_destino'] == IP_ADDRESS:
            print("-------------------")
            print('topic: %s' % message.topic)
            print('payload: %s' % message.payload)
    
            payload = {
                'action' : 'respond_load_model',
                'data':{
                    'ip_address': '%s' % IP_ADDRESS,
                    'port' : '%s' % PORT,
                    'model_id' : '%s' %payload_decode['data']['model_id'],
                    'model_name' : '%s' %payload_decode['data']['model_name'],
                },
            } 

            payload =  json.dumps(payload)
            
            
            client.publish(topic="config_device/answer/", payload=payload, qos=0)
            
            conection = network.Socket_IoT()
            dir_dest = "models/" + str(payload_decode['data']['model_name']) + ".xml"
            conection.create_server(IP_ADDRESS, PORT, dir_dest)
