"""
MQTT Broker forwards any data it receives to its subscribers.

Constraints:
- prints out an IP address on the screen when a new subscriber or publisher connects or disconnects.
- prints out published messages on the screen.
"""

import paho.mqtt.client as mqtt

# from client.mqtt_client import MQTTClient
# from server.mqtt_server import MQTTServer
from logger import Logger

BROKER_IP = '127.0.0.1'
BROKER_PORT = 1883


class MQTTBroker(Logger):
    def __init__(self, broker_ip, broker_port):
        super().__init__('broker')
        self.broker_ip = broker_ip
        self.broker_port = broker_port

        self.broker = mqtt.Client()
        self.broker.connect(self.broker_ip, self.broker_port)
        self.broker.on_connect = self.on_connect
        self.broker.on_disconnect = self.on_disconnect
        self.broker.on_message = self.on_message

        self.broker.subscribe('#')
        self.broker.loop_forever()

    def on_connect(self, client, userdata, flags, rc):
        self.info(f"broker {self.broker_ip}:{self.broker_port} connected")

    def on_disconnect(self, client, userdata, rc):
        self.info(f"broker {self.broker_ip}:{self.broker_port} disconnected")

    def on_message(self, client, userdata, msg):
        if msg.topic.endswith('log'):
            self.info(msg=bytes(msg.payload).decode('utf-8'))


if __name__ == '__main__':
    broker = MQTTBroker(BROKER_IP, BROKER_PORT)
