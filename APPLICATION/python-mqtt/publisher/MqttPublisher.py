from config import MqttConfig
import logging

logger = logging.getLogger(__name__)

class MqttPublisher:
    def __init__(self, mqtt_client):
        self.mqtt_client = mqtt_client

    def publish(self, topic, payload):
        try:
        
            result = self.mqtt_client.publish(topic, payload, qos=1, retain=True)
            if result[0] == 0:
                logger.info(f"Publisher Published message to topic '{topic}': {payload}")
            else:
                logger.error(f"Publisher Failed to publish message to topic '{topic}': {payload}")
            return result
        except Exception as e:
            logger.error(f"Publisher Failed to publish message to topic '{topic}': {e}")
            return None