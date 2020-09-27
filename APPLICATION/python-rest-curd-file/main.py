from flask_restful import Api
from src.config.application_config import AppConfig, app, log
from src.web.greet_controller import GreetController
from src.web.user_controller import UserController

api = Api(app)


def server_starting(msg):
    log.info('Web Server starting ... , {msg}')
    UserController()
    GreetController()
    app.run(debug=True, port=5000, host='0.0.0.0')


if __name__ == '__main__':
    server_starting('espark adarsh ')
