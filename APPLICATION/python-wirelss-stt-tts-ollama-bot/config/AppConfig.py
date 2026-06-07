from vosk import Model
import os
import logging 

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AppConfig:
    def __init__(self):
        self.model_path = "model/vosk-model-en-us-0.22"

    def load_vosk_model(self):
        logger.info("Loading Vosk model...")
        if not os.path.exists(self.model_path):
            logger.error("Vosk model not found! Download and place it in the 'models' directory.")
            raise FileNotFoundError("Vosk model not found! Download and place it in the 'models' directory.")
        return Model(self.model_path)