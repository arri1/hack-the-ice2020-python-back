import logging

from flask import request
from flask_restx import Resource
from dollar.api.models.requests import pagination_arguments
from dollar.api.models.responses import page_of_companies
from dollar.api.restx import api
from dollar.db.companies_table import get_companies_count_and_page, get_companies_count_and_page_by_category

log = logging.getLogger(__name__)
ns = api.namespace('companies', description='Companies endpoints')


@ns.route('/')
class CompaniesCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_companies)
    def get(self):
        """
        Returns list of companies.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 0)
        per_page = args.get('per_page')
        sort_by = args.get('sort_by', 'rate')
        is_descending = args.get('is_descending', 1)
        total, items = get_companies_count_and_page(page, per_page, sort_by, is_descending)
        result = {
            'page': page,
            'per_page': per_page,
            'total': total,
            'is_descending': is_descending,
            'sort_by': sort_by,
            'items': items
        }
        return result


@ns.route('/category/<int:category_id>')
class CompaniesByCategoryCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_companies)
    def get(self, category_id: int):
        """
        Returns list of companies.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 0)
        per_page = args.get('per_page')
        sort_by = args.get('sort_by', 'rate')
        is_descending = args.get('is_descending', 1)
        total, items = get_companies_count_and_page_by_category(page, per_page, sort_by, is_descending, category_id)
        result = {
            'page': page,
            'per_page': per_page,
            'total': total,
            'is_descending': is_descending,
            'sort_by': sort_by,
            'items': items
        }
        return result
