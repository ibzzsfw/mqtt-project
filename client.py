"""
    Information about the client and server threads:

    Client1: localhost:1883, 1001, input.xlsx, node1
    Client2: localhost:1883, 1002, input.xlsx, node2

    Broker: localhost:1883

    Server1: localhost:1883, server1, ['1001/data', '1002/data']
    Server2: localhost:1883, server2, ['1001/data', '1002/data']
"""

# Import Libraries
import threading

# Import Packages
from client import MQTTClient

# If running as main
if __name__ == '__main__':
    
    # Create client threads
    clients = []
    client1 = threading.Thread(target=MQTTClient, args=(
        'localhost',
        1883,
        '1001',
        'input.xlsx',
        'node1'
    ))

    client2 = threading.Thread(target=MQTTClient, args=(
        'localhost',
        1883,
        '1002',
        'input.xlsx',
        'node2'
    ))

    clients.append(client1)
    clients.append(client2)

    for client in clients:
        client.start()

    for client in clients:
        client.join()

