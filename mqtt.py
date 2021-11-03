from config.data import *
from paho.mqtt.client import Client
from callback_mqtt import *

topics_suscribe = [ "config_device/" ]

def connect_mqtt():
    #Set Connecting Client ID
    client_mqtt = Client(client_id=ID_SUSCRIBE)
    client_mqtt.on_connect = on_connect
    client_mqtt.on_message = on_message
    client_mqtt.connect(MQTT_SERVER, port=1883)
    return client_mqtt
    
def suscribe_to_topics(client):
    
    for topic in topics_suscribe:
        client.subscribe(topic, qos=0)


