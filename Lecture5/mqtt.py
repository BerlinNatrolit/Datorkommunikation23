import paho.mqtt.client as mqtt
from typing import Any, Optional


def on_connect(client, userdata, flags, rc):
    """ Anropas när vi ansluter till brokern """
    # rc = result code
    print(f"Connected to server, with result code {rc}")

    # Om vi lyckades ansluta, gör subscribe till en topic
    client.subscribe(topic="testtopic/kyh")


def on_message(client, userdata, message):
    """ Anropas när vi får ett meddelande från brokern """
    print(f"Topic: {message.topic}, Message: {message.payload.decode('utf-8')}")


def main():
    client = mqtt.Client()

    # Ställ in vad som händer när klienten anslutit eller tagit emot meddelanden
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set("fatima", "123456")

    # Anslut till en broker
    # localhost
    # 127.0.0.1
    # 192.168.0.89		min egna lokala dator
    client.connect(host='localhost', port=1883, keepalive=60)

    client.publish("testtopic/kyh", "hello world", qos=1)

    # Lyssna på trafik
    client.loop_forever()
    



if __name__ == '__main__':
    main()