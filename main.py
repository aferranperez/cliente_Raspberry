from time import sleep
from uuid import SafeUUID
from config.data import *
from mqtt import *
import network
import face_recognizer


def main():
    #Inicializando cliente para mosquitto
    global CONNECTION_BROKER

    client_mqtt = create_client()

    #Diferente de 0, no hay comunicacion con el broker
    while CONNECTION_BROKER != 0:
        
        #Intento conectarme con el broker
        try:
            connect_mqtt(client_mqtt)
            client_mqtt.loop_start()
            
        except Exception as e:
            #Disparo error de conexion
            print("[Error] No se puede conectar con MQTT Broker definido en la IP: " + MQTT_SERVER )

        else:
            #Se logro la comunicacion con el broker, cambio la variable global de la conexion
            CONNECTION_BROKER = 0

            #LLamo a la funcion "suscribe_to_topics" en mqtt.py
            suscribe_to_topics(client_mqtt)

            #Bloques de codigo a realizar, mientras se esta conectado al broker
            while CONNECTION_BROKER == 0:
                #Si es True la bandera "recv_data", preparo el raspberry para recibir datos
                if network.recv_data:
                    print("-------------------")
                    print("Preparando dispositivo para recepcion de modelo...")
                    
                    try:
                        network.create_server(IP_ADDRESS, PORT_SOCKET, network.dir_dest_model)
                    except Exception as e:
                        print("[Error] No se puede recibir el modelo correctamente:" + str(e))
                    else:
                        config.data.DIR_MODEL = network.dir_dest_model
                        config.data.HAVE_MODEL = True
                        print("-------------------")
                
                
                elif config.data.STATE and config.data.HAVE_MODEL:
                    #LLamo a la funcion para empezar a reconocer rostros
                    face_recognizer.clasificar_rostro()
                    print("-------------------")
                    print("[INFO] Finalizo el modulo de Reconocimiento Facial.")
                    print("-------------------")
                    #Pongo el estado del raspberry a 0, ya que se dejo de reconocer rostros
                    config.data.STATE = False


                sleep(5)
                print("[INFO] Esperando señalizacion del ADMIN.")


if __name__ == '__main__':
    main()
