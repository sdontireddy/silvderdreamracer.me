Title: CORS with POSTMAN however "No 'Access-Control-Allow-Origin' from a browser
Date: 2021-09-12 10:53
Author: sdontireddy
Category: Postman , CORS , JavaScript
Tags: Postman , CORS , Javascript
Slug: CORS-postman-No-Access-Control-Allow-Origin-From-Browser
Status: published

# CORS with POSTMAN compared to Browser - "No 'Access-Control-Allow-Origin' from a browser

One of the common questions is Why browser throwing 'Access-Control-Allow-Origin' header , however no issues with Postman Desktop tool

```
CORS Error: The request is blocked because of the Cross-Origin Resource Sharing (CORS) policy.
Error: Browser does not support cross-origin requests.

```

According to [CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) 

```
ORS defines a way in which a browser and server can interact to determine whether it is safe to allow the cross-origin request.
It allows for more freedom and functionality than purely same-origin requests, but is more secure than simply allowing all cross-origin requests.
```

So CORS is mainly applicable to browser not to the Postman

### Solution for backend services to allow the list of hosts allowed


```
write this line of code in doPost() function whichever you are using in backend

response.setHeader("Access-Control-Allow-Origin", "*");
```

