from logging import log
from flask import Flask

def create_app():
    app = Flask(__name__)
    # app.config.from_object(config_class)

    from Logger.routes import logger
    from Communication.routes import communicaiton
    app.register_blueprint(logger)
    app.register_blueprint(communicaiton)
    return app


