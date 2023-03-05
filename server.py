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
import os

import sqlite3

# Import Packages
from server import MQTTServer, Database


def signal_handler(sig, frame):
    print('Keyboard interrupt detected, stopping server...')
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

# If running as main
if __name__ == '__main__':

    host = input('Enter broker ip: ')
    if host == '':
        host = 'localhost'
    port = input('Enter broker port: ')
    if port == '':
        port = 1883
    else:
        port = int(port)
    db_path = input('Enter database path: ')
    if db_path == '':
        db_path = 'server1'
    topics = input('Enter topics (comma splitted): ').split(',')
    if topics == ['']:
        topics = ['1001/data', '1002/data, 1001/ack, 1002/ack']

    mode = input("Enter mode (1: start a server, 2: query database): ")
    if mode == '1':
        print("PRESS CTRL+C TO STOP SERVER")
        # Running server
        MQTTServer(host, port, db_path, topics)

    if mode == '2':
        # check if database exists
        if not os.path.exists(f"{db_path}.sqlite"):
            print("Database does not exist")
            sys.exit(0)

        db = Database(f"{db_path}.sqlite")

        menu = int(input(
            "1 to query all data\n2 to query data by sensor\n3 to query data by node\n4 SQL query\n: "))
        fetched = []
        if menu == 1:
            # Query all data
            fetched = db.get_all_data()
        if menu == 2:
            # Query data by topic
            sensor = input("Enter sensor: ")
            # Query data by topic
            fetched = db.get_data_by_sensor(sensor)

        if menu == 3:
            # Query data by node
            node = input("Enter node: ")
            # Query data by node
            fetched = db.get_data_by_node_id(node)

        if menu == 4:
            # SQL query
            query = input("Enter SQL query: ")
            # SQL query
            fetched = db.raw_query(query)

        if fetched == []:
            print("Invalid input")
            sys.exit(0)
        print(fetched)
