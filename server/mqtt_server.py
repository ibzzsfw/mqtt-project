"""
MQTT Server subscribes for data from Client. 

- The received data is assembled as necessary and written in the local database sqlite3 for later query or visualization. 
- Data sent in the same round from Client must be stored in the same database record. 
- Any lost data would result in missing values in the database records.

Constraints:
- server prints out received messages from Broker on the screen.
- At Server, one must be able to query data of each sensor separately from the database.
- Multiple IoT nodes and servers can be deployed in the system. If Server subscribes data from several clients, all the data is stored in the same database table.
"""

# import threading

import paho.mqtt.client as mqtt

from .database import Database
from logger import Logger


class MQTTServer():
    def __init__(self, broker_ip, broker_port, db_path, topics):
        self.broker_ip = broker_ip
        self.broker_port = broker_port
        self.db_path = db_path
        self.buffersize = 0
        self.buffer = ''
        self.data_chunks = {}
        self.topics = topics
        self.client = mqtt.Client()
        self.client.connect(self.broker_ip, self.broker_port)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        # Connect to the database
        self.db = Database(self.db_path + '.sqlite')
        self.db.delete_all_data()

        self.ip = ""
        self.port = 0

        self.client.loop_forever()

    def on_connect(self, client, userdata, flags, rc):
        self.ip = client._sock.getpeername()[0]
        self.port = client._sock.getpeername()[1]
        self.client.publish(
            f"server/log", f"server {self.ip}:{self.port} connected")
        for topic in self.topics:
            self.client.publish(
                f"server/log", f"server {self.ip}:{self.port} subscribed to {topic}")
            self.client.subscribe(topic)

    def disconnect(self):
        self.client.publish(
            f"server/log", f"server {self.ip}:{self.port} disconnected")
        self.client.disconnect()
        self.client.loop_stop()

    def on_message(self, client, userdata, msg):

        if msg.topic.endswith('data'):
            print(f"Received messages: {msg.payload.decode()}")

            # Split the message into its components
            node_id, expected_length, data_chunk = msg.payload.decode().split('/')

            # Convert the expected length to an integer
            expected_length = int(expected_length)
            if node_id not in self.data_chunks:
                # Start a new list for this node_id
                self.data_chunks[node_id] = [data_chunk]
            else:
                # Append the data chunk to the existing list
                self.data_chunks[node_id].append(data_chunk)

            # Check if all the chunks have been received
            if sum(len(chunk) for chunk in self.data_chunks[node_id]) == expected_length:

                # Concatenate the chunks into a single string
                data_string = ''.join(self.data_chunks[node_id])

                # Split the data string into its components
                node_id, time, humidity, temperature, thermal_array = data_string.split(
                    ';')

                # Insert the data into the database
                self.db.insert_data(node_id, time, humidity,
                                    temperature, thermal_array)

                # Reset the list of chunks for this node_id
                self.data_chunks[node_id] = []
