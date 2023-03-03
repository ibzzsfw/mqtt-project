import sqlite3

"""
Schema:
    - id: primary key
    - node_id: 4-digit node id
    - time: current time (Date, hours, minutes)
    - humidity: relative humidity readings are between 0 to 100 percent
    - temperature: temperature readings are between 0 to 90 degree celsius
    - thermal_array: 24×32 where each array value represents a temperature reading between 5 to 60 degree celsius
"""

import sqlite3

class Database:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS sensor_data (id INTEGER PRIMARY KEY AUTOINCREMENT, node_id INTEGER, time TEXT, humidity REAL, temperature REAL, thermal_array TEXT)")
        self.conn.commit()

    def insert_data(self, node_id: int, time: str, humidity: float, temperature: float, thermal_array: str):
        self.cursor.execute(
            "INSERT INTO sensor_data (node_id, time, humidity, temperature, thermal_array) VALUES (?, ?, ?, ?, ?)", (node_id, time, humidity, temperature, thermal_array))
        self.conn.commit()

    def get_all_data(self):
        self.cursor.execute("SELECT * FROM sensor_data")
        return self.cursor.fetchall()

    def get_data_by_id(self, id: int):
        self.cursor.execute(
            "SELECT * FROM sensor_data WHERE id = ?", (id,))
        return self.cursor.fetchone()

    def get_data_by_node_id(self, node_id: int):
        self.cursor.execute(
            "SELECT * FROM sensor_data WHERE node_id = ?", (node_id,))
        return self.cursor.fetchall()

    def get_data_by_time(self, time: str):
        self.cursor.execute(
            "SELECT * FROM sensor_data WHERE time = ?", (time,))
        return self.cursor.fetchall()

    def get_data_by_humidity(self, humidity: float):
        self.cursor.execute(
            "SELECT * FROM sensor_data WHERE humidity = ?", (humidity,))
        return self.cursor.fetchall()

    def get_data_by_temperature(self, temperature: float):
        self.cursor.execute(
            "SELECT * FROM sensor_data WHERE temperature = ?", (temperature,))
        return self.cursor.fetchall()

    def get_data_by_thermal_array(self, thermal_array: str):
        self.cursor.execute(
            "SELECT * FROM sensor_data WHERE thermal_array = ?", (thermal_array,))
        return self.cursor.fetchall()

    def update_data_by_id(self, id: int, node_id: int, time: str, humidity: float, temperature: float, thermal_array: str):
        self.cursor.execute(
            "UPDATE sensor_data SET node_id = ?, time = ?, humidity = ?, temperature = ?, thermal_array = ? WHERE id = ?",
            (node_id, time, humidity, temperature, thermal_array, id))
        self.conn.commit()

    def delete_data_by_id(self, id: int):
        self.cursor.execute(
            "DELETE FROM sensor_data WHERE id = ?", (id,))
        self.conn.commit()

    def delete_all_data(self):
        self.cursor.execute("DELETE FROM sensor_data")
        self.conn.commit()

    def close(self):
        self.conn.close()
