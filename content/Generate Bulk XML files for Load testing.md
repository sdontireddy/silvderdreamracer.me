Title: Generate Bulk XML files for Load testing using JMeter
Date: 2021-07-04 20:53
Author: sdontireddy
Category: Performance
Tags: Jmeter, Performance , Loadtesting
Slug: jmeter-generate-bulk-xml-files-load-testing
Status: published

# Generate Bulk XML files for Load testing

UseCase : One of the very common use cases while performing loading testing an backend applications /services that rely on XML's as input is to generate 1000's of XMLs  with minor differences and feed in to the application in order to gather the metrics for the services under stress. 

Example applications  : A sample Mule application that reads a Distribution Order XML file and transforms in to a simple financial system asynchronous message.

However in order to load test this application , we would need to generate bulk of of these Distribution Order XML's with very minor medications like different distribution order id , quantity , price and some time the child line items aswell. 

## Solution

A **Java + Jmeter + Maven  + YM **  based simple solution that needs very minimal codes changes.

Imagine the if this is the only configuration file needed to generate required number of distribution orders related XML that you can feed to your system.

```
---

bulkloadconfig:

samplefile : DO_sample_under_resource.xml # Sample XML file
numberoffiles: 100 # Number of XML files to generate
childnode: LineItem # We wanted to have different number child nodes with name LineItem , Consider this as a customer order with 2 items vs orders with 5 items. 
numberofchildnodes: 5 # Max child nodes in any given XML , So when bulk xmls are generated a random number between 1 to 5 number of child nodes will be created
resultsfolderwithpath: "../../../results//" # Output folder relative to your path

xmlnodes:
-
name: DistributionOrderId # Field name which needs to be different in each of the files
path: //DistributionOrderId # corresponding XPath
value:
generatedvalue: randomstring # how you want that value to be
prefix: SD # any prefix?
suffix: 061721 # Any suffix
-
name: OrderedDttm
path: /tXML/Message/DistributionOrder/OrderedDttm
value:
generatedvalue: date
adddays : 10
format: yyyy-MM-dd'T'HH:mm:ss.SSSZ
```

Please refer to [project](https://github.com/sdontireddy/performance-tests) for more information.

 
