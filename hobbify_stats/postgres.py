#!/usr/bin/env python
"""This script contains the connection with postgres"""
import os
import psycopg2

POSTGRES_HOST = os.environ['POSTGRES_HOST']
POSTGRES_PORT = os.environ['POSTGRES_PORT']
POSTGRES_DB = os.environ['POSTGRES_DB']
POSTGRES_USER = os.environ['POSTGRES_USER']
POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']

def conecct():
    """Function to connection with postgres"""
    conn = None
    if conn is None:
        try:
            conn = psycopg2.connect(f"""dbname={POSTGRES_DB}
                                        user={POSTGRES_USER} 
                                        password={POSTGRES_PASSWORD} 
                                        host={POSTGRES_HOST}""")
            return conn
        except psycopg2.DatabaseError:
            print('Fail Conecct')
    else:
        return conn
