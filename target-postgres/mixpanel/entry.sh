#!/bin/sh

sed -i "s|HOST|${HOST}|" postgres.conf.json
sed -i "s|DATABASE|${DATABASE}|" postgres.conf.json
sed -i "s|USER|${USER}|" postgres.conf.json
sed -i "s|PASS|${PASS}|" postgres.conf.json
sed -i "s|SCHEMA|${SCHEMA}|" postgres.conf.json

sed -i "s|MIX_SECRET|${MIX_SECRET}|" mix-conf.json

python setup.py

~/.virtualenvs/tap-mixpanel/bin/tap-mixpanel --config mix-conf.json --discover > catalog.json

~/.virtualenvs/tap-mixpanel/bin/tap-mixpanel --config mix-conf.json --catalog catalog.json | ~/.virtualenvs/singer-target-postgres/bin/target-postgres --config postgres.conf.json