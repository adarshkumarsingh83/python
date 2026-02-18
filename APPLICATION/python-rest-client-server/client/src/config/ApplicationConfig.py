import os
from src.config.YmlReader import YmlReader
from src.config.bean.ConfigBean import ConfigBean, ApiConfigBean
from src.service.EmployeeService import EmployeeService
from src.web.ApplicationController import ApplicationController

class ApplicationConfig:
    
    def __init__(self, ):
        print("Initializing ApplicationConfig")
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.resource_dir = os.path.normpath(os.path.join(current_dir, '..','..', 'resources'))
        self.apiConfigStore = None
        self.configBean:ConfigBean = None
        self.apiConfigBeans:ApiConfigBean = None
        self.ymlReader: YmlReader = None
        self.integrationService = None
        self.employeeService: EmployeeService = None
        self.appController: ApplicationController = None
        self.loadConfig()
        
    def loadConfig(self) -> None:
        print("Loading application configuration")
        yml_path = os.path.join(self.resource_dir, 'application.yml')
        print(f"YML file path: {yml_path}")
        if not yml_path or not os.path.exists(yml_path):
            print(f"YML file not found at: {yml_path}")
            raise FileNotFoundError(f"YML file not found at: {yml_path}")
        self.ymlReader = YmlReader(yml_path)
        self.configBean = self.ymlReader.getConfigBean()
        self.apiConfigBeans = self.ymlReader.getAppConfigBean()
        self.apiConfigStore = {api.name: api for api in self.apiConfigBeans} 
        from src.service.IntegrationService import IntegrationService
        self.integrationService = IntegrationService(self.apiConfigStore)
        self.employeeService = EmployeeService(self.integrationService)
        self.appController = ApplicationController(self.employeeService)
        
    def getConfigBean(self) -> ConfigBean:
        return self.configBean
    
    def getConfigByName(self, name: str) -> ApiConfigBean:
        return self.apiConfigStore.get(name)
        
    def getAppController(self) -> ApplicationController:
        return self.appController
    
    def getEmployeeService(self) -> EmployeeService:
        return self.employeeService
