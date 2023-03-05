"""
MQTT Broker forwards any data it receives to its subscribers.

Constraints:
- prints out an IP address on the screen when a new subscriber or publisher connects or disconnects.
- prints out published messages on the screen.
"""

import paho.mqtt.client as mqtt
# import module paho-mqtt  
from logger import Logger
# import class logger

# class MQTTBroker inherits from class Logger
class MQTTBroker(Logger):
    # method __init__ is called when an object of class MQTTBroker is created
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

    # method on_connect is called when broker connects to broker
    def on_connect(self, client, userdata, flags, rc):
        """Callback when broker connects to broker"""
        self.info(f"broker {self.broker_ip}:{self.broker_port} connected")

    # method on_connect is called when broker connects to broker
    def on_disconnect(self, client, userdata, rc):
        """Callback when broker disconnects from broker"""
        self.info(f"broker {self.broker_ip}:{self.broker_port} disconnected")

    # method on_message is called when broker receives a message
    def on_message(self, client, userdata, msg):
        """Callback when broker receives a message"""
        if msg.topic.endswith('log'):
            self.info(msg=bytes(msg.payload).decode('utf-8'))
