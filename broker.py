"""
    Information about the client and server threads:

    Client1: localhost:1883, 1001, input.xlsx, node1
    Client2: localhost:1883, 1002, input.xlsx, node2

    Broker: localhost:1883

    Server1: localhost:1883, server1, ['1001/data', '1002/data']
    Server2: localhost:1883, server2, ['1001/data', '1002/data']
"""

# Import Libraries
# import threading

# Import Packages
from broker import MQTTBroker


# Broker Info
BROKER_IP = '127.0.0.1'
BROKER_PORT = 1883

# If running as main
if __name__ == '__main__':
    # Create broker
    broker = MQTTBroker(BROKER_IP, BROKER_PORT)
