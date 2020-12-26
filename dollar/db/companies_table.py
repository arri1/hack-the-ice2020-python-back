from dollar.db import db
import pymongo

choosable_chars = ['verification', 'days_online', 'own', 'median_delivery_time',
                   'mean_product_price',
                   'good_orders', 'bad_orders',
                   'mean_feedback', 'mean_call', 'mean_cost_delivery',
                   'count_products', 'median_sale', 'sum_views']

companies_db = db['companies']


def get_companies_count_and_page(page, per_page, sort_by, is_descending):
    total = companies_db.count_documents({})
    items = list(
        companies_db.find({}, {'products': 0, 'orders': 0}).sort(sort_by, direction=(
            pymongo.DESCENDING if is_descending else pymongo.ASCENDING)).skip(
            page * per_page).limit(per_page))
    return total, items


def get_companies_count_and_page_by_category(page, per_page, sort_by, is_descending, category,
                                             chosen_chars=None):
    from dollar.ml.fill_database import set_rates_by_db
    if chosen_chars is None:
        chosen_chars = choosable_chars
    total = companies_db.count_documents({'category': category})
    if sort_by != 'rate':
        items = list(
            companies_db.find({'category': category}, {'products': 0, 'orders': 0}).sort(sort_by, direction=(
                pymongo.DESCENDING if is_descending else pymongo.ASCENDING)).skip(
                page * per_page).limit(per_page))
        set_rates_by_db(items, category, chosen_chars)
        return total, items

    items = list(companies_db.find({'category': category}, {'products': 0, 'orders': 0}))
    set_rates_by_db(items, category, chosen_chars)
    items.sort(key=lambda x: x['rate'], reverse=is_descending)
    items = items[page * per_page:(page + 1) * per_page]  # FIXME
    return total, items


def get_company_by_id(_id):
    return dict(companies_db.find_one({'id': _id}))


def get_companies_collection(category):
    return list(companies_db.find({'category': category}))


def update_companies_collection(companies):
    companies_db.drop()
    companies_db.insert_many(companies)
