from flask_restx import fields
from dollar.api.restx import api

company = api.model('Company', {
    '_id': fields.String(readOnly=True, description='The unique identifier'),
    'modified_on': fields.DateTime(readonly=True),
    'name': fields.String(required=True, description='Company name'),
    'rating': fields.Float(required=True, description='Company rating'),
})

settings = api.model('Company', {
    'smth_k': fields.Float(required=True, description='Coefficient of something'),
})

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
    'is_descending': fields.Boolean(description='Are results descending'),
    'sort_by': fields.String(description='Results sorted by'),
})

page_of_companies = api.inherit('Page of companies', pagination, {
    'items': fields.List(fields.Nested(company))
})
