Title: Docker Windows Tips-Trics
Date: 2022-02-20 16:53
Author: sdontireddy
Category: Docker
Tags: GIT, Pipeline  , Docker , Docker Compose
Slug: docker-mount-volume-in-windows
Status: published

# Docker Windows Tips-Trics


### Struggling to mount a host directory on windows machine?

Tip : Use "%cd%" instead of Linux command $(pwd) in Windows  

```
docker run --name compare -it --rm -v "%cd%/report":/usr/app/src/report -v "%cd%/data":/usr/app/src/data ito-compare-excel:latest

```


### Override Default Entry point in docker comppse file 

```
 MyContainer:
    container_name: My-Container
    entrypoint: "tail -f /dev/null"
 ```
 
 ### Override Entry point with docker run
 
 ```
  docker run -it --entrypoint //bin/sh image_name
 ```
 
## Override entry point for a container that is RUNNING  
```
(docker exec -i container_name sh -c "cat > /usr/local/bin/start-app.sh") < ./scripts/custom-entry.sh
- Assumnuing usr/local/bin/start-app.sh is the current entry point,execute above and restart
```
