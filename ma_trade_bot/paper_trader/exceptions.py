class ValidationError(Exception):
    def __init__(self, text, *args):
        super(ValidationError, self).__init__(*args)
        self.text = text
