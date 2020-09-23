from service.greet_services import app_greet
from service.data_services import app_data


def server_started(name):
    print(f'Espark Web Services, {name}')
    app_data.run()
    app_greet.run()


if __name__ == '__main__':
    server_started('...starting')

