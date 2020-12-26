from dollar.db import db
import pymongo

companies_db = db['companies']


def get_companies_count_and_page(page, per_page, sort_by, is_descending):
    total = companies_db.count_documents({})
    items = list(
        companies_db.find().sort(sort_by, direction=(pymongo.DESCENDING if is_descending else pymongo.ASCENDING)).skip(
            page * per_page).limit(per_page))
    return total, items


def update_companies_collection(companies):
    companies_db.drop()
    companies_db.insert_many(companies)
