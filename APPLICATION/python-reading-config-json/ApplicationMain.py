from config.application_config_reader import ApplicationConfigReader
import json



def __main_application_executor():
    print("application execution started")
    application_config_reader: ApplicationConfigReader = ApplicationConfigReader()
    config_data: object = application_config_reader.readConfig()
    print("whole data \n"+json.dumps(config_data, indent=2))
    print("profile data \n"+json.dumps(config_data["profiles"], indent=2))
    print("dev profile data \n"+json.dumps(config_data["profiles"]["dev"], indent=2))
    print("qa profile data \n"+json.dumps(config_data["profiles"]["qa"], indent=2))
    print("prod profile data \n"+json.dumps(config_data["profiles"]["prod"], indent=2))
    print("application execution ended")


if __name__ == '__main__':
    __main_application_executor()