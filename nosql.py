#!/usr/bin/python3

from pymongo import MongoClient
from datetime import datetime
from pprint import pprint

cars = [{'name': 'Audi', 'price': 52642},
        {'name': 'Mercedes', 'price': 57127},
        {'name': 'Skoda', 'price': 9000},
        {'name': 'Volvo', 'price': 29000},
        {'name': 'Bentley', 'price': 350000},
        {'name': 'Citroen', 'price': 21000},
        {'name': 'Hummer', 'price': 41400},
        {'name': 'Volkswagen', 'price': 21600}]

client = MongoClient('mongodb://localhost:27017/')

with client:
    db = client.sample
    # db.cars.delete_many({})
    #
    # result = db.cars.insert_many(cars)
    # print(result.inserted_ids)
    # name = 'Audi'
    # value = 50000
    #
    # query = {'name': name, 'price': {'$gt': value}}
    # query = {}
    # result = db.cars.find(query)
    # for row in result:
    #     print(row)

    # name = 'Audi'
    # value = 60000
    # emp = 'Raman'
    #
    # query = {'name': name}
    # update = {'$set': {'price': value, 'updated_date': datetime.now(), 'updated_by': emp}}
    #
    # db.cars.update_one(query, update)
    #
    # result = db.cars.find({})
    # for row in result:
    #     print(row)

    # name = 'Audi'
    #
    # query = {'price': {'$lt': 50000}}
    #
    # db.cars.delete_many({})
    #
    result = db.cars.find({})
    for row in result:
        print(row.get('price'))

