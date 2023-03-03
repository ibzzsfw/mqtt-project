import paho.mqtt.client as mqtt

# MQTT server configuration
broker_address = "localhost"
broker_port = 1883

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        client.subscribe("IoT_node")
    else:
        print("Failed to connect to MQTT broker")

def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()}")

try:
    broker = mqtt.Client()
    broker.on_connect = on_connect
    broker.on_message = on_message

    # Start MQTT broker
    broker.connect(broker_address, broker_port)
    broker.loop_forever()
except ConnectionRefusedError:
    print("Connection refused: MQTT broker not running or incorrect broker address/port")