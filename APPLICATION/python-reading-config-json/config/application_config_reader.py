import json

class ApplicationConfigReader:

    RESOURCE_DIR = './resources/'

    def readConfig(self) -> object:
        with open(ApplicationConfigReader.RESOURCE_DIR+'application_config.json', 'r') as dataInputFile:
            configData = json.load(dataInputFile)
            return configData