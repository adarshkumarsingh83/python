import uvicorn
from fastapi import FastAPI
from src.config.ApplicationConfig import ApplicationConfig
from src.router.ApplicationRouter import ApplicationRouter
from src.entity.Employee import Employee


def executeWeb():
    print("Starting web application...")
    appConfig = ApplicationConfig()
    print("Application configuration loaded successfully.")
    app = FastAPI()
    app.router.include_router(prefix="/v",router=appConfig.getApplicationRouter().getRouter())
    uvicorn.run(app, host="127.0.0.1", port=8000)
    
    
if __name__ == "__main__":
    executeWeb()