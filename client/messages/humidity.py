import json
from .message import Message

class Humidity(Message):
    
    # Constructor to initialize humidity message
    def __init__(self, content, timestamp):
        super().__init__('humidity', content, timestamp)
