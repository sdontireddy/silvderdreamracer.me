Title: Consul Quik Start on MiniKube using Helm Charts
Date: 2023-01-22 22:53
Author: sdontireddy
Category: infra
Tags: infrastructure , network , Consul , MiniKube , Helm Charts
Slug: install-consul-with-minikube-helm-docker-kubernetes
Status: published

# Quik instrcution guide to install Consul with MiniKube , Helm Charts and docker on Linux


#### Pre-requisites

Make sure you have  

2 CPUs or more
4GB of free memory
30GB of free disk space


##### Install MiniKube 
 minikube is local Kubernetes, focusing on making it easy to learn and develop for kubernetes.

```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

```
minikube start
```

Please refer [here](https://minikube.sigs.k8s.io/docs/start/) more info

##### Install docker

<b>Why?</b> MiniKube-Kubernetes gets installed / created as a virtual environment using docker.

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
#### Install the Consul
```
   minikube start --driver=docker ## To start the MiniKube Kubernetese Dev Cluser on local machine
   helm install -f consul-values.yaml consul hashicorp/consul --create-namespace -n consul --version 1.0.2 # Create a counsul namespace
   
   Download the sample consult from Hashicorp
   git clone https://github.com/hashicorp-education/learn-consul-service-mesh-deploy.git
   cd learn-consul-service-mesh-deploy
   
   Install Consul Helm Charts 
   helm install -f consul-values.yaml consul hashicorp/consul --create-namespace -n consul --version 1.0.2
   
   Validate the installation 
   kubectl get pods --namespace consul --selector app=consul
   
   Expose Consult UI port
   kubectl port-forward pods/consul-server-0 8500:8500 --namespace consul
   
   Now we can access Consult UI at localhost:8500/ui
   
   
   Deploy Sample app from Hashicorp
   kubectl apply -f hashicups/
   
   Check the services
   
   kubectl get pods --selector consul.hashicorp.com/connect-inject-status=injected
   
   Expose the app
   kubectl port-forward service/nginx 18080:80 --address 0.0.0.0
   
   The HashiCups UI will be available at http://localhost:18080 in your browse
   
   
   ### Kill everything
   
   minikube delete --all
   
```

Once you install the Pre-requisites , please follow the below steps mentioned [here](https://developer.hashicorp.com/consul/tutorials/kubernetes-features/service-mesh-deploy) for deploying a sample Consult on to the new cluser and then deploying a sample application whith Service Mesh





