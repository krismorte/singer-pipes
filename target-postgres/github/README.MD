# Github -> Postgres

A singer.io pipeline from github to postgres. All data imported from github will be saved in a specific postgres schema, the image will handle this creation whether if exists or not

## Command line

Variables
>HOST
>DATABASE
>USER
>PASS
>SCHEMA
>GH_USER
>GH_ORG
>GH_TOKEN

```sh
docker run --rm -it -e HOST=<IP> -e DATABASE=<DB> -e USER=<USER> -e PASS=<SECRET> -e SCHEMA=<SCHEMA> -e GH_USER=<USER> -e GH_ORG=<ORG> -e GH_TOKEN=<TOKEN> krismorte/singer.io:github-postgres
```