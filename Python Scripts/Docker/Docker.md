# Docker TP

[![Docker](.\asset\Moby-logo.png)](https://www.docker.com/)

**Quickstart Docker** 

## Lancement du premier container
```sh
docker run hello-world
```
Cette commande permet de lancer mon premier container avec son image 
On peut vérifier ce résultat au travers du desktop Docker

[![Containers](.\asset\Containers.PNG )]
[![Containers](.\asset\Containers2.PNG)]

L'image
[![Image](.\asset\images_docker.PNG)]

On peut aussi le voir au travers de sa console Terminal sur Mac ou Powershell sur Windows
[![Docker Run](.\asset\Docker_run_Powershell.PNG)]

```sh
docker version
```
Permet de connaitre la version de docker utilisé

[![Docker_version](.\asset\Docker_version.PNG)]

##Petit Résumé des commande docker

```sh
docker create 
```
Créer un nouveau conteneur


docker build : Construire une nouvelle image à partir du code source dans le PATH \
docker commit : Créer une nouvelle image à partir des changements d’un conteneur \
docker cp : Copier des fichiers ou des dossiers depuis le PATH d’un conteneur vers le HOSTDIR ou vers STDOUT \

docker history : Afficher l’historique d’une image Docker \
docker images : Lister des images \
docker info : Afficher l’ensemble des informations système \
docker inspect : Afficher les informations de bas niveau sur un conteneur ou une image Docker \
docker kill : Tuer un conteneur en cours d’exécution en utilisant SIGKILL ou un signal spécifié \
docker load : Chargez une image à partir d’une archive tar sur STDIN \
docker logs : Fetch des journaux d’un conteneur \
docker pause : Mettre en pause tous les processus dans un conteneur \
docker port : Liste les ports d’un conteneur, ou rechercher les ports “public” NATé vers un PRIVATE_PORT \
docker ps : Liste de conteneurs \
docker pull : Récupérer une image ou un repository à partir du Docker HUB \
docker push : Publier une image ou un repository vers le Docker HUB \
docker rename : Renommer un conteneur Docker \
docker restart : Redémarrez un conteneur en cours d’exécution \
docker rm : Supprimer une ou plusieurs conteneurs \
docker rmi : Supprimer une ou plusieurs images \
docker run : Exécuter une commande dans un nouveau conteneur \
docker save : Enregistrer une image dans une archive tar (streaming vers STDOUT par défaut) \
docker start : Lancer un ou plusieurs conteneurs arrêtés \
docker stats : Afficher l’utilisation des ressources d’un ou plusieurs conteneurs sous la forme d’un flux \
docker stop : Arrêtez un conteneur en cours d’exécution en envoyant SIGTERM et SIGKILL après une période de grâce \