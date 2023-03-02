import json

class Message:
    
    # Constructor to initialize message
    def __init__(self, type, message, timestamp):
        self.time = timestamp
        self.message = message
        self.type = type
    
    def createMessage():
        temp = {
            "time": self.time,
            "type": self.type,
            "message": self.message
        }
        return temp

    def toJson(self):
        return json.dumps(self.message)