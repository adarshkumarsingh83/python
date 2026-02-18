from dataclasses import dataclass
from typing import List, Optional


@dataclass
class ApiConfigBean:
    name: Optional[str] = None
    baseUrl: Optional[str] = None
    url: Optional[str] = None
    httpMethod: Optional[str] = None
    

@dataclass
class ConfigBean:
    apis: Optional[List[ApiConfigBean]] = None