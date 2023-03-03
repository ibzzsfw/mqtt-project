import pandas as pd
import random
import paho.mqtt.client as mqtt
import json
import datetime

# MQTT broker configuration
broker_address = "localhost"
broker_port = 1883

def read_sensors_node1():
    df = pd.read_excel('input.xlsx', sheet_name='node1')
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    humi = df['Humidity']
    temp = df['Temperature']
    thermal = df['ThermalArray']
    n = random.randint(0, len(humi) - 1)
    return {
        "nodeid": 1001,
        "timestamp": timestamp,
        "humidity": humi[n],
        "temperature": temp[n],
        "thermalarray": thermal[n]
    }

client_id = "IoT_node"
sensor1_data = read_sensors_node1()

client = mqtt.Client(client_id)
client.connect(broker_address, broker_port)

client.publish("IoT_node", json.dumps(sensor1_data))

client.disconnect()
