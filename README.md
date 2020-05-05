# Get Corona Virus Data, Kurdistan Weather Status, and IQD Exchange Rate

## The following tools are required to run this project

-   [Python 3](https://www.python.org/) - Programming Language
-   [Django](https://www.djangoproject.com/) - Web Framework
-   [Django Rest Framework](https://www.django-rest-framework.org/) - Web API's
-   [Gunicorn](https://gunicorn.org/) - WSGI HTTP Server
-   [PostgreSQL](https://www.postgresql.org/) - PostgreSQL Database
-   [NginX](https://www.nginx.com/) - High performance web server
-   [Docker](https://www.docker.com/) - Container Platform
-   [Docker Compose] (https://docs.docker.com/compose/) - Multi-container Docker applications.
-   [Git](https://git-scm.com/) - Version Control

##  Installation
First **clone** 
$ git clone https://github.com/the-farshad/coronaVirus.git
```
You will need three Volumes, amd two docker netword, you can create with below command

```sh
$ docker volume create coronavirus_postgresql
$ docker volume create cv_static_volume
$ docker volume create cv_files_volume
```
```sh
$ docker network create nginx_network
$ docker network create cv_network
``` 
You need to change name .env.ample to .env file in the project root file with your coustome values.
```sh
POSTGRES_USER=Postgres Username
POSTGRES_PASSWORD=Postgres Password
POSTGRES_DB=Postgres Databasename
```
Now run django and postgresql with **docker-compose**.
```sh
$ docker-compose up -d
```
Then run nginx container with **docker-compose**.
```sh
$ cd config/nginx/
$ docker-compose up -d
```

#### TODO
> - [x] Dockerize
> - [] Add Telegram API
> - [] Complate django feature


## Contributing
Contributions are  **welcome**  and will be fully  **credited**. I'd be happy to accept PRs for template extending.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/the-farshad/coronaVirus/blob/master/LICENSE) file for details

> ###### Good Luck!
> May the force be with you