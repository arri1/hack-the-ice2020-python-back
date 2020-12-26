import logging.config

import os
from flask import Flask, Blueprint
from dollar.api.endpoints.companies import ns as companies_namespace
from dollar.api.endpoints.settings import ns as settings_namespace
from dollar.api.restx import api

app = Flask(__name__)
app.config.SWAGGER_UI_DOC_EXPANSION = 'list'
logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '../logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)

blueprint = Blueprint('api', __name__, url_prefix='/api')
api.init_app(blueprint)
api.add_namespace(companies_namespace)
api.add_namespace(settings_namespace)
app.register_blueprint(blueprint)
