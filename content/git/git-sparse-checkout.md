Title: Git checkout only specific sub folder or sub module
Date: 2022-09-22 14:13
Author: sdontireddy
Category: git
Tags: GIT 
Slug: git-checkout-only-specific-folder
Status: published

# Git - How to checkout only specific subfolder from the github

Often we just need to clone/download a subfolder/submodule from a bit repo
Example : https://github.com/eugenp/tutorials - This is very big repo with lot of subdirectories

This project has 100's of submodule , however if you are just interested in downloading a subdirectory 
ex:You want to download <b>/spring-cloud-modules/spring-cloud-open-telemetry</b>

```
git clone --no-checkout git@github.com:eugenp/tutorials.git

cd tutorials/

git sparse-checkout set /spring-cloud-modules/spring-cloud-open-telemetry

git reset --hard HEAD
```
