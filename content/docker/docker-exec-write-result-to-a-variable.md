Title: Docker execute a command and store the output to a variable
Date: 2023-02-22 21:11
Author: sdontireddy
Category:  Docker
Tags: Shell, CLI  , Docker , Docker Compose
Slug: docker-exec-write-result-to-a-variable
Status: published

# How to exectute a command inside a docker and write the output to a variable
 This command bringsup a docker and exectes the command inside the docker and stores the output into client

```
client =$(docker exec command)
```

<b>Example</b> :  This command bringsup a docker and exectes the command inside the docker and stores the output into client

```
client=$(docker-compose -f quickstart.yml exec hydra \
    hydra create client \
    --endpoint http://127.0.0.1:4445/ \
    --format json \
    --grant-type client_credentials)
    
 ```
 
 
#### Notes : 
#### We can parse the JSON response using <b>jq</b> to get the client ID and client secret:
client_id=$(echo $client | jq -r '.client_id')
client_secret=$(echo $client | jq -r '.client_secret')

 JQ is a lightweight and flexible command-line JSON processor. Please refer https://stedolan.github.io/jq/ for more info

