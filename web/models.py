#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
testdbconn: Test MySQL Database Connection
"""
import sys
import pymysql.cursors
conn = None


def get_connection():
    global conn
    try:
        if not conn:
            conn = pymysql.connect(host='localhost', user="root", password="ramana", db="sample",
                                   cursorclass=pymysql.cursors.DictCursor)
            return conn
        else:
            return conn
    except Exception as exc:
        print(exc)
        return None


def get_data():
    try:
        conn = get_connection()
        with conn:
            cursor = conn.cursor()
            cursor.execute('select * from cafe')
            return list(cursor.fetchall())
    except Exception as exc:
        print(exc)


def validate_user(username, password):
    try:
        conn = get_connection()
        with conn:
            cursor = conn.cursor()
            cursor.execute('select * from users where username=%s and password=%s', (username, password))
            user_details = cursor.fetchone()
            print(user_details)

            if user_details:
                return True
            else:
                return False

    except Exception as exc:
        print(exc)
        return False


def add_user(username, password):
    try:
        conn = get_connection()
        with conn:
            cursor = conn.cursor()
            affected_count = cursor.execute('insert into users values (NULL, %s, %s)', (username, password))

            print(affected_count)
            if affected_count >= 1:
                return True
            else:
                return False

    except Exception as exc:
        print(exc)
        return False

