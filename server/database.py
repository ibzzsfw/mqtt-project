"""
Schema:
    - id: primary key, uuid
    - nodeId: 4-digit node id
    - time: current time (Date, hours, minutes)
    - humidity: relative humidity readings are between 0 to 100 percent
    - temperature: temperature readings are between 0 to 90 degree celsius
    - thermalArray: 24×32 where each array value represents a temperature reading between 5 to 60 degree celsius
"""

import sqlite3
import uuid


class Database:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS SensorData (id TEXT PRIMARY KEY, nodeId INTEGER, time TEXT, humidity REAL, temperature REAL, thermalArray TEXT)")
        self.conn.commit()

    def insert_data(self, node_id: int, time: str, humidity: float, temperature: float, thermal_array: str):
        self.cursor.execute(
            "INSERT INTO SensorData VALUES (?, ?, ?, ?, ?, ?)", (str(uuid.uuid4()), node_id, time, humidity, temperature, thermal_array))
        self.conn.commit()

    def get_all_data(self):
        try:
            self.cursor.execute("SELECT * FROM SensorData")
            return self.cursor.fetchall()
        except Exception as e:
            return [e]

    def get_data_by_node_id(self, node_id: int):
        try:
            self.cursor.execute(
                f"SELECT * FROM SensorData WHERE nodeId = {node_id}")
            return self.cursor.fetchall()
        except Exception as e:
            return [e]

    def get_data_by_sensor(self, sensor: str):
        try:
            self.cursor.execute(
                f"SELECT nodeId, time, {sensor} FROM SensorData")
            return self.cursor.fetchall()
        except Exception as e:
            return [e]

    def delete_all_data(self):
        self.cursor.execute("DELETE FROM SensorData")
        self.conn.commit()

    def raw_query(self, query: str):
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            return [e]

    def close(self):
        self.conn.close()
