from mqtt import Client_MQTT
from callback_mqtt import on_message
from config.data import *

def main():
    #Inicializando cliente para mosquitto
    cliente = Client_MQTT(ID_SUSCRIBE, MQTT_SERVER)

    result, error = cliente.initialize_client_MQTT(MQTT_SERVER)


    if result:
        cliente.client_mqtt.on_message = on_message
        cliente.client_mqtt.loop_start()
        while True:
            continue
    else:
        print (f" {result} , {error}")
            


if __name__ == '__main__':
    main()

