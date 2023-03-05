"""
    Information about the client and server threads:

    Client1: localhost:1883, 1001, input.xlsx, node1
    Client2: localhost:1883, 1002, input.xlsx, node2

    Broker: localhost:1883

    Server1: localhost:1883, server1, ['1001/data', '1002/data']
    Server2: localhost:1883, server2, ['1001/data', '1002/data']
"""

# Import Libraries
import signal
import sys

# Import Packages
from client import MQTTClient


def signal_handler(sig, frame):
    print('Keyboard interrupt detected, stopping server...')
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

# If running as main
if __name__ == '__main__':

    # Create CLI for user to input broker ip, port, node id, xlsx file path, sheet name

    host = input("Broker IP: ")
    if host == '':
        host = 'localhost'
    port = input("Broker Port: ")
    if port == '':
        port = 1883
    else:
        port = int(port)
    node_id = input("Node ID: ")
    if node_id == '':
        node_id = '1001'
    xlsx_file_path = input("XLSX file path: ")
    if xlsx_file_path == '':
        xlsx_file_path = 'input.xlsx'
    sheet_name = input("Sheet name: ")
    if sheet_name == '':
        sheet_name = 'node1'

    print("PRESS CTRL+C TO STOP SERVER")

    # Running client
    MQTTClient(host, port, node_id, xlsx_file_path, sheet_name)
