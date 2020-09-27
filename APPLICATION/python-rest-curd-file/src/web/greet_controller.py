from src.config.application_config import Response, json, app, log


class GreetController:

    def __init__(self):
        log.info('GreetController Constructor ')


@app.route("/")
def get_welcome():
    log.info('GreetController get() execution ')
    return Response(response=json.dumps({'message': 'welcome to espark'}),
                    status=200,
                    mimetype='application/json')
