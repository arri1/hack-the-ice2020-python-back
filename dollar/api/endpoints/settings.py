import logging

from flask import request
from flask_restx import Resource
from dollar.api.models.responses import settings as settings_model

from dollar.api.restx import api

from dollar.db.settings_table import get_settings, update_settings
from dollar.fetcher import request_fetch_now

log = logging.getLogger(__name__)
ns = api.namespace('settings', description='Settings endpoints')


@ns.route('/')
class SettingsCollection(Resource):
    @api.marshal_with(settings_model)
    def get(self):
        """
        Returns Settings.
        """
        return get_settings()

    @api.expect(settings_model)
    @api.marshal_with(settings_model)
    @api.response(200, 'Settings successfully updated.')
    def put(self):
        data = request.json
        res = update_settings(data)
        request_fetch_now()
        return res