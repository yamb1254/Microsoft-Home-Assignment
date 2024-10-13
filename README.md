
# **Microsoft-Home-Assignment**

## **Overview**


Project Name is a microservice-based web application that fetches real-time Bitcoin prices and displays the latest value along with a 10-minute moving average. It is deployed on a Kubernetes cluster using NGINX as the Ingress controller, with two services:
- Service A: Fetches and displays the Bitcoin price and its 10-minute average.
- Service B: A simple hello-world-style service returning "Hello Microsoft!"


## **Table of Contents**
- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Deployment](#deployment)
- [Usage](#usage)

## **Features**
- **Bitcoin Price Fetcher**: Service A fetches Bitcoin prices from an external API and calculates a 10-minute moving average.
- **Microservice Architecture**: Service A and Service B run as separate microservices, each isolated from the other.
- **Kubernetes Integration**: The app is deployed in a Kubernetes cluster, making it scalable and highly available.
- **Ingress Controller**: NGINX Ingress controller manages routing based on paths `/service-A` and `/service-B`.
- **Service Isolation**: Service A and Service B are restricted from communicating with each other via network policies.

## **Architecture**

The architecture of the project is designed with scalability and modularity in mind:
- **Service A**: Fetches Bitcoin price from an external API every minute.
- **Service B**: A simple service that returns a "Hello Microsoft!" message.
- **Kubernetes**: Both services run in separate pods in a Kubernetes cluster, with NGINX Ingress managing external traffic routing.

Here's a visual diagram of the architecture:
![alt text](<K8Sassigmnet.drawio (1).png>)


## **Getting Started**

### **Prerequisites**
- **Docker**: To build the images for the services.
- **Kubernetes Cluster**: Azure Kubernetes Service (AKS) or any other managed Kubernetes service.
- **kubectl**: To interact with your Kubernetes cluster.
- **Docker Hub**: An account to push Docker images.

### **Installation**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yamb1254/Microsoft-Home-Assignment.git
   cd Microsoft-Home-Assignment
   ```

2. **Build Docker Images**:
   Build the Docker images for Service A and Service B.
   ```bash
   # For Service A
   docker build -t <your-dockerhub-username>/service-a:v1 ./service-a
   
   # For Service B
   docker build -t <your-dockerhub-username>/service-b:v1 ./service-b
   ```

3. **Push Images to Docker Hub**:
   ```bash
   docker push <your-dockerhub-username>/service-a:v1
   docker push <your-dockerhub-username>/service-b:v1
   ```

### **Running the Application**

1. **Deploy to Kubernetes**:
   Deploy the services using the provided YAML files:
   ```bash
   kubectl apply -f k8s/service-a-deployment.yaml
   kubectl apply -f k8s/service-b-deployment.yaml
   kubectl apply -f k8s/ingress.yaml
   kubectl apply -f k8s/network-policy.yaml
   ```

2. **Verify Deployment**:
   Check if the pods are running correctly:
   ```bash
   kubectl get pods
   ```

3. **Access the Services**:
   Once deployed, access the services via the NGINX Ingress controller at:
   - `http://<ingress-ip>/service-A`: Fetches the Bitcoin price and moving average.
   - `http://<ingress-ip>/service-B`: Displays "Hello Microsoft!".

## **Deployment**

### **Using Azure Kubernetes Service (AKS)**

1. **Create an AKS Cluster**:
   Follow these steps to create an AKS cluster with RBAC enabled:
   ```bash
   az aks create --resource-group <resource-group> --name <aks-cluster-name> --enable-rbac
   ```

2. **Deploy to AKS**:
   Ensure that `kubectl` is configured to access your AKS cluster:
   ```bash
   az aks get-credentials --resource-group <resource-group> --name <aks-cluster-name>
   ```

3. **Scale the Cluster**:
   If necessary, you can scale your node pools:
   ```bash
   az aks nodepool scale --resource-group <resource-group> --cluster-name <aks-cluster-name> --nodepool-name <nodepool-name> --node-count 3
   ```

## **Usage**

### **Service A**:
- Fetches the Bitcoin price every minute.
- Outputs the current price and a 10-minute average.
  
You can access the service at `/service-A`.

### **Service B**:
- A simple service that returns "Hello Microsoft!".

You can access the service at `/service-B`.

