import requests
import psycopg2
import os
from requests.auth import HTTPBasicAuth

host = os.environ['HOST']
database = os.environ['DATABASE']
user = os.environ['USER']
password = os.environ['PASS']
schema = os.environ['SCHEMA']

conn = psycopg2.connect(host=host, database=database,
user=user, password=password)

cur = conn.cursor()

cur.execute('SELECT nspname FROM pg_catalog.pg_namespace where nspname=\''+schema+'\'')
records = cur.fetchall()
if len(records) == 0:
    cur.execute('create schema '+schema+';')
    print('Postgres Schema created')


cur.close()
conn.commit()
conn.close()