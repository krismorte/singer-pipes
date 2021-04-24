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

gh_user = os.environ['GH_USER']
gh_org = os.environ['GH_ORG']
gh_token = os.environ['GH_TOKEN']

moreRepos = True
pageNo = 1
request = requests.get(f'https://api.github.com/orgs/{gh_org}/repos?type=all&page={pageNo}&per_page=100',auth = HTTPBasicAuth(gh_user, gh_token))

allRepos = ""

while moreRepos:

  json = request.json()
  for i in range(0,len(json)):
    print(i+1, "Project Name: ",json[i]['name'])
    allRepos = allRepos + json[i]['full_name']+" "
  
  if len(json)<100:
    print ("bye")
    moreRepos=False
  else:
    pageNo= pageNo + 1
    request = requests.get(f'https://api.github.com/orgs/{gh_org}/repos?type=all&page={pageNo}&per_page=100',auth = HTTPBasicAuth(gh_user, gh_token))

fin = open("github.conf.json", "rt")
#read file contents to string
data = fin.read()
#replace all occurrences of the required string
data = data.replace('GH_REPOS', allRepos)
#close the input file
fin.close()
#open the input file in write mode
fin = open("github.conf.json", "wt")
#overrite the input file with the resulting data
fin.write(data)
#close the file
fin.close()  