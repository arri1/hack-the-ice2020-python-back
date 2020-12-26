import logging
import traceback

from flask_restx import Api

log = logging.getLogger(__name__)

api = Api(version='1.0', title='kek',
          description='kek')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    return {'message': message}, 500
