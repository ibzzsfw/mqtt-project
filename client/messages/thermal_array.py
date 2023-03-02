import json
from .message import Message

class ThermalArray(Message):
        
    # Constructor to initialize thermal array message
    def __init__(self, content, timestamp):
        super().__init__('thermal_array', content, timestamp)
