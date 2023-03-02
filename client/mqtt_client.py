"""
 MQTT Client has three types of sensors 
 
 – Relative humidity, temperature, and thermal array. 
    - The relative humidity readings are between 0 to 100 percent, 
    - the temperature readings are between 0 to 90 degree celsius, 
    - the thermal array readings are 24×32 where each array value represents a temperature reading between 5 to 60 degree celsius. 
 
 - Client simultaneously reads all the sensors every 3 minutes 
 - and wants to send the sensor data to Broker together with 4-digit node id and current time (Date, hours, minutes). 
 
 To emulate the sensor readings without installing real sensors, Client can read sensor data stored in an Excel file and sends to Broker.
 Constraints:
- Client can only send at most 250 bytes in one message.
"""

# Import libraries
import paho.mqtt.client as mqtt

# Import modules
from client.messages.message import Message
from client.messages.thermal import Thermal
from client.messages.humidity import Humidity
from client.messages.thermal_array import ThermalArray
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
        elif type == 'thermal_array':
            message = ThermalArray(content, timestamp)
        else: 
            message = Message('other', content, timestamp)
        self.client.publish(self.topic, message.getJson())

    """
    Function to subscribe to topic
    self: MqttClient
    """
    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()