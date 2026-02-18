import os
import yaml
from src.config.bean.ConfigBean import ConfigBean, ApiConfigBean

class YmlReader:
    def __init__(self, path: str):
        print(f"YmlReader initialized with path: {path}")
        self.filePaath = path
        self.configData = None
        self.appConfigBean : list[ApiConfigBean] = None
        self.configBean : ConfigBean = None
        self.loadConfig()
        
    def loadConfig(self) -> None:
        print(f"Loading config from: {self.filePaath}")
        if not os.path.exists(self.filePaath):
            print(f"Config file not found at: {self.filePaath}")
            return
        try:
            with open(os.path.normpath(self.filePaath), 'r',encoding='utf-8') as file:
                self.configData = yaml.safe_load(file)
                print(f"Config data loaded: {self.configData}")
                self.configBean  = ConfigBean(apis=[ApiConfigBean(**api) for api in self.configData.get('apis', [])])
        except Exception as e:
            print(f"Error loading config: {e}")
            
    def getConfigBean(self) -> ConfigBean:
        return self.configBean
    
    def getAppConfigBean(self) -> list[ApiConfigBean]:
        return self.configBean.apis if self.configBean else None    
    