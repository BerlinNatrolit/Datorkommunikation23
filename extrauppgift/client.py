import paho.mqtt.client as mqtt
import time
import wmi
import os

if __name__ == '__main__':
    client = mqtt.Client()
    client.connect(host='broker.hivemq.com', port=1883, keepalive=60)

    while True:
        w = wmi.WMI(namespace="root\\OpenHardwareMonitor")
        CPU_pub = ""
        sensors = w.Sensor()
        for sensor in sensors:
            if sensor.SensorType == 'Temperature' and sensor.Name == 'CPU Package':
                CPU_pub = f"{os.getenv('COMPUTERNAME')}: {sensor.Name}: {sensor.Value} °C: Time: {int(time.time())}"
                
        client.publish("computerstats/stats", CPU_pub, qos=0)
        time.sleep(1)