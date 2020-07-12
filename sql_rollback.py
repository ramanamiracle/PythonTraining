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

    try:
        cursor = conn.cursor()

        cursor.execute("insert into cafe values (NULL, 'coffee', 'test2', 3.19)")
        conn.commit()

        cursor.execute("insert into cafe values (NULL, 'tea', 'test2', 2.99)")
        cursor.execute("insert into cafe (xxx) values ('tea')")  # uncomment to trigger an error
        cursor.execute("insert into cafe values (NULL, 'tea', 'test2', 2.89)")
        conn.commit()

    except pymysql.Error as e:
        print('error {}: {}'.format(e.args[0], e.args[1]))
        if conn:
            conn.rollback()
            print('rolled back...')
        sys.exit(1)  # Raise a SystemExit exception for cleanup, but honor finally-block

    finally:
        print('finally...')
        if conn:
            cursor.execute('select * from cafe')
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            conn.close()


except Exception as e:
    print(e)  # Error code number, description
    sys.exit(1)  # Raise a SystemExit exception for cleanup, but honor finally-block
