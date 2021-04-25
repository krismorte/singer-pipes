# Gitlab -> Postgres

A singer.io pipeline from gitlab to postgres. All data imported from gitlab will be saved in a specific postgres schema, the image will handle this creation whether if exists or not

## Command line

Variables
>HOST
>DATABASE
>USER
>PASS
>SCHEMA
>GL_TOKEN
>GL_GROUP

```sh
docker run --rm -it -e HOST=<IP> -e DATABASE=<DB> -e USER=<USER> -e PASS=<SECRET> -e SCHEMA=<SCHEMA> -e GL_TOKEN=<TOKEN > -e GL_GROUP=<GROUPT> krismorte/singer.io:gitlab-postgres
```