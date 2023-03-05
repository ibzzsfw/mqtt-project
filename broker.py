# Import Libraries
import signal
import sys

# Import Packages
from broker import MQTTBroker

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

    print("PRESS CTRL+C TO STOP SERVER")
    # Start broker
    MQTTBroker(host, port)
