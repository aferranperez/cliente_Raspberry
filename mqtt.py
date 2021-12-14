from config.data import *
from paho.mqtt.client import Client
from callback_mqtt import *

#Esta funcion es para crear el cliente MQTT
def create_client():
    #Set Connecting Client ID
    client_mqtt = Client(client_id=ID_SUSCRIBE)
    client_mqtt.on_connect = on_connect
    client_mqtt.on_message = on_message
    return client_mqtt

#Conecta con el broker
def connect_mqtt(client):
    client.connect(MQTT_SERVER, port=1883)

#Se suscribe a cada topic definido en data.py
def suscribe_to_topics(client):
    
    for topic in TOPICS_SUSCRIBE:
        client.subscribe(topic, qos=0)


