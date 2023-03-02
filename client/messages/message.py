import json

class Message:
    
    # Constructor to initialize message
    def __init__(self, type, content, timestamp):
        self.time = timestamp
        self.content= content
        self.type = type
        self.createMessage()
        self.toJson()
    
    # Function to create message (dictionary format)
    def createMessage(self, content, timestamp, type):
        if (content == None & timestamp == None & type == None) :
            temp = {
                "time": timestamp,
                "type": type,
                "content": content
            }
        else :
            temp = {
                "time": self.time,
                "type": self.type,
                "content": self.content
            }
        self.message = temp
        return self.message
    
    # Function to convert message to json format
    def toJson(self, message):
        if (message == None) :
            self.json = json.dumps(self.createMessage())
        else :
            self.json = json.dumps(message)
        return self.json
    
    """
    Getter functions and Setter functions
    """
    def getMessage(self):
        return self.message

    def getJson(self):
        return self.toJson()
