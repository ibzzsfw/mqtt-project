import paho.mqtt.client as mqtt
import sqlite3 as sql
import json

# MQTT server configuration
server_address = "localhost"
server_port = 1883

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT server")
        client.subscribe("IoT_node")
    else:
        print("Failed to connect to MQTT server")

# Define on_message callback function for MQTT client
def on_message(client, userdata, message):
    db_file = "output.db"
    db_table = "sensors"
    
    # Parse sensor data from MQTT message payload
    sensor1_data = json.loads(message.payload.decode("utf-8"))
    nodeid = sensor1_data["nodeid"]
    timestamp = sensor1_data["timestamp"]
    humidity = sensor1_data["humidity"]
    temperature = sensor1_data["temperature"]
    thermalarray = sensor1_data["thermalarray"]

    db = sql.connect(db_file)
    cursor = db.cursor()

    # cursor.execute("CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY AUTOINCREMENT, node_id TEXT, timestamp TEXT, humidity REAL, temperature REAL, thermalarray REAL)".format(db_table))
        
    query = "INSERT INTO {} (node_id, timestamp, humidity, temperature, thermalarray) VALUES (?, ?, ?, ?, ?)".format(db_table)
    values = (nodeid, timestamp, humidity, temperature, thermalarray)
    cursor.execute(query, values)
    print(f"Received message: {message.payload.decode()}")

    db.commit()
    db.close()

    print("Stored sensor data from node " + str(nodeid) + " at " + str(timestamp))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Start MQTT client
client.connect(server_address, server_port)
client.loop_forever()