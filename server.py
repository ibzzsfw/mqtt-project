# Import Libraries
import os
import signal
import sys

# Import Packages
from server import Database, MQTTServer

# Broker Info
BROKER_IP = '127.0.0.1'
BROKER_PORT = 1883


def signal_handler(sig, frame):
    print('Keyboard interrupt detected, stopping server...')
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

# If running as main
if __name__ == '__main__':

    """For any prompt, if no input is given, the default value will be used"""

    # Get user input
    host = input('Enter broker ip: ')
    if host == '':
        host = BROKER_IP
    port = input('Enter broker port: ')
    if port == '':
        port = BROKER_PORT
    else:
        port = int(port)
    db_path = input('Enter database path: ')
    if db_path == '':
        db_path = 'server1'
    topics = input('Enter topics (comma splitted): ').split(',')
    if topics == ['']:
        topics = ['1001/data', '1002/data', '1001/ack', '1002/ack']

    mode = input("Enter mode\n1: start a server\n2: query database\n> ")
    """
    The server has 2 modes:
    1: start a server: start a server that will listen to the topics and store the data in the database
    2: query database: query the database for data
    """
    if mode == '1':
        print("PRESS CTRL+C TO STOP SERVER")
        # Running server
        server = MQTTServer(host, port, db_path, topics)

    if mode == '2':
        # check if database exists
        if not os.path.exists(f"{db_path}.sqlite"):
            print("Database does not exist")
            sys.exit(0)

        # Initialize database
        db = Database(f"{db_path}.sqlite")

        menu = int(input(
            "1: Query all data\n2: Query data by sensor\n3: Query data by node\n4: SQL query\n> ")
        )
        """
        The database query menu:
        1: Query all data: query all data from the database
        2: Query data by sensor: query data by sensor from the database by asking the user for the sensor
        3: Query data by node: query data by node from the database by asking the user for the nodeId
        4: SQL query: query the database by asking the user for any SQL query
        """
        fetched = []
        if menu == 1:
            fetched = db.get_all_data()
        if menu == 2:
            # Query data by topic
            sensor = input("Enter sensor: ")
            fetched = db.get_data_by_sensor(sensor)

        if menu == 3:
            # Query data by node
            node_id = input("Enter node id: ")
            fetched = db.get_data_by_node_id(node_id)

        if menu == 4:
            # Query data by manually inputting SQL query
            query = input("Enter SQL query: ")
            fetched = db.raw_query(query)

        # Print fetched data
        print(fetched)
        print("Server stopped after query")
