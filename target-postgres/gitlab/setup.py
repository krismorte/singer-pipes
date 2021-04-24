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


gl_token = os.environ['GL_TOKEN']

headers = {
    'Authorization': 'Bearer '+ gl_token
}


# request = requests.get(f'https://gitlab.com/api/v4/groups?visibility=private',headers=headers)

# allRepos = ""

# json = request.json()
# for i in range(0,len(json)):
#   print(i+1, "Project Name: ",json[i]['name'])
#   allRepos = allRepos + json[i]['full_path']+" "
  

# fin = open("gitlab.conf.json", "rt")
# #read file contents to string
# data = fin.read()
# #replace all occurrences of the required string
# data = data.replace('GL_GROUPS', allRepos)
# #close the input file
# fin.close()
# #open the input file in write mode
# fin = open("gitlab.conf.json", "wt")
# #overrite the input file with the resulting data
# fin.write(data)
# #close the file
# fin.close()  