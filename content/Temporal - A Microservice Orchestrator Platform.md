Title: Why Temporal - A Microservice Orchestrator Platform
Date: 2022-01-05 02:53
Author: sdontireddy
Category: Temporal
Tags: microservice , fault-tolerance , high-availability , Temporal
Slug: why-temporal-a-microservice-orchestrator
Status: published

## Why Temporal - A Microservice Orchestrator Platform


Temporal Tagline - Taglines for Temporal were  “fault oblivious code — it does not know failure” and “stateful workflow engine.”

In the world of microservices, every customer interaction often requires coordination across many services.
However, as is often the case, a solution to one problem can introduce new problems.

Unlike monolithic apps, microservice often runs on different systems and data can be spread accorss different systems and tech stacks.

So new problem with interconnected microservices is developers are forced to anticipate all failure in any of the interconnected services and cover scenarios and corner cases
within the entire flow, and often developer spends a lot of time writing these exception cases from scratch in order to handle these innumerable failure modes.


And the usual solution is actually a use different technologies like messaging queues, cahcing technologies , intermediatory databases with polling interval set etc..

Example : I work for a team which handles Order management , where we have mulitple services that performs multiple functionalities like order scheduling ,order routing ,
payment ,tax calculations on top of these services which helps to manipulate the orders for customer service and wharehouse teams.

So we eneded up with a custom built orchestrator which keep on updating the "State" of customer orders in a a state database along 
with some additional queue for each of the process that updates the state.

Above solutions works perfects however there is no standard way of implementing these solutions and most of these solutions are not
reusuable accross the stacks and additional code leading more issues which does not any value to the business at the expense of developer time just to make sure applications are reliable enough.

Especially with "Stateless microservices" often the solution is to store the "state" of logic and keep updating the "State" with every request.

That’s where Temporal technology enables any application to handle failures gracefully and in a user-friendly way.

### Temporal 

Temporal is an open-source  stateful, microservice orchestration runtime.

```
Temporal has two major components: a stateful backend layer which is powered by the database of your choice and a client-side framework in one of the supported languages.
Applications are built using a client-side framework and plain old code which automatically persists state changes to the backend while your code runs.
````

Microservices are great but the price developers and businesses pay in productivity and reliability to use them is not.
Temporal aims to solve this problem by providing an environment that pays the microservice tax for the developer.
