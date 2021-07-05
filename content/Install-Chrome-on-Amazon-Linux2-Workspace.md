Title: Install Chrome on Amazon Linux2 WorkSpaces
Date: 2020-07-03 01:53
Author: sdontireddy
Category: aws
Tags: AWS, Workspace, Chrome , Linux
Slug: install-chrome-on-amazon-linux2
Status: published


### Install Chrome on Amazon Linux2 WorkSpaces
I recently started playing with Amazon workspace as my personal development environment and choose Standard with Amazon Linux 2 as my AMI.

Below quick steps to setup Chrome

Note : Amazon Linux 2 seems to be based on Centos RHEL Fedora based on the /etc/hosts files

Create a new file with the contents given below. This will basically point to google repository for distribution file

```
> sudo vi /etc/yum.repos.d/google-chrome.repo
[google-chrome]
name=google-chrome
baseurl=http://dl.google.com/linux/chrome/rpm/stable/$basearch
enabled=1
gpgcheck=1
gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub
1
yumdownloader google-chrome-stable
```

you should see packages installing and a prompt to accept the security key, press y and enter.

That’s It, you should a message with complete.

```
Retrieving key from https://dl-ssl.google.com/linux/linux_signing_key.pub
Is this ok [y/N]: y
```