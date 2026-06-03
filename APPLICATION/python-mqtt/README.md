
# Python MQTT Application

A Python-based MQTT publisher and subscriber application using the Paho MQTT client library.

## Prerequisites

- Python 3.x
- Mosquitto MQTT broker (or any MQTT broker)

## Installation

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Install and Configure Mosquitto (macOS)

Install Mosquitto using Homebrew:

```bash
brew install mosquitto
```

### 3. Configure Mosquitto

Edit the Mosquitto configuration file:

```bash
nano /opt/homebrew/etc/mosquitto/mosquitto.conf
```

Add the following configuration:

```
listener 1883
allow_anonymous true
```

### 4. Start Mosquitto

Option 1: Start as a background service:

```bash
brew services start mosquitto
```

Option 2: Run manually:

```bash
/opt/homebrew/opt/mosquitto/sbin/mosquitto -c /opt/homebrew/etc/mosquitto/mosquitto.conf
```

## Usage

### Run the Application

```bash
python main.py
```

This will start the subscriber first, then publish test messages.

### Manual MQTT Commands

Subscribe to a topic:

```bash
mosquitto_sub -h localhost -t "my/topic"
```

Publish a message:

```bash
mosquitto_pub -h localhost -t "my/topic" -m "Your message here"
```

## Project Structure

```
python-mqtt/
├── main.py                 # Main entry point
├── requirements.txt        # Python dependencies
├── config/
│   ├── __init__.py
│   └── MqttConfig.py       # MQTT configuration
├── publisher/
│   ├── __init__.py
│   └── MqttPublisher.py    # Publisher implementation
└── subscriber/
    ├── __init__.py
    └── MqttSubscriber.py   # Subscriber implementation
```


* work log 
```
pip install -r requirements.txt


brew install mosquitto
-------------------------------
mosquitto has been installed with a default configuration file.
You can make changes to the configuration by editing:
    /opt/homebrew/etc/mosquitto/mosquitto.conf

To start mosquitto now and restart at login:
  brew services start mosquitto
Or, if you don't want/need a background service you can just run:
  /opt/homebrew/opt/mosquitto/sbin/mosquitto -c /opt/homebrew/etc/mosquitto/mosquitto.conf

 ----------------------------   
nano /opt/homebrew/etc/mosquitto/mosquitto.conf
...................
listener 1883
allow_anonymous true
..................

brew services start mosquitto

mosquitto_sub -h localhost -t "my/topic" 

mosquitto_pub -h localhost -t "my/topic" -m "Your message here"

```