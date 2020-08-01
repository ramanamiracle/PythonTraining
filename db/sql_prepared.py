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

        cursor.execute('''create table if not exists cafe (
                            id int unsigned not null auto_increment,
                            category enum('tea', 'coffee') not null,
                            name varchar(50) not null,
                            price decimal(5,2) not null,
                            primary key (id)
                          )''')

        print("--------------------insert-------------------------")
        # Using prepared-statement via printf-like formatting specifiers
        # Use %s for all fields?!
        sql = 'insert into cafe (category, name, price) values (%s, %s, %s)'

        t = ('coffee', 'Espresso1', 3.19)
        # Execute for one set of data
        cursor.execute(sql, t)

        # Execute for more than one set of data
        data = [('coffee', 'Cappuccino', 3.29),
                ('coffee', 'Caffe Latte', 3.39),
                ('tea', 'Green Tea', 2.99),
                ('tea', 'Wulong Tea', 2.89)]

        cursor.executemany(sql, data)

        conn.commit()  # Commit the insert

        cursor.execute('select * from cafe')
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        print("------------------------------Update-----------------------")
        # Another example
        item = 'Cappuccino'
        cursor.execute('update cafe set price = price * 1.1 where name = %s', (item,))  # or one-element list: [item]

        cursor.execute('select * from cafe where name = %s', [item])
        row = cursor.fetchone()
        print(row)

except Exception as e:
    print(e)  # Error code number, description
    sys.exit(1)  # Raise a SystemExit exception for cleanup, but honor finally-block
