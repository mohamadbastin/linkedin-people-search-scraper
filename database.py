import pymongo


class DatabaseManager:
    db = None

    @staticmethod
    def init():
        my_client = pymongo.MongoClient("mongodb://localhost:27017/")

        db = my_client["mydatabase"]
        DatabaseManager.db = db
        return db

    @staticmethod
    def get_db_reference():
        return DatabaseManager.db

    @staticmethod
    def insert_many_if_duplicate_pass(collection, data):
        for i in data:
            try:
                collection.insert_one(i)
            except pymongo.errors.DuplicateKeyError:
                continue
        print("wrote result to database.")
        return True
