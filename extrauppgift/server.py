import paho.mqtt.client as mqtt
from typing import Any, Optional
import os

data = {}
log = []

def on_connect(client, userdata, flags, rc):
    """ Anropas när vi ansluter till brokern """
    # rc = result code
    print(f"Connected to server, with result code {rc}")

    # Om vi lyckades ansluta, gör subscribe till en topic
    client.subscribe(topic="computerstats/stats")


def on_message(client, userdata, message):
    """ Anropas när vi får ett meddelande från brokern """
    # print(f"Topic: {message.topic}, Message: {message.payload.decode('utf-8')}")
    try:
        m = message.payload.decode().split(":")
        data[m[0]] = m[2]
    except:
        log.append(str(userdata) + ":" + message.payload.decode())
        if len(log) >= 10:
            log.remove(0)
    
    os.system("cls")
    print("===========================================")
    print("Stats")
    print("===========================================")
    for k, v in data.items():
        print(k + ": " + v)
    print()
    print("===========================================")
    print("People with problems end up here:")
    print("===========================================")
    for l in log:
        print(l)

def main():
    client = mqtt.Client()

    # Ställ in vad som händer när klienten anslutit eller tagit emot meddelanden
    client.on_connect = on_connect
    client.on_message = on_message

    # Anslut till en broker
    client.connect(host='broker.hivemq.com', port=1883, keepalive=60)

    # Lyssna på trafik
    client.loop_forever()
    

if __name__ == '__main__':
    main()