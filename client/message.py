import json

class Message:
    
    # Constructor to initialize message
    def __init__(self, message):
        self.message = message
    
    # Convert message to json
    def to_json(self.message):
        return json.dumps(self.message)
