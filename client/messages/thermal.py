import json
from .message import Message

class Thermal(Message):
    
    # Constructor to initialize thermal message
    def __init__(self, content, timestamp):
        super().__init__('thermal', content, timestamp)
