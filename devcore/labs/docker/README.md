# Docker Lab Notes

To build and name your docker image from Dockerfile

> NOTE: This must be done in the docker file directory 

`docker build -t [what you name the image] .`

To view your new docker image

`docker images`

To create a Docker network 

`docker network create --subnet=172.20.0.0/24 --gateway=172.20.0.1 [Network Name]`

To view docker networks

`docker network ls`

To view specific docker networks

`docker network inspect [Network Name]`

To create a container with an assigned network, ip, and port mapping

`docker run --net appnet --ip 172.20.0.100 -it -d -p 5000:5000 app`

To view running container

`docker ps`

To view all containers, even those not running

`docker ps -a`

To stop a container `Gracefully`

`docker stop [container name]`

To stop a container none gracefully

`docker kill [container name]`

To delete/remove containers

`docker rm [container name]`

To delete a docker image, -- First all containers assigned to the image must be deleted

`docker rm [IMAGE ID]`

To create a mysql container with environment variables and mounted volume for persistent storage

`docker run --env MYSQL_ALLOW_EMPTY_PASSWORD=yes --net appnet --ip 172.20.0.200 -v ~/working_directory/db:/var/lib/mysql -it mysql:5.7`

To connect to your running containers

`docker exec it [container name] bash`

__

## Creating a Inventory Database in mySQL

To connect to mysql

`mysql`

```sql
CREATE DATABASE inventory;
USE inventory;
CREATE TABLE routers (hostname VARCHAR(255), ip VARCHAR(255));
INSERT INTO routers VALUES ('r1.example.com', '192.168.1.1');
INSERT INTO routers VALUES ('r2.example.com', '192.168.1.2');
INSERT INTO routers VALUES ('r3.example.com', '192.168.1.3');
```

To verify database

`SELECT * FROM inventory.routers;`