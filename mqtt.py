from config.data import *
from paho.mqtt.client import Client
from callback_mqtt import *



def create_client():
    #Set Connecting Client ID
    client_mqtt = Client(client_id=ID_SUSCRIBE)
    client_mqtt.on_connect = on_connect
    client_mqtt.on_message = on_message
    return client_mqtt

def connect_mqtt(client):
    client.connect(MQTT_SERVER, port=1883)

def suscribe_to_topics(client):
    
    for topic in TOPICS_SUSCRIBE:
        client.subscribe(topic, qos=0)


