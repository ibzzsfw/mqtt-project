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

import threading

import paho.mqtt.client as mqtt
from database import Database


class MQTTServer():
    def __init__(self, broker_ip, broker_port, db_path, topics):
        self.broker_ip = broker_ip
        self.broker_port = broker_port
        self.db_path = db_path
        self.topics = topics

        self.client = mqtt.Client()
        self.client.connect(self.broker_ip, self.broker_port, 10)
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message

        # Connect to the database
        self.db = Database(self.db_path + '.sqlite')
        self.db.delete_all_data()
        self.client.loop_forever()

    def on_connect(self, client, userdata, flags, rc):
        ip = client._sock.getpeername()[0]
        port = client._sock.getpeername()[1]
        self.client.publish(f"server/log", f"server {ip}:{port} connected")
        for topic in self.topics:
            self.client.publish(f"server/log", f"server {ip}:{port} subscribed to {topic}")
            self.client.subscribe(topic)

    def on_disconnect(self, client, userdata, rc):
        ip = client._sock.getpeername()[0]
        port = client._sock.getpeername()[1]
        self.client.publish(f"server/log", f"server {ip}:{port} disconnected")

    def on_message(self, client, userdata, msg):
        node_id, time, humidity, temperature, thermal_array = msg.payload.decode().split(';')
        self.db.insert_data(node_id, time, humidity,
                            temperature, thermal_array)


if __name__ == '__main__':

    servers = []

    server1 = threading.Thread(target=MQTTServer, args=(
        'localhost',
        1883,
        'server1',
        ['1001/data', '1002/data']
    ))
    server2 = threading.Thread(target=MQTTServer, args=(
        'localhost',
        1883,
        'server2',
        ['1001/data', '1002/data']
    ))

    servers.append(server1)
    servers.append(server2)

    for server in servers:
        server.start()

    for server in servers:
        server.join()
