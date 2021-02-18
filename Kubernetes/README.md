# Kubernetes

Kubernetes also called K8s
|--------|
    ^
   K8s
Because there are 8 characters between the K and s or Kubernetes. 

To Get Started with Kubernetes basics in a lab. [Go Here](https://kubernetes.io/docs/tutorials/kubernetes-basics/)

To create a local Kubernetes cluster. [Minikube](https://github.com/kubernetes/minikube) and [minikube start](https://minikube.sigs.k8s.io/docs/start/)

## About Kubernetes

Kubernetes cluster is an open source orchestration system, designed by google. Kubernetes manages your containerized applications ensuring that they are available, where and when you want, and that they have the resources they need. In other words it allows you to automate the management and deployment of all of your containers. 



To Understand the K8s Architecture:

Container Images
- One single container

Pod
- A collection of containers

Worker Nodes:
- VMs (Servers)
- A collection of pods

Cluster
- A collection of Nodes
- Containerized applications are deployed ontop of here with a deployment configuration

Master Nodes:
- Hosting the K8s control plane and the management of the of worker nodes
- Decides the most efficient way to distribute your container to nodes

0                   <- Containter
[0, 0]              <- Pod can hold multiple containers
([0, 0], [0, 0])    <- Node can hold multiple pods
{([0, 0], [0, 0])}  <- Cluster can hold multiple nodes



### Kubernetes Commands

To install minikube on MAC

`brew install minikube`

To check the minikube version

`minikube version`

To start a cluster in minikube if you have one built. 

`minikube start`

To check the kubectl version

`kubectl version`

To view your cluster details

`kubectl cluster-info`

To view your running Kubernetes services

`kubectl get services`

To access your cluster

`kubectl get po -A`

To view your pods

`kubectl get pods`

To view nodes in a cluster

`kubectl get nodes`

To access your local kubernetes dashboard

`minikube dashboard`

To create a deployment in minikube

`kubectl create deployment hello-minikube --image=k8s.gcr.io/echoserver:1.4`

To scale your deployment `How many copies of my app`

> Kubernetes will handle distributing the app to the nodes

`kubectl scale deployment hello-minikube --replicas=3`

To scale your deployment `When 80% cpu is utilized Kurbernetes will increase the number of pods`

`autoscale deployment hello-minikube --cpu-percent-80 --min=1 --max=5`

To expose a port for your deployment

`kubectl expose deployment hello-minikube --type=NodePort --port=8080`

To view your deployment in the browser with minikube

`minikube service hello-minikube`

To create loadbalancer deployment

`kubectl create deployment balanced --image=k8s.gcr.io/echoserver:1.4`

To expose the loadbalancer port

`kubectl expose deployment balanced --name=LoadBalancer-Service --type=LoadBalancer --port=8080`

To create a routable IP for the `balanced` deployment

`minikube tunnel`

To get the ip of the lb

`kubectl get services balanced`

To pause kubernetes without stopping your deployed apps

`minikube pause`

To stop kubernetes

`minikube stop`

To delete the minikube VM

`minikube delete`

Increase the deault memory limit (requires a restart)

> These changes will take effect upon a minikube delete and then a minikube start

`minikube config set memory 16384`

Browse the catalog of easy to install Kubernetes services

`minikube addons list`

Create a 2nd cluster running an older version of Kubernetes

`minikube start -p aged --kubernetes-version=v1.16.1`

To delete all running minikube clusters

> Note use `kubectl cluster-info` to verify this

`minikube delete --all`







