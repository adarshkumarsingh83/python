from flask_restful import Api
from service.base_service import app
from service.greet_services import GreetWorld
from service.data_services import DataService

api = Api(app)
api.add_resource(GreetWorld, '/')
api.add_resource(DataService, '/data', endpoint='post')
api.add_resource(DataService, '/data/<id>', endpoint='get')
api.add_resource(DataService, '/data/<id>', endpoint='put')
api.add_resource(DataService, '/data/<id>', endpoint='delete')


def server_started(name):
    print(f'Espark Web Services, {name}')
    app.run(debug=True)


if __name__ == '__main__':
    server_started('...starting')
