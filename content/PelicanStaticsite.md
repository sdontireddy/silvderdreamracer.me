Title: Install Pelican and configure static site in Amazon S3
date: 2021-06-21 01:53
Author: sdontireddy
Category: AWS
Tags: Aws, Reference , Cheat Sheet
Slug: pelical-static-site-deploy-amazon-s3
Status: published

### Create Virtual Environment for Pelican
python3 -m venv ~/virtualenvs/pelican
cd ~/virtualenvs/pelican/

source bin/activate

#### install Pelican

python3 -m pip install pelican
### Validate Pelican installation
pelican --help

### Install Pelican Markdown related plugins
python -m pip install "pelican[markdown]"

#### Pelican Quick Start

