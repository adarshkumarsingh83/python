from config.ConfigurationBean import ConfigurationBean, DataBaseConfig, UserSetting, Users  
from config.ApplicationConfigurations import ApplicationConfigurations  


def main():
        applicationConfigurations = ApplicationConfigurations("resources/application.yml")
        applicationConfigurations.load_configuration()
        configurations: ConfigurationBean = applicationConfigurations.get_configurations()
        print(configurations)
        db:DataBaseConfig = configurations.database
        print(db)
        user_setting:UserSetting = configurations.user_settings
        print(user_setting)
        users:list[Users] = configurations.users
        print(users)
        

if __name__ == "__main__":
    main()