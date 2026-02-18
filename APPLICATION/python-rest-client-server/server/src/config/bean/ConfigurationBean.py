from dataclasses import dataclass
from typing import Optional


@dataclass
class AppConfigBean:
    appName: Optional[str] = None

@dataclass
class DbConfigBean:
    dbPath: Optional[str] = None
    dbScript: Optional[str] = None

@dataclass
class ConfigurationBean:
    appConfig: Optional[AppConfigBean] = None
    dbConfig: Optional[DbConfigBean] = None