from flask import Flask
from routes import *

app = Flask(__name__)
app.register_blueprint(routes)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run()