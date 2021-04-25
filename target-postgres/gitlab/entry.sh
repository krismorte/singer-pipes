#!/bin/sh

sed -i "s|HOST|${HOST}|" postgres.conf.json
sed -i "s|DATABASE|${DATABASE}|" postgres.conf.json
sed -i "s|USER|${USER}|" postgres.conf.json
sed -i "s|PASS|${PASS}|" postgres.conf.json
sed -i "s|SCHEMA|${SCHEMA}|" postgres.conf.json

sed -i "s|GL_TOKEN|${GL_TOKEN}|" gitlab.conf.json
sed -i "s|GL_GROUP|${GL_GROUP}|" gitlab.conf.json

python setup.py

~/.virtualenvs/tap-gitlab/bin/tap-gitlab --config gitlab.conf.json | ~/.virtualenvs/singer-target-postgres/bin/target-postgres --config postgres.conf.json