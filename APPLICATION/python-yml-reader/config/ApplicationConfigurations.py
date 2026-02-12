import yaml
from dataclasses import dataclass
from config.ConfigurationBean import ConfigurationBean ,DataBaseConfig, UserSetting, Users  

class ApplicationConfigurations:
    
    def __init__(self, config_file_path: str):
        self.config_file_path = config_file_path
        self.configurations = None

    def load_configuration(self) -> None:
        with open(self.config_file_path, 'r') as file:
            configs = yaml.safe_load(file)
        
        database_config = DataBaseConfig(**configs['com']['espark']['adarsh']['database'])
        user_settings = UserSetting(**configs['com']['espark']['adarsh']['user_setting'])
        users = [Users(**user) for user in configs['com']['espark']['adarsh']['users']]
    
        self.configurations = ConfigurationBean(
            database=database_config,       
            user_settings=user_settings,
            users=users
        )
        
    def get_configurations(self) -> ConfigurationBean:
        if self.configurations is None:
            raise ValueError("Configurations have not been loaded. Please call load_configuration() first.")
        return self.configurations