"""Module to handle MQTT Client."""

# Import libraries
import paho.mqtt.client as mqtt

# Import modules
from client.messages.message import Message
from client.messages.thermal import Thermal
from client.messages.humidity import Humidity
from client.messages.temperature import Temperature

class MqttClient:

    """
    Function to initialize client
    client_id: string
    broker: string
    port: int
    topic: string
    """
    def __init__(self, client_id, broker, port, topic):
        self.client_id = client_id
        self.broker = broker
        self.port = port
        self.topic = topic
        self.client = mqtt.Client(client_id=self.client_id)

    """
    Function to connect to broker
    self: MqttClient
    """
    def connect(self):
        self.client.connect(self.broker, self.port)
        self.client.loop_start()

    """
    Function to publish message to broker
    self: MqttClient
    message: string
    """
    def publish(self, type, content, timestamp):
        if type == 'thermal':
            message = Thermal(content, timestamp)
        elif type == 'humidity':
            message = Humidity(content, timestamp)
        elif type == 'temperature':
            message = Temperature(content, timestamp)

        else: 
            message = Message('other', content, timestamp)
        self.client.publish(self.topic, message.getJson())

    """
    Function to disconnect from broker
    self: MqttClient
    """
    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()