from flask_restx import fields
from dollar.api.restx import api

company = api.model('Company', {
    'id': fields.Integer(readOnly=True, description='The unique identifier'),
    'company': fields.String(readOnly=True, description='Company name'),
    'category': fields.Integer(readOnly=True),
    'verification': fields.Integer(readOnly=True),
    'own': fields.Integer(readOnly=True),
    'days_online': fields.Integer(readOnly=True),
    'median_delivery_time': fields.Float(readOnly=True),
    'mean_product_price': fields.Float(readOnly=True),
    'part_good_order': fields.Float(readOnly=True),
    'good_orders': fields.Integer(readOnly=True),
    'bad_orders': fields.Integer(readOnly=True),
    'mean_feedback': fields.Float(readOnly=True),
    'mean_call': fields.Float(readOnly=True),
    'mean_cost_delivery': fields.Float(readOnly=True),
    'count_products': fields.Integer(readOnly=True),
    'median_sale': fields.Float(readOnly=True),
    'sum_views': fields.Integer(readOnly=True),
    'part_orders_of_online': fields.Float(readOnly=True),
    'part_orders_of_views': fields.Float(readOnly=True),
    'median_product_price': fields.Float(readOnly=True),
    'max_product_price': fields.Float(readOnly=True),
    'min_product_price': fields.Float(readOnly=True),
    'max_sale': fields.Float(readOnly=True),
    'min_sale': fields.Float(readOnly=True),
    'mean_sale': fields.Float(readOnly=True),
    'rate': fields.Float(readOnly=True),
})

settings = api.model('Settings', {
    'verification': fields.Float(required=True, description='Coefficient of something'),
    'part_orders_of_online': fields.Float(required=True, description='Coefficient of something'),
    'own': fields.Float(required=True, description='Coefficient of something'),
    'median_delivery_time': fields.Float(required=True, description='Coefficient of something'),
    'mean_product_price': fields.Float(required=True, description='Coefficient of something'),
    'part_good_order': fields.Float(required=True, description='Coefficient of something'),
    'mean_feedback': fields.Float(required=True, description='Coefficient of something'),
    'mean_call': fields.Float(required=True, description='Coefficient of something'),
    'mean_cost_delivery': fields.Float(required=True, description='Coefficient of something'),
    'count_products': fields.Float(required=True, description='Coefficient of something'),
    'median_sale': fields.Float(required=True, description='Coefficient of something'),
    'part_orders_of_views': fields.Float(required=True, description='Coefficient of something'),
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
