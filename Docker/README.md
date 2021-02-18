# Docker notes

What are containers?

- Portable virtualization of the operating system and applications
- Uses Docker to create containers
- Containers is the bare minimal you need to run an app.
- No OS because it shares the under lining OS with the OS that runs on top of.
  - Any applications or packages that are needed to run will be installed in the container.

What is Docker?

- Used to manage containers
- Simple CLI that has dockers command that allow you to start, stop, and pull down new containers from docker hub.
- You can build your own containers using the docker file.

Benefits of using a container:

- Minimize the gap between development and deployment
- Faster and more lightweight than a VM
- Applications that work on every machine (with Docker installed)
- Adds to the DevOps paradigm
- Package applications and dependencies.
- Guarantee portability and consistency of execution.
- Keep an application isolated.
- Take advantage of the isolation offered by a VM without the overhead.
- NOTE there is only one kernel

## Installing Docker (Ubuntu)

### Commands

Verify that all old instances have been uninstalled from your machine.

```bash
sudo apt-get remove docker docker-engine docker.io containerd runc
```

Update your repositories

```bash
sudo apt-get update
```

Install the applications that docker depends on:

```bash
sudo apt-get install \
apt-transport-https \
ca-certificates \
curl \
gnupg-agnet \
software-properties-common
```

Add the correct docker repo to your database to get the keys

```bash
curl -fssl https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

Ensure that you are getting the stable release of docker

```bash
sudo add-apt-repository \
deb [arch=amd64] https://download.docker.com/linux/ubuntu \
$(sb_release -cs) \
Stable
```

Update the database so it knows where to go to get the docker repo

```bash
sudo apt-get update
```

Install docker "ce-community edition" and the containerd.io that is needed to run containers

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

Run docker to verify that docker is up and running with interactive terminal. While pulling down the nyancat image from the Docker hub. https://hub.docker.com/r/06kellyjac/nyancat

```bash
sudo docker run -it --rm --name nyancat 06kellyjac/nyancat
```

Docker Networking

- Docker networks provide more isolation for the containers
- By default containers run in a bridge network `172.x.x.x`

Examples

```bash
docker network create <id-n> 
docker network connect <id-n> <id-c>
docker run --network custom-net example-app
```

Docker Peristent Data

Containers are meant to be immutable and disposable by design. 

If you remove/delete your container your data is lost.

NOTE: Filesystem data is not lost if you stop or restart a container

Docker is using three built-in solutions for persisting data:

- Volumes - Best way
  - /var/lib/docker/volumes
  - Attach to any container
  - Non-Docker processes can modify the data at any time
  - Preferred option for persistent storage
  - `docker run -v app-volume:/var/lib/app`
- Bind Mounts
  - Can point to any path on a file system
  - `docker run -v /home/cisco/app:/var/lib/app`
- tmpfs mounts
  - Memory only

To verify volumes

`docker volume ls`

`docker volume inspect [volume name]`

### DockerFile - To turn your python apps into a container

In vscode install docker extension

### Configure docker file

Version of the base OS

`FROM ubuntu:18.04`

Who created the file

`MAINTAINER Du'An Lightfoot "duanl@labeveryday.com"`

Run - Make sure the system is up to date then install these know applications (no need to specify)

`RUN apt-get update -y && apt-get install -y python3-pip python3-dev`

These raw commands need to be specified

`CMD ["ufw allow 5000"]`

To tell python the needed libraries, use a requirements file. (NOTE you are copying the local requirements.txt to the /app folder in the container.

`COPY ./requirements.txt /app/requirements.txt`

Now tell your container to change to the new working directory.

`WORKDIR /app`

### Manage Docker

Once you have your Dockerfile created. To build your container run:

```docker
docker build -t app .
```
Verify your version of Docker

`docker -v`

Start and test your container

`docker run -it -p 5000:5000 app`

View containers that are running

`docker ps`

View all docker containers

`docker ps --all`

Stop a docker container `Gracefully`

`docker stop [container id]`

Stop all docker containers `Gracefully`

`docker stop $(docker ps -a -q)`

Remove all docker containers

`docker rm $(docker ps -a -q)`

Create and name a docker network

`docker network create --subnet=192.168.0.0/24 --gateway=192.168.0.1 Network_Name`

Verify the network was created

`docker network inspect Network_Name`

Run the container with the network and an ip in the subnet you created

`docker run --net Network_Name --ip 192.168.0.100 -it -d -p 5000:5000 app`

Run a docker container with Limited Memory and CPU Resources

`docker run -d --name my_container --publish 8080:8080 --memory 200m --memory-swap 1G --cpu-shares 1024 app`

To remove:
- all stopped containers
- all networks not used by at least one container
- all dangling images
- all dangling build cache

`docker system prune` 

Also look into: `docker-gctool`

To connect to container through bash

`docker exec -it [container it from docker ps] bash`

#### Resources

[Cisco DevCor E-Learning and Exam Bundle](https://learningnetworkstore.cisco.com/on-demand-e-learning/devcor-and-exam-bundle-eltex-devcor-v1-024496)

[Free - DevNet Docker Content](https://developer.cisco.com/learning/login?refLink=%252Flab%252Fcontainers-101%252Fstep%252F1)

[Understanding Container Images, Part 1: Image Layers](https://blogs.cisco.com/developer/container-image-layers-1)

[Understanding Container Images, Part 2: Optimizing Your Images](https://blogs.cisco.com/developer/container-images-2)
