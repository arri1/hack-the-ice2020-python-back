from flask_restx import reqparse

pagination_arguments = reqparse.RequestParser()
pagination_arguments.add_argument("page", type=int, required=False, default=0, help="Page number")
pagination_arguments.add_argument("per_page", type=int, required=False, choices=[10, 20], default=10,
                                  help="Results per page")
pagination_arguments.add_argument("sort_by", type=str, required=False, default="rate", help="Sort by")
pagination_arguments.add_argument("is_descending", type=int, required=False, default=1,
                                  help="Is descending")  # for some reason bool stopped working
pagination_arguments.add_argument("chosen_chars", type=str, required=False,
                                  default='["verification", "days_online", "own", "median_delivery_time",'
                                          '"mean_product_price","good_orders", "bad_orders","mean_feedback", '
                                          '"mean_call", "mean_cost_delivery","count_products", "median_sale", '
                                          '"sum_views"]',
                                  help="Choosable chars")
