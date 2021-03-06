from dollar.db.companies_table import update_companies_collection, get_companies_collection
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


choosable_chars = ['verification', 'days_online', 'own', 'median_delivery_time',
                   'mean_product_price',
                   'good_orders', 'bad_orders',
                   'mean_feedback', 'mean_call', 'mean_cost_delivery',
                   'count_products', 'median_sale', 'sum_views']


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
        res = calculate_for_category(companies_by_category[category], df_orders, df_products, choosable_chars)
        result_ar += res.T.to_dict().values()
    for c in result_ar:
        c['orders'] = list(df_orders[df_orders['id_company'] == c['id']].T.to_dict().values())
        c['products'] = list(df_products[df_products['id_company'] == c['id']].T.to_dict().values())
    update_companies_collection(result_ar)


def set_rates_by_db(companies, category, chosen_chars):
    dict_coef = get_settings()
    df_companies = pd.DataFrame(get_companies_collection(category))
    df_companies['rate'] = make_rate(df_companies, dict_coef, chosen_chars)
    for company in companies:
        company['rate'] = float(df_companies[df_companies['id'] == company['id']]['rate'])


def calculate_for_category(companies, df_orders, df_products, chosen_chars):
    df_companies = pd.DataFrame(companies)

    dict_coef = get_settings()

    df_companies = main_set(df_companies, df_orders, df_products)
    df_companies = price_set(df_companies, df_orders, df_products)
    df_companies = sale_set(df_companies, df_orders, df_products)

    df_companies['rate'] = make_rate(df_companies, dict_coef, chosen_chars)

    return df_companies
