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
