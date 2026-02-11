from dataclasses import dataclass
from typing import List, Optional

@dataclass
class DataBaseConfig:
    driverClassName:str
    url:str
    username:str
    password:str
    
@dataclass
class UserSetting:
    username: str
    password: str
    name_list: List[str]
    contacts: Optional[List[str]] = None
    
@dataclass
class Users:
    name: str
    email: str
    
@dataclass
class ConfigurationBean:
    database: DataBaseConfig
    user_settings: UserSetting
    users: List[Users]
    