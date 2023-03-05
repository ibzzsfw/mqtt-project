# Import Libraries
import signal
import sys

# Import Packages
from client import MQTTClient

# Broker Info
BROKER_IP = '127.0.0.1'
BROKER_PORT = 1883


def signal_handler(sig, frame):
    print('Keyboard interrupt detected, stopping server...')
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

# If running as main
if __name__ == '__main__':

    host = input("Broker IP: ")
    if host == '':
        host = BROKER_IP
    port = input("Broker Port: ")
    if port == '':
        port = BROKER_PORT
    else:
        port = int(port)
    node_id = input("Node ID: ")
    if node_id == '':
        node_id = '1001'
    xlsx_file_path = input("XLSX file path: ")
    if xlsx_file_path == '':
        xlsx_file_path = 'input'
    sheet_name = input("Sheet name: ")
    if sheet_name == '':
        sheet_name = 'node1'

    print("PRESS CTRL+C TO STOP SERVER")

    # Running client
    MQTTClient(host, port, node_id, f"{xlsx_file_path}.xlsx", sheet_name)
