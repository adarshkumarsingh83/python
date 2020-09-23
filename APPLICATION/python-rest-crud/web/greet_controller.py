from web.abstract_controller import AbstractController


class GreetController(AbstractController):

    def __init__(self):
        print('GreetController Constructor ')

    def get(self):
        print('get() execution ')
        return {'messagge': 'welcome to espark'}