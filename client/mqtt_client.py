"""
 MQTT Client has three types of sensors 
 
 - Client simultaneously reads all the sensors every 3 minutes 
 - and wants to send the sensor data to Broker together with 4-digit node id and current time (Date, hours, minutes). 
 
 To emulate the sensor readings without installing real sensors, Client can read sensor data stored in an Excel file and sends to Broker.

 Constraints:
- Client can only send at most 250 bytes in one message.
"""

import threading
import time

import paho.mqtt.client as mqtt
from sensor_reader import SensorReader

# from logger.logger import Logger

MAX_PAYLOAD_SIZE = 250
READ_INTERVAL = 0.1  # * 60  # 3 minutes


class MQTTClient():
    def __init__(self, broker_ip, broker_port, node_id, xlsx_file_path, sheet_name):
        # super().__init__(f'client {node_id}')
        self.broker_ip = broker_ip
        self.broker_port = broker_port
        self.node_id = node_id
        self.xlsx_file_path = xlsx_file_path
        self.sheet_name = sheet_name
        self.topic = f'{self.node_id}/data'

        self.client = mqtt.Client()
        self.client.connect(self.broker_ip, self.broker_port)
        self.client.enable_logger()
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        # self.on_publish = self.on_publish
        # self.on_message = self.on_message
        self.client.loop_start()

        self.send_sensor_data(self.node_id, self.sheet_name)

    def send_sensor_data(self, node_id, sheet_name):
        stream = SensorReader(self.xlsx_file_path, sheet_name)
        if stream is None:
            print("Invalid stream source.")
            exit()

        # Send sensor data
        for i in range(stream.shape[0]):
            data = stream.get_data_by_row(i)
            payload = f"{node_id};{data['time']};{data['humidity']};{data['temperature']};{data['thermal_array']}"
            self.client.publish("client/log", f"client {self.node_id} sent {self.topic}")
            self.client.publish(self.topic, payload)
            time.sleep(READ_INTERVAL)

        self.client.publish(f'client/log', f'client {self.node_id} disconnected')
        self.client.disconnect()

    def on_connect(self, client, userdata, flags, rc):
        ip = client._sock.getpeername()[0]
        port = client._sock.getpeername()[1]
        self.client.publish(f'client/log', f'client {ip}:{port} connected as client {self.node_id}')

    def on_disconnect(self, client, userdata, rc):
        ip = client._sock.getpeername()[0]
        port = client._sock.getpeername()[1]

    def disconnect(self):
        self.client.disconnect()
        self.client.loop_stop()


if __name__ == '__main__':
    """
    Client1: localhost:1883, 1001, input.xlsx, node1
    Client2: localhost:1883, 1002, input.xlsx, node2
    """
    clients = []
    # Threding clients
    client1 = threading.Thread(target=MQTTClient, args=(
        'localhost',
        1883,
        '1001',
        'input.xlsx',
        'node1'
    ))
    client2 = threading.Thread(target=MQTTClient, args=(
        'localhost',
        1883,
        '1002',
        'input.xlsx',
        'node2'
    ))

    clients.append(client1)
    clients.append(client2)

    for client in clients:
        client.start()

    for client in clients:
        client.join()
