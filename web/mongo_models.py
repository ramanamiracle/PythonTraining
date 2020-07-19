from pymongo import MongoClient
from bson import ObjectId

client = None


def get_client():
    global client
    try:
        if not client:
            client = MongoClient('mongodb://localhost:27017/')
            return client
        else:
            return client
    except Exception as exc:
        print(exc)
        return None


def get_user(user_id):
    client = get_client()
    db = client.sample
    return db.users.find({"_id": ObjectId(user_id)}, {"_id": 0})


def delete_user(user_id):
    client = get_client()
    db = client.sample
    return db.users.delete_one({"_id": ObjectId(user_id)})


def put_user(user_id, data):
    client = get_client()
    db = client.sample
    return db.users.update_one({"_id": ObjectId(user_id)}, {"$set": data})


def get_users():
    client = get_client()
    db = client.sample
    return db.users.find({}, {"_id": 0})


def add_user(data):
    client = get_client()
    db = client.sample
    return db.users.insert_one(data)