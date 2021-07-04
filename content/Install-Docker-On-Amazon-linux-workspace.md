Title: Install Docker on Amazon Linux WorkSpaces
Date: 2020-07-03 01:53
Author: sdontireddy
Category: aws
Tags: AWS, Workspace, Docker , Linux
Slug: install-docker-on-amazon-linux-workspaces
Status: published


### Install Docker on Amazon Linux WorkSpaces
This is continuous to the post here , using Amazon Linux2 as my virtual desktop.

Amazon Linux doesnt come with docker pre installed so we need install required packages

##### Installing Docker And Starting the Service

```
$ sudo yum install -y docker

$ sudo service docker start

//Notice : sudo , pls refer below for explanation
$ sudo docker -version
```

##### Manage Docker as a non-root user

The Docker daemon binds to a Unix socket instead of a TCP port. By default that Unix socket is owned by the user root and other users can only access it using sudo. The Docker daemon always runs as the root user.

If you don’t want to preface the docker command with sudo, create a Unix group called docker and add users to it. When the Docker daemon starts, it creates a Unix socket accessible by members of the docker group. Pls refer here for more information.

```
$ sudo groupadd docker

$ sudo usermod -aG docker $USER

$ newgrp docker
```

```
//Test the docker using
$ docker -version

//Run test HelloWorld docker container
$docker run hello-world
You should be able to see 
```

##### Installing docker-compose

```
$ sudo curl -L "https://github.com/docker/compose/releases/download/1.26.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

$ sudo chmod +x /usr/local/bin/docker-compose
 
//Check the docker-compose version
$ docker-compose -version
```