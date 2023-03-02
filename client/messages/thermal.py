import json
from client.messages.message import Message

class Thermal(Message):
    
    # Constructor to initialize thermal message
    def __init__(self, message, timestamp):
        super().__init__('thermal', message, timestamp)
