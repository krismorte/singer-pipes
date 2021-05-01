#!/bin/sh

sed -i "s|HOST|${HOST}|" postgres.conf.json
sed -i "s|DATABASE|${DATABASE}|" postgres.conf.json
sed -i "s|USER|${USER}|" postgres.conf.json
sed -i "s|PASS|${PASS}|" postgres.conf.json
sed -i "s|SCHEMA|${SCHEMA}|" postgres.conf.json

sed -i "s|STP_SECRET|${STP_SECRET}|" stripe-conf.json
sed -i "s|STP_CLIENT|${STP_CLIENT}|" stripe-conf.json

python setup.py

~/.virtualenvs/tap-stripe/bin/tap-stripe --config stripe-conf.json --catalog catalog.json | ~/.virtualenvs/singer-target-postgres/bin/target-postgres --config postgres.conf.json