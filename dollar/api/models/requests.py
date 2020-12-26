from flask_restx import reqparse

pagination_arguments = reqparse.RequestParser()
pagination_arguments.add_argument('page', type=int, required=False, default=0, help='Page number')
pagination_arguments.add_argument('per_page', type=int, required=False, choices=[10, 20], default=10,
                                  help='Results per page')
pagination_arguments.add_argument('sort_by', type=str, required=False, default='rating', help='Sort by')
pagination_arguments.add_argument('is_descending', type=bool, required=False, default=True, help='Is descending')