"""Temperature message class. Child class of Message class."""
from .message import Message

class Temperature(Message):
    
    # Constructor to initialize temperature message
    def __init__(self, content, timestamp):
        super().__init__('temperature', content, timestamp)