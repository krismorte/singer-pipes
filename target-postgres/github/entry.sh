#!/bin/sh


sed -i "s|HOST|${HOST}|" postgres.conf.json
sed -i "s|DATABASE|${DATABASE}|" postgres.conf.json
sed -i "s|USER|${USER}|" postgres.conf.json
sed -i "s|PASS|${PASS}|" postgres.conf.json
sed -i "s|SCHEMA|${SCHEMA}|" postgres.conf.json

sed -i "s|GH_TOKEN|${GH_TOKEN}|" github.conf.json

python setup.py

~/.virtualenvs/tap-github/bin/tap-github --config github.conf.json --properties properties.json | ~/.virtualenvs/singer-target-postgres/bin/target-postgres --config postgres.conf.json
