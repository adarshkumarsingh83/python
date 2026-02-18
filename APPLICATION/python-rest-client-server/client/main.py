import uvicorn
from src.config.ApplicationConfig import ApplicationConfig
from src.config.bean.ConfigBean import ConfigBean

def executeMain() -> None:
    print("Starting application")
    appConfig = ApplicationConfig()
    configBean: ConfigBean = appConfig.getConfigBean()
    print(f"Config Bean: {configBean}")
    
    
    appController = appConfig.getAppController()
    app = appController.getApp()
    uvicorn.run(app, host="127.0.0.1", port=8090)

if __name__ == "__main__":
    executeMain()