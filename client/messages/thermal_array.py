import json
from client.messages.message import Message

class ThermalArray(Message):
        
    # Constructor to initialize thermal array message
    def __init__(self, message, timestamp):
        super().__init__('thermal_array', message, timestamp)
