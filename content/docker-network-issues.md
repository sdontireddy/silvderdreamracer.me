Title: Docker , Docker compose netwokring isssues settingup CI/CD 
Date: 2022-03-25 22:53
Author: sdontireddy
Category: CI/CD , Docker
Tags: GIT, Pipeline , CI/CD , Docker , Docker network
Slug: docker-compse-network-connection-issues
Status: published

# How i traiged issues with docker/docker compose while setting up CI/CD 

Usecase : Setup a Docker compose file to bringup entire infrastructure required to to test a microservice(infact combination of couple of microservices as we wanted to run domain based integration tests)
as part of the CICD pipelines

Technologies : One service **go** based microservice , another .Net based microservie that expose grpc , Temporal (Orchestrator) , Vault , Consul , Postgress Database

Note : If you have noticed i was trying to bringup the entire infrastrucuture including Vault,DB, Consul, Temporal etc..so that tests are independent of the environments.


Below are some of the challenges / issues faced during the setup

#### Issue #1 : One service not able to communicate with another service

Inorder for one service to communicate with other we have to specify below property on the container which should allow communications from other containers

```
extra_hosts:
        localhost: host-gateway
```
**extra_hosts**
```
extra_hosts adds hostname mappings to the container network interface configuration (/etc/hosts for Linux). Values MUST set hostname and IP address for additional hosts in the form of HOSTNAME:IP.

extra_hosts:
  - "somehost:162.242.195.82"
  - "otherhost:50.31.209.229"
Compose implementations MUST create matching entry with the IP address and hostname in the container's network configuration, which means for Linux /etc/hosts will get extra lines:

162.242.195.82  somehost
50.31.209.229   otherhost
```

#### Issue #2 : Infrastructure is up and working fine on Docker with Windows Sybsystem for Linux , however challenges on Mac

```
The host networking driver only works on Linux hosts, and is not supported on Docker Desktop for Mac, Docker Desktop for Windows, or Docker EE for Windows Server.
```
Solve : Explicitly expose all the requried ports
```
If you use the host network mode for a container, that container’s network stack is not isolated from the Docker host (the container shares the host’s networking namespace), and the container does not get its own IP-address allocated. For instance, if you run a container which binds to port 80 and you use host networking, the container’s application is available on port 80 on the host’s IP address.

Note: Given that the container does not have its own IP-address when using host mode networking, port-mapping does not take effect, and the -p, --publish, -P, and --publish-all option are ignored, producing a warning instead:
```


#### Issue #3 : Communication : InvalidArgument: “host” network_mode is incompatible with port_bindings

We can not expose ports and at the same time cannot use networK_mode as "host" both are mutul exlusive


#### Issue $4 : Applications suppose to comminicate using GRPC are not able to connect to each other

Debug steps : Quickly installed **lsof** package and ran **lsof -i**

**lsof -i** : List all the ports .process opened listening 

This enabled me to see the ports opened for communication

one of the process which was suppose to connect from out side of the current container is listening on **localhost:http**

i.e means this connection is open communication from within the container but not from anther container. 

Once we configured to run this service it will show **`*`:http** - means allow from all the hosts including docker host

```
$ sudo apt-get install lsof     [On Debian, Ubuntu and Mint]
$ sudo yum install lsof         [On RHEL/CentOS/Fedora and Rocky Linux/AlmaLinux]
```

Refernces:

https://github.com/compose-spec/compose-spec/blob/master/spec.md#extra_hosts

