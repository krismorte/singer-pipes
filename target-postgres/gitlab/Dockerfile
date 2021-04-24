FROM python:3.9.4-alpine3.13 

ENV HOST=
ENV DATABASE=
ENV USER=
ENV PASS=
ENV SCHEMA=
ENV GL_TOKEN=
ENV GL_GROUP=
    

#POSTGRES DEPENDENCIES
RUN apk add postgresql-dev=13.2-r0 gcc=10.2.1_pre1-r3 py3-setuptools=51.3.3-r0 musl-dev=1.2.2-r0 
#SINGER INSTALLATION
RUN python3 -m venv ~/.virtualenvs/tap-gitlab && python3 -m venv ~/.virtualenvs/singer-target-postgres
RUN source ~/.virtualenvs/tap-gitlab/bin/activate && pip3 install tap-gitlab==0.5.1 
RUN source ~/.virtualenvs/singer-target-postgres/bin/activate && pip3 install singer-target-postgres==0.2.4

RUN pip install requests psycopg2

COPY *.json /
COPY *.py /
COPY entry.sh .

ENTRYPOINT [ "./entry.sh" ]