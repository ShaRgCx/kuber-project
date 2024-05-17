#!/bin/bash

# Сборка образов Docker
docker build -t web-app web_app/.
docker build -t statistics-logger logger/.

# Развертывание ресурсов Kubernetes
kubectl apply -f web_app/deployment-web-app.yaml
kubectl apply -f web_app/service-web-app.yaml
kubectl apply -f logger/deployment-statistics-logger.yaml

#kubectl expose deployment web-app --type=LoadBalancer --port=8080
#kubectl port-forward services/web-app 5000:5000

# Проверка статуса развертывания
kubectl get pods

minikube tunnel
