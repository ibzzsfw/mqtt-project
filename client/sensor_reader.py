"""
- The relative humidity readings are between 0 to 100 percent,
- the temperature readings are between 0 to 90 degree celsius,
- the thermal array readings are 24×32 where each array value represents a temperature reading between 5 to 60 degree celsius.
"""
import os

import pandas as pd

# Minimum and maximum values for sensor readings
HUMIDITY_MIN = 0
HUMIDITY_MAX = 100
TEMPERATURE_MIN = 0
TEMPERATURE_MAX = 90
THERMAL_ARRAY_MIN = 5
THERMAL_ARRAY_MAX = 60
THERMAL_ARRAY_ROW = 24
THERMAL_ARRAY_COLUMN = 32


class SensorReader:
    def __init__(self, file_path, sheet_name):
        """
        Function: init
        Description: init SensorReader class
        Parameters:
            file_path: excel file path
            sheet_name: excel sheet name, specify the node
        Returns: None
        """
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.data = self.read_excel_file()
        self.shape = self.data.shape

    def read_excel_file(self):
        """
        Function: read_excel_file
        Description: read excel file if it exists, otherwise return None
        Parameters: 
            None
        Returns:
            data: excel data or None, depends on the possibility of reading the file
        """
        try:
            data = pd.read_excel(self.file_path, sheet_name=self.sheet_name)
            return data
        except Exception as e:
            print(e)
            return None

    def get_data_by_row(self, row):
        """
        Function: get_data_by_row
        Description: get data by row index with data verification
        Parameters:
            row: row index
        Returns:
            data: data in the row in dictionary format
        """
        if row > len(self.data):
            raise Exception('Row index out of range')
        # verify data
        time = self.data.iloc[row]['Time']
        humidity = self.data.iloc[row]['Humidity']
        temperature = self.data.iloc[row]['Temperature']
        thermal_array = self.data.iloc[row]['ThermalArray']
        # convert thermal array to double array
        thermal_array = thermal_array.split(',')
        thermal_array = [float(i) for i in thermal_array]
        # check humidity, temperature, thermal array value
        if humidity < HUMIDITY_MIN or humidity > HUMIDITY_MAX:
            # assign to missing na
            humidity = pd.NA

        if temperature < TEMPERATURE_MIN or temperature > TEMPERATURE_MAX:
            temperature = pd.NA

        # check thermal array value
        for i in range(len(thermal_array)):
            if thermal_array[i] < THERMAL_ARRAY_MIN or thermal_array[i] > THERMAL_ARRAY_MAX:
                thermal_array[i] = pd.NA

        # check thermal array dimension
        if len(thermal_array) != THERMAL_ARRAY_ROW * THERMAL_ARRAY_COLUMN:
            # append missing na
            thermal_array = thermal_array + \
                [pd.NA] * (THERMAL_ARRAY_ROW *
                           THERMAL_ARRAY_COLUMN - len(thermal_array))

        return {
            'time': time,
            'humidity': humidity,
            'temperature': temperature,
            'thermal_array': thermal_array
        }
