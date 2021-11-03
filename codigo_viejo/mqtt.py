from paho.mqtt.client import Client
from config.data import *
import json

class Client_MQTT:
    
    def __init__(self,client_id,mqtt_server):
        self.client_id = client_id
        self.mqtt_server = mqtt_server
        self.client_mqtt = Client(client_id=client_id,clean_session=False, transport="tcp")

    #Pasar el topic deseado en mqtt_topic
    #Pasar del json recibido, ip_devices = payload['devices']. Aqui estan los IP ha sincronizar
    #ip_address es el IP de este dispositivo
    #syncronized, es el estado de este Raspberry con respecto al servidor
    def synchronize_device(self,mqtt_topic,ip_devices,ip_address,syncronized):
        
        #Verifico que este dispositivo este, entre los que quieren sincronizar
        result = [True for device in ip_devices if ip_address == device] 
        
        if not(syncronized) and result:
            #mqtt_topic = "config_device/answer/"
            
            payload = {
                'action' : 'respond_syncronize',
                'data':{
                    'id_suscribe' : '%s' % self.client_id
                }
            }
            try:
                self.client_mqtt.connect(self.mqtt_server, port= 1883, keepalive=10)  
                
            except Exception as e:
                error = 'Ha ocurrido un error de %s' % e
                syncronized = False
            else:
                payload =  json.dumps(payload)
                self.client_mqtt.publish(topic=mqtt_topic, payload=payload,  qos=1)
                syncronized = True

        return syncronized

    def respond_state(self,mqtt_topic,state,have_model):
        
        payload = {
            'action' : 'respond_state',
            'data':{
                'id_suscribe': '%s' % self.client_id,
                'state' : '%s' %state,
                'have_model' : '%s' %have_model,
                'ip_address' : '%s' %state,
            },
        } 

        try:
            self.client_mqtt.connect(self.mqtt_server, port= 1883, keepalive=10)  
        
        except Exception as e:
            error = 'Ha ocurrido un error de %s' % e
   
        else:
            payload =  json.dumps(payload)
            self.client_mqtt.publish(topic=mqtt_topic, payload=payload,  qos=1)
 
    def initialize_client_MQTT(self,mqtt_server):

        try:
            self.client_mqtt.connect(mqtt_server,port=1883,keepalive=5)
                
        except Exception as e:
            error = 'Ha ocurrido un error de %s' % e
            return False, e

        else:
            self.client_mqtt.subscribe("config_device/", qos=0)
            return True, True






            


    