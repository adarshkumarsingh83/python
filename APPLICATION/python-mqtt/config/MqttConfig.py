from paho.mqtt import client as mqtt_client
import logging

logger = logging.getLogger(__name__)

class MqttConfig:

    # Define configuration parameters
    BROKER = 'localhost'
    PORT = 1883
    TOPIC = "my/topic"
    PUBLISHER_CLIENT_ID = "python-mqtt-publisher-123"
    SUBSCRIBER_CLIENT_ID = "python-mqtt-subscriber-123"

    def connect_publisher_mqtt(self):
        # Use CallbackAPIVersion.VERSION2 for paho-mqtt 2.0+
        client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION2, client_id=self.PUBLISHER_CLIENT_ID)
        
        def on_connect(client, userdata, connect_flags, reason_code, properties):
            if reason_code == 0:
                logger.info("Connected to MQTT broker successfully")
            else:
                logger.error(f"Failed to connect to MQTT broker: {reason_code}")
        
        def on_disconnect(client, userdata, disconnect_flags, reason_code, properties):
            logger.info(f"Disconnected from MQTT broker with code {reason_code}")
        
        client.on_connect = on_connect
        client.on_disconnect = on_disconnect
        client.connect(self.BROKER, self.PORT, keepalive=60)
        return client
    
    def connect_subscriber_mqtt(self):
        # Use CallbackAPIVersion.VERSION2 for paho-mqtt 2.0+
        client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION2, client_id=self.SUBSCRIBER_CLIENT_ID)
        return client
    
    def get_mqtt_port(self):
        return self.PORT
    
    def get_mqtt_topic(self):
        return self.TOPIC
    
    def get_mqtt_broker(self):
        return self.BROKER

    def get_mqtt_publisher_client_id(self):
        return self.PUBLISHER_CLIENT_ID
    
    def get_mqtt_subscriber_client_id(self):
        return self.SUBSCRIBER_CLIENT_ID
    
    def get_mqtt_subscribe_client(self):
        return self.connect_subscriber_mqtt()