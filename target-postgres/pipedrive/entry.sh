#!/bin/sh

sed -i "s|HOST|${HOST}|" postgres.conf.json
sed -i "s|DATABASE|${DATABASE}|" postgres.conf.json
sed -i "s|USER|${USER}|" postgres.conf.json
sed -i "s|PASS|${PASS}|" postgres.conf.json
sed -i "s|SCHEMA|${SCHEMA}|" postgres.conf.json

sed -i "s|PIPE_SECRET|${PIPE_SECRET}|" pipedrive-conf.json

python setup.py

~/.virtualenvs/tap-pipedrive/bin/tap-pipedrive --config pipedrive-conf.json --catalog catalog.json | ~/.virtualenvs/singer-target-postgres/bin/target-postgres --config postgres.conf.json