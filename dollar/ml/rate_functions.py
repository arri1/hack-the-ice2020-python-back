import numpy as np
from catboost import CatBoostRegressor


def rate_meadian_time_delivery(df, dict_coef):
    X_train, y_train = [[df['median_delivery_time'].max()],
                        [df['median_delivery_time'].min()]], [
                           df['mean_product_price'].max(),
                           df['mean_product_price'].min()]
    df['rate'] += CatBoostRegressor().fit(X_train, y_train).predict(
        df['median_delivery_time']) * dict_coef['median_delivery_time'] / 1000
    return df


def rate_mean_product_price(df, dict_coef):
    df['rate'] += df['mean_product_price'] * dict_coef['mean_product_price'] / 1000
    return df


def rate_part_goods(df, dict_coef):
    X_train, y_train = [[df['part_good_order'].max()],
                        [df['part_good_order'].min()]], [
                           df['mean_product_price'].max(),
                           df['mean_product_price'].min()]
    df['rate'] += CatBoostRegressor().fit(X_train, y_train).predict(
        df['part_good_order']) * dict_coef['part_good_order'] / 1000
    return df


def rate_mean_feedback(df, dict_coef):
    X_train, y_train = [[df['mean_feedback'].max()],
                        [df['mean_feedback'].min()]], [
                           df['mean_product_price'].max(),
                           df['mean_product_price'].min()]
    df['rate'] += CatBoostRegressor().fit(X_train, y_train).predict(
        df['mean_feedback']) * dict_coef['mean_feedback'] / 1000
    return df


def rate_mean_call(df, dict_coef):
    X_train, y_train = [[df['mean_call'].max()],
                        [df['mean_call'].min()]], [
                           df['mean_product_price'].max(),
                           df['mean_product_price'].min()]
    df['rate'] += CatBoostRegressor().fit(X_train, y_train).predict(
        df['mean_call']) * dict_coef['mean_call'] / 1000
    return df


def rate_mean_cost_delivery(df, dict_coef):
    X_train, y_train = [[df['mean_cost_delivery'].max()],
                        [df['mean_cost_delivery'].min()]], [
                           df['mean_product_price'].max(),
                           df['mean_product_price'].min()]
    df['rate'] += CatBoostRegressor().fit(X_train, y_train).predict(
        df['mean_cost_delivery']) * dict_coef['mean_cost_delivery'] / 1000
    return df


def rate_part_orders_of_online(df, dict_coef):
    X_train, y_train = [[df['part_orders_of_online'].max()],
                        [df['part_orders_of_online'].min()]], [
                           df['mean_product_price'].max(),
                           df['mean_product_price'].min()]
    df['rate'] += CatBoostRegressor().fit(X_train, y_train).predict(
        df['part_orders_of_online']) * dict_coef['part_orders_of_online'] / 1000
    return df


def rate_count_products(df, dict_coef):
    X_train, y_train = [[df['count_products'].max()],
                        [df['count_products'].min()]], [
                           df['mean_product_price'].max(),
                           df['mean_product_price'].min()]
    df['rate'] += CatBoostRegressor().fit(X_train, y_train).predict(
        df['count_products']) * dict_coef['count_products'] / 1000
    return df


def rate_median_sale(df, dict_coef):
    X_train, y_train = [[df['median_sale'].max()],
                        [df['median_sale'].min()]], [
                           df['mean_product_price'].max(),
                           df['mean_product_price'].min()]
    df['rate'] += CatBoostRegressor().fit(X_train, y_train).predict(
        df['median_sale']) * dict_coef['median_sale'] / 1000
    return df


def rate_part_orders_of_views(df, dict_coef):
    X_train, y_train = [[df['part_orders_of_views'].max()],
                        [df['part_orders_of_views'].min()]], [
                           df['mean_product_price'].max(),
                           df['mean_product_price'].min()]
    df['rate'] += CatBoostRegressor().fit(X_train, y_train).predict(
        df['part_orders_of_views']) * dict_coef['part_orders_of_views'] / 1000
    return df


def rate_verification(df, dict_coef):
    df['rate'] += df['verification'] * df['rate'] * (
            dict_coef['verification'] - 1)
    return df


def rate_own(df, dict_coef):
    df['rate'] += df['own'] * df['rate'] * (dict_coef['own'] - 1)
    return df


dict_chars = {'verification': rate_verification,
              'days_online': rate_part_orders_of_online, 'own': rate_own,
              'median_delivery_time': rate_meadian_time_delivery,
              'mean_product_price': rate_mean_product_price,
              'good_orders': rate_part_goods,
              'mean_feedback': rate_mean_feedback, 'mean_call': rate_mean_call,
              'mean_cost_delivery': rate_mean_cost_delivery,
              'count_products': rate_count_products,
              'median_sale': rate_median_sale,
              'sum_views': rate_part_orders_of_views}


def make_rate(company, dict_coef, chosen_chars):
    company['rate'] = np.zeros(len(company))
    for choice in chosen_chars:
        if choice in dict_chars:
            company = dict_chars[choice](company, dict_coef)
    return company['rate']
