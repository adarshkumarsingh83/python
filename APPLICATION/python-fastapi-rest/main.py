import uvicorn
from fastapi import FastAPI
from router.ApplicationRouter import ApplicationRouter

def appExecutor() -> None:
    router = ApplicationRouter()
    app = FastAPI()
    app.router.include_router(prefix="/v",router=router.getRouter())
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    appExecutor()
   