import yaml
import os 
from src.config.bean.ConfigurationBean import AppConfigBean, DbConfigBean, ConfigurationBean

class YamlReader:
    
    def __init__(self, filePath: str):
        print("Initializing YAML reader...")
        self.filePath = filePath
        self.configData = None
        self.appConfig: AppConfigBean = None
        self.dbConfig: DbConfigBean = None
        self.loadYmlConfig()

    def loadYmlConfig(self) -> AppConfigBean:
        print("Loading YAML configuration...")
        with open(os.path.normpath(self.filePath), 'r') as file:
                self.configData = yaml.safe_load(file)
                self.appConfig = AppConfigBean(**self.configData['com']['adarsh']['espark']['application']['appConfig'])
                self.dbConfig = DbConfigBean(**self.configData['com']['adarsh']['espark']['application']['dbConfig'])
            
    def getAppConfig(self) -> AppConfigBean:
        return self.appConfig
    
    def getDbConfig(self) -> DbConfigBean:
        return self.dbConfig
    
    