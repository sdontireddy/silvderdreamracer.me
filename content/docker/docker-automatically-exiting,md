Title: Docker automatically exits
Date: 2022-10-19 22:53
Author: sdontireddy
Category: CI/CD , Docker
Tags: GIT, Pipeline , CI/CD , Docker , Docker Compose
Slug: docker-automatic-stops-exits
Status: published

# Curious why Docker container automatically exits

Are you curious why docker container exits automatically?

Docker Container needs some process running in the foreground (Please note , Not as a background process) to keep the container running.

Dont know how to make a container running with a simple process in the foreground?

```
# open container with a shell prompt
docker run -it IMAGE_NAME /bin/sh

```

Another solution : Simply put an extra line in your entry-point.sh 

Please note the extra line **exec** at the end of the script.

```
#!/bin/bash
set -e
|
|

exec "$@"
```
Please refer here for more information https://stackoverflow.com/questions/32255814/what-purpose-does-using-exec-in-docker-entrypoint-scripts-serve/32261019#32261019
