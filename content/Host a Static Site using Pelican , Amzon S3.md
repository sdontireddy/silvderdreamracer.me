Title: Host a Static Site using Pelican , Amzon S3 for less than 1$
date: 2021-07-07 02:14
Author: sdontireddy
Category: WebSite
Tags: Pelican, Reference ,Github Actions
Slug: pelican-static-site-amazon-s3-using-githib-action-CICD
Status: published

## Host a Static Site using Pelican , Amzon S3 for less than a $1*

This article was basis for creating my personal site [SilverDreamRacer.me]( www.silverdreamracer.me) static site.
The only cost for me was 
- Amazon Route 53 Hosted Zones : 0.5$

*Ofcourse there is domain cost ,  I have got my domain for free part of another domain hosting  deal.

#### Technolgies Used
- [Pelican Static Site Generator](https://blog.getpelican.com/)
- AWS Resources
    - AWS CloudFront 
    - AWS Route 53  
    - AWS S3
    - AWS LambdaEdge
    - AWS Certificate Manager
- github.com actions for CI/CD
    -  AWS CloudFormation for creating a AWS managed user for github actions    

#### Pelican Static Site Generator
A simple easy to use static Site generator devloped in Python.
We can create content in Markdown , so no additional resources required. Please [Pelican Static Site Generator](https://blog.getpelican.com/) for more information.

Pls refer to my [quick-reference](https://www.silverdreamracer.me/pelical-static-site-deploy-amazon-s3.html) for installtion commands.

Article intention is not to provide step by step instruction on how to use Pelican. So please go through the steps [here](https://docs.getpelican.com/en/latest/quickstart.html) for additional information.

#### One time Setup

A simple static site hosted on aws needs below few important resources

- Amazon S3 – Creates an Amazon S3 bucket to host your static website.

- CloudFront – Creates a CloudFront distribution to speed up your static website.

- Lambda@Edge – Uses Lambda@Edge to add security headers to every server response. Security headers are a group of headers in the web server response that tell web browsers to take extra security precautions. For more information, see the blog post Adding HTTP security headers using Lambda@Edge and Amazon CloudFront.

##### Configure AWS resources

Easy and simplest way is to use AWS Cloudformation Template outlined [here](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/getting-started-secure-static-website-cloudformation-template.html) to deploy/configure these resources.
