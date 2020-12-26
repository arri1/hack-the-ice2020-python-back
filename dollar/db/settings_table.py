from dollar.db import db

settings_db = db['settings']


def get_settings():
    if settings_db.count_documents({}) == 0:
        settings_db.insert_one({'verification': 1.5,
                                'part_orders_of_online': 1.0,
                                'own': 1.1,
                                'median_delivery_time': -1.0,
                                'mean_product_price': -1.0,
                                'part_good_order': 1.0,
                                'mean_feedback': 1.0,
                                'mean_call': 1.0,
                                'mean_cost_delivery': -1.0,
                                'count_products': 1.0,
                                'median_sale': 1.0,
                                'part_orders_of_views': 1.0})
    result = dict(settings_db.find_one())
    return result


def update_settings(settings):
    if settings_db.count_documents({}) == 0:
        settings_db.insert_one(settings)
    else:
        settings_db.update_one({}, {"$set": settings})
    return get_settings()
