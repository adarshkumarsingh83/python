class ValidationError(Exception):

    def __init__(self, message):
        self.message = message

    def get_message(self):
        return self.message
