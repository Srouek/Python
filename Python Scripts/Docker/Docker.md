# Docker TP

[![Docker](https://github.com/Srouek/Python/blob/main/Python%20Scripts/Docker/asset/Moby-logo.png)](https://www.docker.com/)

**Quickstart Docker** 

## Lancement du premier container
```sh
docker run hello-world
```
Cette commande permet de lancer mon premier container avec son image 
On peut vérifier ce résultat au travers du desktop Docker

![Containers](https://github.com/Srouek/Python/blob/main/Python%20Scripts/Docker/asset/Containers.PNG )
![Containers](https://github.com/Srouek/Python/blob/main/Python%20Scripts/Docker/asset/Containers2.PNG)

L'image
![Image](.\asset\images_docker.PNG)

On peut aussi le voir au travers de sa console Terminal sur Mac ou Powershell sur Windows
![Docker Run](https://github.com/Srouek/Python/blob/main/Python%20Scripts/Docker/asset/Docker_run_Powershell.PNG)

```sh
docker version
```
Permet de connaitre la version de docker utilisé

![Docker_version](https://github.com/Srouek/Python/blob/main/Python%20Scripts/Docker/asset/Docker_version.PNG)

## Petit Résumé des commande docker

```sh
docker ps 
```
Liste tous les containers

```sh
docker create 
```
Crée un nouveau container

```sh
docker run 
```
Crée puis lance un nouveau container run est l'équivalent de create and start

```sh
docker exec
```
Exécute une commande dans un le container en cours d'éxécution 

```sh
docker start
```
Lance un ou plusieurs containers arrêtés

```sh
docker rm
``` 
Supprime un ou plusieurs containers

```sh
docker restart
```
Redémarre un container en cours d’exécution

```sh
docker port
```
Liste les port d'un container

```sh
docker port
```
Liste les ports d'un container

```sh
docker build 
```
Construis une nouvelle image à partir du code source 
```sh
docker pull
```
Récupére une image ou un repository à partir du Docker HUB
```sh
docker push
```
Publie une image ou un repository vers le Docker HUB

```sh
docker images
```
Liste les images (Les info relative aux containers seront aussi affiché)

```sh
docker rmi
```
Supprime une ou plusieurs images

### La Notion de port dans un container
Le port est le point d'entré d'un container, il permet de pouvoir accèder au contenus du container

