import json
from time import sleep

from cv2 import data
from config.data import *
import network
import config.data

PORT_SOCKET = 6190

#Para cuando reciba el ACK del Broker al establecer comunicacion
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado a MQTT Broker definido en la IP:" + MQTT_SERVER)
    else:
        print("Conexion Fallida")

#Para cuando se recibe un mensaje de los topics a los que se esta suscrito
def on_message(client, userdata, message):

    #Cuando recibo un mensaje del admin
    if message.topic == "config_device/":
        
        try:
            payload_decode = json.loads(message.payload)

        except Exception as e:
            #Disparo error de conexion
            print("[Error] No se puede decodificar el JSON recibido: " + str(e) )

        else:
            print("-------------------")
            print("[Info] Mensaje recibo del topic: " + message.topic)
            print("Contenido del payload: ")
            print(payload_decode)
            print("-------------------")

            # Verificar que se desea cargar un modelo
            # Verificar que sea el dispositivo correcto por la IP
            if payload_decode['action'] == "load_model" and payload_decode['data']['ip_destino'] == IP_ADDRESS:
                #
                payload_respond = {
                    'action' : 'respond_load_model',
                    'data' : {
                        'ip_address': '%s' % IP_ADDRESS,
                        'port' : '%s' % PORT_SOCKET,
                        'model_id' : '%s' %payload_decode['data']['model_id'],
                        'model_name' : '%s' %payload_decode['data']['model_name'],
                    },
                } 

                payload_respond =  json.dumps(payload_respond)
                
                client.publish(topic="config_device/answer/", payload=payload_respond, qos=0)
                
                #Preparar Raspberry para recibir archivo de modelo
                network.recv_data = True
                network.dir_dest_model = "models/" + str(payload_decode['data']['model_name']) + ".xml"

            elif payload_decode['action'] == "set_state" and payload_decode['data']['ip_destino'] == IP_ADDRESS:
                config.data.STATE = not(config.data.STATE)

                payload_respond = {
                    'action' : 'respond_set_state',
                    'data' : {
                        'actual_state' : '%s' % config.data.STATE,
                        'ip_address' : '%s' % IP_ADDRESS,
                    }
                }

                payload_respond =  json.dumps(payload_respond)
                client.publish(topic="config_device/answer/", payload=payload_respond, qos=0)
