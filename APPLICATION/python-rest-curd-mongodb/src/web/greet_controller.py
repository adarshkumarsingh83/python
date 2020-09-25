from src.web.abstract_controller import AbstractController, app, log


class GreetController(AbstractController):

    def __init__(self):
        log.info('GreetController Constructor ')


@app.route("/")
def get_welcome():
    log.info('GreetController get() execution ')
    return {'message': 'welcome to espark'}
