
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
    def publish(self, message):
        self.client.publish(self.topic, message)

    """
    Function to subscribe to topic
    self: MqttClient
    """
    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()