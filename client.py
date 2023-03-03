"""
 MQTT Client has three types of sensors 
 
 – Relative humidity, temperature, and thermal array. 
    - The relative humidity readings are between 0 to 100 percent, 
    - the temperature readings are between 0 to 90 degree celsius, 
    - the thermal array readings are 24×32 where each array value represents a temperature reading between 5 to 60 degree celsius. 
 
 - Client simultaneously reads all the sensors every 3 minutes 
 - and wants to send the sensor data to Broker together with 4-digit node id and current time (Date, hours, minutes). 
 
 To emulate the sensor readings without installing real sensors, Client can read sensor data stored in an Excel file and sends to Broker.

 Constraints:
- Client can only send at most 250 bytes in one message.
"""

# Import client packages
from client import MqttClient
from client import ExcelReader

reader = ExcelReader('input.xlsx')
reader.readExcel('node1', 'Time')
reader.printDataframe()