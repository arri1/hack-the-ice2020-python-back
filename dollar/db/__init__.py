import pymongo as pymongo

# TODO: Load from env/settings
client = pymongo.MongoClient(
    "mongodb+srv://kekas:kekmasterpassword@cluster0.jhqzb.mongodb.net/test?retryWrites=true&w=majority")
db = client['test']
