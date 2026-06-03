from publisher import MqttPublisher
from subscriber import MqttSubscriber
from config import MqttConfig
import logging
import time

import publisher
import subscriber
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
config = MqttConfig()


def publish(publisher):
    msg_count = 1
    while msg_count <= 5:
        time.sleep(1)
        msg = f"Hello, MQTT: {msg_count}"
        result = publisher.publish(config.get_mqtt_topic(), msg)
        # result[0] is the status code (0 means success)
        if result and result[0] == 0:
            print(f"Sent `{msg}` to topic `{config.get_mqtt_topic()}`")
        else:
            print(f"Failed to send message to topic {config.get_mqtt_topic()}")
        msg_count += 1



def executePublish(pub_client):
    logger.info("Starting MQTT Publisher...")
    pub_client.loop_start()
    
    # Wait for connection to establish
    time.sleep(1)
    
    publisher = MqttPublisher(pub_client)
    message = publish(publisher)

    logger.info("Publishing messages...")
    
    # Wait for messages to be delivered before stopping loop
    time.sleep(2)
    pub_client.loop_stop()   
    pub_client.disconnect()


    
if __name__ == "__main__":
    # Start subscriber first (non-blocking)
    logger.info("Starting MQTT Subscriber...")
    sub_client = config.connect_subscriber_mqtt()
    subscriber = MqttSubscriber(sub_client, config.get_mqtt_broker(), config.get_mqtt_port(), config.get_mqtt_topic())
    subscriber.subscribe(config.get_mqtt_topic())
    
    # Wait for subscriber to connect
    time.sleep(1)
    
    # Then run publisher
    pub_client = config.connect_publisher_mqtt()
    executePublish(pub_client)
    
    # Keep subscriber running for a bit to receive messages
    time.sleep(3)
    
    # Cleanup
    sub_client.loop_stop()
    sub_client.disconnect()

