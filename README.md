# 📡 MQTT-based IoT application

## General Information

### 🎯 Aim, Objective, and Goal

This is a project that aims to design and implement a MQTT-based IoT application that sends sensor readings from an IoT node to a remote database. Our goal is to create  and simulate MQTT-based system which composes of broker, server, and client. We want to be able to run multiple client reading data from given excel and send all those data to multiple server, which have its own database, via broker.

### 📦 Architecture

![Blank_diagram](https://user-images.githubusercontent.com/100426625/222967222-f96c0019-571f-4516-86f9-29885aadbd58.png)

The system consists of three entities - Client (IoT node), Broker, and Server.

The client is responsible for reading the sensor data and publishing it to the broker. The broker acts as a mediator between the client and server. It receives the data from the client and forwards it to the server. The server stores the data in the database.

The client and server communicate with the broker using the MQTT protocol. MQTT is a lightweight publish-subscribe messaging protocol that is widely used in IoT applications.

### 📁 Files Description

The following is a description of the files in this project:

- `broker/__init__.py` - The `__init__.py` file that makes the `broker` directory a Python package.
- `broker/mqtt_broker.py` - The MQTT broker class that handles the MQTT protocol.
- `client/__init__.py` - The `__init__.py` file that makes the `client` directory a Python package.
- `client/mqtt_client.py` - The MQTT client class that handles the MQTT protocol.
- `client/sensor_reader.py` - The sensor reader class that reads the sensor data.
- `logger/__init__.py` - The `__init__.py` file that makes the `logger` directory a Python package.
- `logger/logger.py` - The logger class that handles logging.
- `server/__init__.py` - The `__init__.py` file that makes the `server` directory a Python package.
- `server/database.py` - The database class that handles the database operations.
- `server/mqtt_server.py` - The MQTT server class that handles the MQTT protocol.
- `broker.py` - File to run the broker application with **main**.
- `client.py` - File to run the client application with **main**.
- `server.py` - File to run the server application with **main**.
- `requirements.txt` - The list of required packages to run the application.
- `config.ini` - The configuration file that contains the configuration parameters for the application.

Full description are available in each file.

# 🛠 Getting Started

To get started with this project, you will need to have some prerequisites:

- Python 3.6 or higher installed.
- A basic understanding of MQTT protocol.
- Knowledge of programming languages such as Python and SQL.
- MQTT Broker (such as Mosquitto) installed.

## 📥 Installation

1. Clone the repository

```bash
git clone https://github.com/ibzzsfw/mqtt-project.git
```

2. Install the required packages

```bash
pip install -r requirements.txt
```

## 🚴 Running the application

1. Start the broker

```bash
python broker.py
```

2. Start the server

```bash
python server.py
```

3. Start the client

```bash
python client.py
```
