import psycopg2
import os

POSTGRES_HOST= os.environ['POSTGRES_HOST']
POSTGRES_PORT= os.environ['POSTGRES_PORT']
POSTGRES_DB = os.environ['POSTGRES_DB']
POSTGRES_USER = os.environ['POSTGRES_USER']
POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']

def conecct():
    conn = None
    if conn == None:
        try:
            conn = psycopg2.connect(f'dbname={POSTGRES_DB} user={POSTGRES_USER} password={POSTGRES_PASSWORD} host={POSTGRES_HOST}')
            return conn
        except:
                print('Fail Conecct')
    else:
        return conn
