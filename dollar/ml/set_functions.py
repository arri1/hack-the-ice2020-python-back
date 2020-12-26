import numpy as np


def set_median_time_delivery(company, orders, products):
    median_times = []
    for _id in company['id']:
        median_times.append(
            orders[orders['id_company'] == _id]['delivery_time'].median())
    company['median_delivery_time'] = median_times
    return company.fillna(0)


def set_mean_product_price(company, orders, products):
    mean_price = []
    for _id in company['id']:
        mean_price.append(
            products[products['id_company'] == _id]['price'].mean())
    company['mean_product_price'] = mean_price
    return company.fillna(0)


def part_good_orders(company, orders, products):
    goods = []
    bads = []
    for _id in company['id']:
        goods.append(
            orders[(orders['id_company'] == _id) & (orders['good'] == 1)][
                'good'].sum())
    for _id in company['id']:
        bads.append(
            orders[(orders['id_company'] == _id) & (orders['bad'] == 1)][
                'bad'].sum())
    company['part_good_order'] = np.array(goods) / (
            np.array(goods) + np.array(bads))
    return company.fillna(0)


def set_good_orders(company, orders, products):
    goods = []
    for _id in company['id']:
        goods.append(
            orders[(orders['id_company'] == _id) & (orders['good'] == 1)][
                'good'].sum())
    company['good_orders'] = goods
    return company.fillna(0)


def set_bad_orders(company, orders, products):
    bads = []
    for _id in company['id']:
        bads.append(
            orders[(orders['id_company'] == _id) & (orders['bad'] == 1)][
                'bad'].sum())
    company['bad_orders'] = bads
    return company.fillna(0)


def set_mean_feedback(company, orders, products):
    mean_feedback = []
    for _id in company['id']:
        mean_feedback.append(
            orders[orders['id_company'] == _id]['feedback'].mean())
    company['mean_feedback'] = mean_feedback
    return company.fillna(0)


def set_mean_call(company, orders, products):
    mean_call = []
    for _id in company['id']:
        mean_call.append(orders[orders['id_company'] == _id]['call'].mean())
    company['mean_call'] = mean_call
    return company.fillna(0)


def set_mean_cost_delivery(company, orders, products):
    mean_cost = []
    for _id in company['id']:
        mean_cost.append(
            orders[orders['id_company'] == _id]['delivery_cost'].mean())
    company['mean_cost_delivery'] = mean_cost
    return company.fillna(0)


def set_count_products(company, orders, products):
    count_products = []
    for _id in company['id']:
        count_products.append(len(products[products['id_company'] == _id]))
    company['count_products'] = count_products
    return company


def set_median_sale(company, orders, products):
    median_sale = []
    for _id in company['id']:
        median_sale.append(
            products[products['id_company'] == _id]['sale'].median())
    company['median_sale'] = median_sale
    return company.fillna(0)


def set_sum_views(company, orders, products):
    sum_view = []
    for _id in company['id']:
        sum_view.append(products[products['id_company'] == _id]['views'].sum())
    company['sum_views'] = sum_view
    return company.fillna(0)


def set_part_orders_of_online(company, orders, products):
    goods = []
    bads = []
    for _id in company['id']:
        goods.append(
            orders[(orders['id_company'] == _id) & (orders['good'] == 1)][
                'good'].sum())
    for _id in company['id']:
        bads.append(
            orders[(orders['id_company'] == _id) & (orders['bad'] == 1)][
                'bad'].sum())
    company['part_orders_of_online'] = (np.array(goods) + np.array(bads)) / \
                                       company['days_online']
    return company.fillna(0)


def set_part_orders_of_views(company, orders, products):
    goods = []
    bads = []
    for _id in company['id']:
        goods.append(
            orders[(orders['id_company'] == _id) & (orders['good'] == 1)][
                'good'].sum())
    for _id in company['id']:
        bads.append(
            orders[(orders['id_company'] == _id) & (orders['bad'] == 1)][
                'bad'].sum())
    sum_view = []
    for _id in company['id']:
        sum_view.append(products[products['id_company'] == _id]['views'].sum())
    company['part_orders_of_views'] = (np.array(goods) + np.array(bads)) / sum_view
    return company.fillna(0)


def set_median_product_price(company, orders, products):
    median_price = []
    for _id in company['id']:
        median_price.append(
            products[products['id_company'] == _id]['price'].median())
    company['median_product_price'] = median_price
    return company.fillna(0)


def set_max_product_price(company, orders, products):
    max_price = []
    for _id in company['id']:
        max_price.append(
            products[products['id_company'] == _id]['price'].max())
    company['max_product_price'] = max_price
    return company.fillna(0)


def set_min_product_price(company, orders, products):
    min_price = []
    for _id in company['id']:
        min_price.append(
            products[products['id_company'] == _id]['price'].min())
    company['min_product_price'] = min_price
    return company.fillna(0)


def set_mean_sale(company, orders, products):
    mean_sale = []
    for _id in company['id']:
        mean_sale.append(
            products[products['id_company'] == _id]['sale'].mean())
    company['mean_sale'] = mean_sale
    return company.fillna(0)


def set_max_sale(company, orders, products):
    max_sale = []
    for _id in company['id']:
        max_sale.append(
            products[products['id_company'] == _id]['sale'].max())
    company['max_sale'] = max_sale
    return company.fillna(0)


def set_min_sale(company, orders, products):
    min_sale = []
    for _id in company['id']:
        min_sale.append(
            products[products['id_company'] == _id]['sale'].min())
    company['min_sale'] = min_sale
    return company.fillna(0)


def main_set(companies, orders, products):
    funcs = [set_median_time_delivery, set_mean_product_price, part_good_orders,
             set_good_orders, set_bad_orders, set_mean_feedback, set_mean_call,
             set_mean_cost_delivery, set_mean_cost_delivery, set_count_products,
             set_median_sale, set_sum_views, set_part_orders_of_online,
             set_part_orders_of_views]
    for func in funcs:
        companies = func(companies, orders, products)
    return companies


def price_set(companies, orders, products):
    funcs = [set_median_product_price, set_max_product_price,
             set_min_product_price]
    for func in funcs:
        companies = func(companies, orders, products)
    return companies


def sale_set(companies, orders, products):
    funcs = [set_max_sale, set_min_sale, set_mean_sale]
    for func in funcs:
        companies = func(companies, orders, products)

    return companies
