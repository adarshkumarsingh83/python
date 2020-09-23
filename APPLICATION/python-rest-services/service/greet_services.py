from service.base_service import BaseServices, app


class GreetWorld(BaseServices):

    def __init__(self):
        print('GreetWorld constructor ')

    def get(self):
        print('get() execution ')
        return {'messagge': 'welcome to espark'}
