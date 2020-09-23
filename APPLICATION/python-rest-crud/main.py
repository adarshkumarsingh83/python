from flask_restful import Api
from web.abstract_controller import app
from web.user_controller import UserController, UserControllerList
from web.greet_controller import GreetController

api = Api(app)
api.add_resource(GreetController, '/')
api.add_resource(UserControllerList, '/users')
api.add_resource(UserController, '/user', endpoint='post')
api.add_resource(UserController, '/user/<id>', endpoint='get')
api.add_resource(UserController, '/user/<id>', endpoint='put')
api.add_resource(UserController, '/user/<id>', endpoint='delete')


def server_starting(name):
    print('Web Server starting ... , {name}')
    app.run(debug=True)


if __name__ == '__main__':
    server_starting('espark adarsh ')
