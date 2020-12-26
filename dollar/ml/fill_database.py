from dollar.db.companies_table import update_companies_collection
from dollar.ml.set_functions import main_set, price_set, sale_set
from dollar.ml.rate_functions import make_rate
import pandas as pd

from dollar.db.settings_table import get_settings

company_columns = ['verification',
                   'days_online',
                   'own',
                   'median_delivery_time',
                   'mean_product_price',
                   'good_orders',
                   'bad_orders',
                   'mean_feedback',
                   'mean_call',
                   'mean_cost_delivery',
                   'count_products',
                   'median_sale',
                   'sum_views',
                   'part_good_order',
                   'part_orders_of_online',
                   'part_orders_of_views',
                   'rate']
price_columns = ['mean_product_price', 'median_product_price',
                 'max_product_price', 'min_product_price']
sale_columns = ['mean_sale', 'median_sale', 'max_sale', 'min_sale']


def company_response(companies):
    d = {}
    for _id in companies['id']:
        line_d = {}
        line = companies[companies['id'] == _id]
        for column in company_columns:
            line_d[column] = list(line[column])[0]

        d[list(line['company'])[0]] = line_d
    return d


def price_response(companies):
    d = {}
    for _id in companies['id']:
        line_d = {}
        line = companies[companies['id'] == _id]
        for column in price_columns:
            line_d[column] = list(line[column])[0]

        d[list(line['company'])[0]] = line_d
    return d


def sale_response(companies):
    d = {}
    for _id in companies['id']:
        line_d = {}
        line = companies[companies['id'] == _id]
        for column in sale_columns:
            line_d[column] = list(line[column])[0]

        d[list(line['company'])[0]] = line_d
    return d


def fill_database(companies, orders, products):
    categories_by_company_id = {}
    companies_by_category = {}
    for company in companies:
        category = company['category']
        categories_by_company_id[company['id']] = category
        if category not in companies_by_category:
            companies_by_category[category] = []
        companies_by_category[category].append(company)

    df_orders = pd.DataFrame(orders)
    df_products = pd.DataFrame(products)
    result_ar = []
    for category in companies_by_category:
        res = calculate_for_category(companies_by_category[category], df_orders, df_products)
        result_ar += res.T.to_dict().values()
    update_companies_collection(result_ar)

def calculate_for_category(companies, df_orders, df_products):
    df_companies = pd.DataFrame(companies)

    dict_coef = get_settings()

    df_companies = main_set(df_companies, df_orders, df_products)
    df_companies = price_set(df_companies, df_orders, df_products)
    df_companies = sale_set(df_companies, df_orders, df_products)

    df_companies['rate'] = make_rate(df_companies, dict_coef)

    return df_companies
