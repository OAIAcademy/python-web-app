import os
import waitress
from service import flask_app


hostName = "0.0.0.0"
serverPort = int(os.environ.get("PORT", 80))

if __name__ == '__main__':
    waitress.serve(flask_app, port=serverPort, host=hostName)