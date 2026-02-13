
import os 
from src.config.bean.ConfigurationBean import AppConfigBean, DbConfigBean
from src.config.PropertiesReader import PropertiesReader    
from src.config.YamlReader import YamlReader
from src.config.persistance.DbConection import DbConnection
from src.config.persistance.initializedDb import InitializedDb
from src.respository.EmployeeRepository import EmployeeRepository

class ApplicationConfig:
    def __init__(self):
        print("Initializing application configuration...")
        currentDir = os.path.dirname(os.path.abspath(__file__))
        self.resourceDir = os.path.normpath(os.path.join(currentDir, "..", "..", "resources"))
        self.ymlReader: YamlReader = None
        self.propertiesReader: PropertiesReader = None
        self.dbConfig: DbConfigBean = None
        self.apiConfig: AppConfigBean = None
        self.loadConfig()
        self.loadDbConfig()

    def loadConfig(self)-> None:
        print("Loading application configuration...")
        ymlFilePath = os.path.join(self.resourceDir, "application.yml")
        print(f"Looking for application.yml at: {ymlFilePath}")
        if not ymlFilePath or not os.path.exists(ymlFilePath):
            print(f"Error: {ymlFilePath} file not found in resources directory.")
            raise FileNotFoundError("application.yml file not found in resources directory.")
        self.ymlReader = YamlReader(ymlFilePath)
        self.dbConfig: DbConfigBean = self.ymlReader.getDbConfig()
        self.apiConfig: AppConfigBean = self.ymlReader.getAppConfig()
        propertiesFilePath = os.path.join(self.resourceDir, "application.properties")
        print(f"Looking for application.properties at: {propertiesFilePath}")
        if not propertiesFilePath or not os.path.exists(propertiesFilePath):
            print(f"Error: {propertiesFilePath} file not found in resources directory.")
            raise FileNotFoundError("application.properties file not found in resources directory.")
        self.propertiesReader = PropertiesReader(propertiesFilePath)
        
    def loadDbConfig(self) -> None:
        print("Loading database configuration...")
        sqlScriptPath = os.path.join(self.resourceDir, self.dbConfig.dbScript)
        if not sqlScriptPath or not os.path.exists(sqlScriptPath):
            raise FileNotFoundError(f"SQL script file {sqlScriptPath} not found in resources directory.")    
        dbConnection = DbConnection(os.path.join(self.resourceDir, self.dbConfig.dbPath))
        InitializedDb(dbConnection, sqlScriptPath)  
        
    def getDbConnection(self) -> DbConnection:
        return DbConnection(os.path.join(self.resourceDir, self.dbConfig.dbPath))
    
    def getEmployeeRepository(self) -> EmployeeRepository:
        dbConnection = self.getDbConnection()
        return EmployeeRepository(dbConnection)
    
    def getAppConfig(self) -> AppConfigBean:
        return self.apiConfig
    
    def getProperties(self) -> dict:
        return self.propertiesReader.getAllProperties()
    
    
        
        
        