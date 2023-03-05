"""
 MQTT Client has three types of sensors 
 
 - Client simultaneously reads all the sensors every 3 minutes 
 - and wants to send the sensor data to Broker together with 4-digit node id and current time (Date, hours, minutes). 
 
 To emulate the sensor readings without installing real sensors, Client can read sensor data stored in an Excel file and sends to Broker.

 Constraints:
- Client can only send at most 250 bytes in one message.
"""

import time

import paho.mqtt.client as mqtt
from .sensor_reader import SensorReader

MAX_PAYLOAD_SIZE = 250 # bytes
READ_INTERVAL = 3 * 60 # 3 minutes


class MQTTClient():
    def __init__(self, broker_ip, broker_port, node_id, xlsx_file_path, sheet_name):
        self.broker_ip = broker_ip
        self.broker_port = broker_port
        self.node_id = node_id
        self.xlsx_file_path = xlsx_file_path
        self.sheet_name = sheet_name

        self.client = mqtt.Client()
        self.client.connect(self.broker_ip, self.broker_port)
        self.client.enable_logger()
        self.client.on_connect = self.on_connect

        self.client.loop_start()
        self.send_sensor_data(self.node_id, self.sheet_name)
        self.ip = ""
        self.port = 0

    def send_sensor_data(self, node_id, sheet_name):
        stream = SensorReader(self.xlsx_file_path, sheet_name)
        if stream is None:
            print("Invalid stream source.")
            exit()

        # Send sensor data
        for i in range(stream.shape[0]):
            print("Sending data row "+str(i))
            data = stream.get_data_by_row(i)
            data_string = f"{node_id};{data['time']};{data['humidity']};{data['temperature']};{data['thermal_array']}"
            data_size = len(data_string)
            info = f"{node_id};{data_size}"

            # Send info
            self.client.publish(
                "client/log", f"client sending information {data_size} to {self.node_id}/info")
            self.client.publish(f"{self.node_id}/ack", info)

            # Check payload size
            if data_size > MAX_PAYLOAD_SIZE:
                chunks_size = MAX_PAYLOAD_SIZE - \
                    len(node_id) - len(str(data_size)) - 2
                chunks = [data_string[i:i+chunks_size]
                          for i in range(0, data_size, chunks_size)]

                # Send each chunks as a separate payload along with node_id and data_size as prefixes
                self.client.publish(
                    "client/log", f"client {self.node_id} requested {data_size} byte(s)")
                for chunk in chunks:
                    # node id/expected length/data chunk
                    payload = f"{node_id}/{data_size}/{chunk}"
                    self.client.publish(
                        "client/log", f"client {self.node_id} sent {len(payload)} byte(s) in {f'{self.node_id}/data'}")
                    self.client.publish(f'{self.node_id}/data', payload)
                time.sleep(READ_INTERVAL)

            else:
                # Send data in one message
                payload = f"{node_id}/{data_size}/{data_string}"
                self.client.publish(f'{self.node_id}/data', payload)
                time.sleep(READ_INTERVAL)

            self.client.publish(
                "client/log", f"client {self.node_id} sent {f'{self.node_id}/data'}")

        self.disconnect()

    def on_connect(self, client, userdata, flags, rc):
        self.ip = client._sock.getpeername()[0]
        self.port = client._sock.getpeername()[1]
        self.client.publish(
            f'client/log', f'client {self.ip}:{self.port} connected as client {self.node_id}')

    def disconnect(self):
        self.client.publish(
            f'client/log', f'client {self.node_id}, {self.ip}:{self.port} disconnected')
        self.client.disconnect()
        self.client.loop_stop()
