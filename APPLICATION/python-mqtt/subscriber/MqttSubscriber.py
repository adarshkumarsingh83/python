from config import MqttConfig
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MqttSubscriber:
    
    def __init__(self, mqtt_client, broker, port, topic):
            self.mqtt_client = mqtt_client
            self.BROKER = broker
            self.PORT = port
            self.TOPIC = topic

    def subscribe(self, topic):
        
        def on_connect(client, userdata, connect_flags, reason_code, properties):
            if reason_code == 0:
                logger.info("Subscriber Connected to MQTT broker successfully")
                client.subscribe(self.TOPIC)
            else:
                logger.error(f"Subscriber Failed to connect to MQTT broker: {reason_code}")
        
        def on_message(client, userdata, msg):
            logger.info(f"Subscriber Received message on topic '{msg.topic}': {msg.payload.decode()}")

        def on_disconnect(client, userdata, disconnect_flags, reason_code, properties):
            logger.info(f"Subscriber Disconnected from MQTT broker with code {reason_code}")
        try:
            self.mqtt_client.on_connect = on_connect
            self.mqtt_client.on_message = on_message 
            self.mqtt_client.on_disconnect = on_disconnect
            self.mqtt_client.connect(self.BROKER, self.PORT, keepalive=60)
            self.mqtt_client.loop_start()
            logger.info(f"Subscribed to topic '{topic}'")
        except Exception as e:
            logger.error(f"Failed to subscribe to topic '{topic}': {e}")