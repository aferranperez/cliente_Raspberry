from time import sleep
from config.data import *
from mqtt import *
import network
import face_recognizer

def main():
    #Inicializando cliente para mosquitto
    global CONNECTION_BROKER
    global STATE

    client_mqtt = create_client()

    #Diferente de 0, no hay comunicacion con el broker
    while CONNECTION_BROKER != 0:
        try:
            connect_mqtt(client_mqtt)
            client_mqtt.loop_start()

        except Exception as e:
            print("[Error] No se puede conectar con MQTT Broker definido en la IP: " + MQTT_SERVER )

        else:
            #Se logro la comunicacion con el broker
            CONNECTION_BROKER = 0
            suscribe_to_topics(client_mqtt)

            #Bloque a realizar mientras esta conectado al broker
            while CONNECTION_BROKER == 0:
    
                #Si es True preparo el raspberry para recibir datos
                if network.recv_data:
                    print("-------------------")
                    print("Preparando dispositivo para recepcion de modelo...")
                    network.create_server(IP_ADDRESS, PORT_SOCKET, network.dir_dest_model)
                    print("-------------------")
                
                elif STATE and HAVE_MODEL:
                    face_recognizer.clasificar_rostro()
                    print("Hizo la funcion")
                    STATE = 0



                sleep(5)
                print("[INFO] Esperando señalizacion del ADMIN.")


if __name__ == '__main__':
    main()
