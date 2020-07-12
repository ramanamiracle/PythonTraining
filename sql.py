#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
testdbconn: Test MySQL Database Connection
"""
import sys
import pymysql.cursors
conn = None  # Database connection


try:
    # Open database connection.
    # Parameters are: (server_hostname, username, password, database_name, server_port=3306)
    conn = pymysql.connect(host='localhost', user="root", password="ramana", db="sample", cursorclass=pymysql.cursors.DictCursor)
    print('Connected...')

    with conn:  # Automatically close with error handling
        cursor = conn.cursor()

        # Create a new table
        cursor.execute('drop table if exists cafe')

        cursor.execute('''create table if not exists cafe (
                            id int unsigned not null auto_increment,
                            category enum('tea', 'coffee') not null,
                            name varchar(50) not null,
                            price decimal(5,2) not null,
                            primary key (id)
                          )''')

        # Insert one record
        cursor.execute('''insert into cafe (category, name, price) values
                            ('coffee', 'Espresso', 3.19)''')

        # Insert multiple records
        cursor.execute('''insert into cafe (category, name, price) values
                            ('coffee', 'Cappuccino', 3.29),
                            ('coffee', 'Caffe Latte', 3.39),
                            ('tea', 'Green Tea', 2.99),
                            ('tea', 'Wulong Tea', 2.89)''')

        # Commit the insert
        conn.commit()

        print("----------------------Querying---------------------------")
        # Query all records
        cursor.execute('select * from cafe')

        # Fetch all rows from result-set into 'a tuple of tuples'
        rows = cursor.fetchall()
        # print(rows)  # For debugging

        # Process each row (tuple)
        for row in rows:
            print(row.get('unknown'), row.get('price'))

        print("----------------Another-------------------------------------")
        # Another way to fetch row-by-row
        cursor.execute('select * from cafe where category="coffee" and price < 3.3')
        while True:
            row = cursor.fetchone()
            if row == None:
                break
            print(row)


except Exception as e:
    print(e)  # Error code number, description
    sys.exit(1)  # Raise a SystemExit exception for cleanup, but honor finally-block
