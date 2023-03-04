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
from server import MQTTServer

# If running as main
if __name__ == '__main__':

    # Create server threads
    servers = []
    server1 = threading.Thread(target=MQTTServer, args=(
        '127.0.0.1',
        1883,
        'server/server1',
        ['1001/data', '1002/data']
    ))
    server2 = threading.Thread(target=MQTTServer, args=(
        '127.0.0.1',
        1883,
        'server/server2',
        ['1001/data', '1002/data']
    ))

    servers.append(server1)
    servers.append(server2)
    

    for server in servers:
        server.start()

    for server in servers:
        server.join()


