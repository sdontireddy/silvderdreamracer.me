Title: Install Pelican and configure static site in Amazon S3
date: 2021-07-05 02:14
Author: sdontireddy
Category: WebSite
Tags: Pelican, Reference , Cheat Sheet
Slug: pelical-static-site-deploy-amazon-s3
Status: published

### Create Virtual Environment for Pelican
``` python3 -m venv ~/virtualenvs/pelican
cd ~/virtualenvs/pelican/

source bin/activate
```
#### install Pelican

```python3 -m pip install pelican```
### Validate Pelican installation
```pelican --help```

### Install Pelican Markdown related plugins
```python -m pip install "pelican[markdown]"```

#### Pelican Validation

 ```pelican --help```
#### Check installed Pelican Themes
```pelican-themes -l```

 #### Install Pelican Themes
        
```  cd $PYTHON_HOME 
  mkdir pelican-addon-clones # Optional just creating a separate folder for themese
  cd pelican-addon-clones
  ```
  ```
  git clone https://github.com/alexandrevicenzi/Flex # pick your own theme
  pelican-themes --install Flex/ --verbose
        pelican-themes -l
```

#### Run Dev server
```make devserver
localhost:8000
```
#### Publish output folder

``` make publish ```

#### Sync to S3

 ``` aws s3 sync output/ s3://BUCKET_NAME```
