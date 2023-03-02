import json
from client.messages.message import Message

class Humidity(Message):
    
    # Constructor to initialize humidity message
    def __init__(self, message, timestamp):
        super().__init__('humidity', message, timestamp)
