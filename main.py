from time import sleep
from config.data import *
from mqtt import *

CONNECTION_BROKER = -1

def main():
    #Inicializando cliente para mosquitto
    global CONNECTION_BROKER

    #Diferente de 0, no hay comunicacion con el broker
    while CONNECTION_BROKER != 0:
        try:
            client_mqtt = connect_mqtt()
            client_mqtt.loop_start()

        except Exception as e:
            print("[Error] No se puede conectar con MQTT Broker definido en la IP: " + MQTT_SERVER )

        else:
            #Se logro la comunicacion con el broker
            CONNECTION_BROKER = 0

            #Bloque a realizar mientras esta conectado al broker
            while CONNECTION_BROKER == 0:
                print("Hola")
                suscribe_to_topics(client_mqtt)
                sleep(4)


if __name__ == '__main__':
    main()
