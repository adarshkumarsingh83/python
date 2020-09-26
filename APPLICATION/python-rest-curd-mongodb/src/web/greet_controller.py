from src.web.abstract_controller import AbstractController, Response, json, app, log


class GreetController(AbstractController):

    def __init__(self):
        log.info('GreetController Constructor ')


@app.route("/")
def get_welcome():
    log.info('GreetController get() execution ')
    return Response(response=json.dumps({'message': 'welcome to espark'}),
                    status=200,
                    mimetype='application/json')
