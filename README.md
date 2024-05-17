# kuber-project

## Getting Started
Тестирование производилось с использованием minikube и в некоторой степени опирается на его особенности (такие как minikube tunnel). Для запуска с готовым сервером kubernetes можно воспользоваться kubectl port-forward для получения доступа к серверу с localhost.

```sh
./deploy.sh

minikube service web-app

|-----------|---------|-------------|---------------------------|
| NAMESPACE |  NAME   | TARGET PORT |            URL            |
|-----------|---------|-------------|---------------------------|
| default   | web-app |          80 | http://192.168.49.2:31152 |
|-----------|---------|-------------|---------------------------|
```

Подключение производится по указанному после команды URL.

Для получения данных со статистикой необходимо выполнить команду:

```sh
kubectl get pods

NAME                                 READY   STATUS    RESTARTS   AGE
statistics-logger-6764896d5f-mvbpx   1/1     Running   0          28m
web-app-depl-588f5874b5-fn57f        1/1     Running   0          28m

kubectl cp statistics-logger-***:statistics.json ./statistics.json
```

Где под *** номер, присвоенной поду.
