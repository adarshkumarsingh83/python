import configparser
import os 

class PropertiesReader:
    def __init__(self, filePath: str):
        print("Initializing properties reader...")
        self.filePath = filePath
        self.configData = None
        self.properties = {}
        self.loadPropertiesConfig()

    def loadPropertiesConfig(self):
        print("Loading properties configuration...")
        self.configData = configparser.ConfigParser()
        self.configData.read(os.path.normpath(self.filePath))
        for section in self.configData.sections():
            for key, value in self.configData.items(section):
                self.properties[f"{section}.{key}"] = value
                
    def getProperty(self, key: str) -> str:
        return self.properties.get(key, None)
    
    def getAllProperties(self) -> dict:
        return self.properties
        