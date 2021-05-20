from logging import log
from flask import Flask
from flask.json import jsonify
import datetime

def create_app():
    app = Flask(__name__)

    @app.route("/", methods=["GET"])
    def index():
        datetimeObj = datetime.datetime.now()
        dataObject = {'Server Time':"{0}".format(str(datetimeObj.time())), 
                      'Server Date':"{0}".format(str(datetimeObj.date()))}
        return jsonify(dataObject)
    # app.config.from_object(config_class)

    from Logger.routes import logger
    from Communication.routes import communication
    app.register_blueprint(logger)
    app.register_blueprint(communication)
    return app


