from . import routes


@routes.route('/')
def index():
    return "{'data':'Hello World!'}"
