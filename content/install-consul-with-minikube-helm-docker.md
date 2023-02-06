Title: Consul Quik Start on MiniKube using Helm Charts
Date: 2023-01-22 22:53
Author: sdontireddy
Category: infra
Tags: infrastructure , network , Consul , MiniKube , Helm Charts
Slug: install-consul-with-minikube-helm-docker
Status: published

# Quik instrcution guide to install Consul with MiniKube , Helm Charts and docker on Linux


#### Pre-requisites

Make sure you have  

2 CPUs or more
4GB of free memory
30GB of free disk space


##### Install MiniKube 
 minikube is local Kubernetes, focusing on making it easy to learn and develop for Kubernetes.

```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

##### Install docker

<b>Why?</b> Minicube get installed / created as a virtual environment using docker.

If you are intersted you can use any of the Container or virtual machine manager, 
such as: Docker, QEMU, Hyperkit, Hyper-V, KVM, Parallels, Podman, VirtualBox, or VMware Fusion/Workstation


##### Install Helm Charts

<b>Why?</b> The best package manager for Kubernetes

If you think you can manage , you can try with Terraform Kubernetes aswell , however Helm provides best of support to mange Kubernetes cluser

```
curl https://baltocdn.com/helm/signing.asc | gpg --dearmor | sudo tee /usr/share/keyrings/helm.gpg > /dev/null
sudo apt-get install apt-transport-https --yes
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/helm.gpg] https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
sudo apt-get update
sudo apt-get install helm

```




minikube start
