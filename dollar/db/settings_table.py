from dollar.db import db

settings_db = db['settings']


def get_settings():
    if settings_db.count_documents({}) == 0:
        settings_db.insert_one({'smth_k': 1})
    result = dict(settings_db.find_one())
    return result


def update_settings(settings):
    if settings_db.count_documents({}) == 0:
        settings_db.insert_one(settings)
    else:
        settings_db.update_one({}, {"$set": settings})
    return get_settings()
