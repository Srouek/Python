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

![Image](https://github.com/Srouek/Python/blob/main/Python%20Scripts/Docker/asset/images_docker.PNG)

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

### Les containers
Ce sont des environnement Linux que l'on isole les uns des autres, mais qui s'appuis sur l'OS (le système d'exploitation) de la machine où il se trouve.
> *Sur des environnement Linux oui, mais depuis 2016  il possible d'exéuter des containers Windows grâce à **Hyper-V Containers** mais aussi des container Linux grâce à la virtualisation proposée par **Hyper-V** sur Windows. C'est d'ailleurs surement pour ça que les développeurs ne mentionnent plus la restrictions qu'avait les containers Docker*
#### L'utilité
> Si vous  êtes fan de Marvel, vous connaissez surement Iron man.
> Tony Stark pourrait être comparé à l'Os de notre machine et les armures de Tony Stark (oui il en a plusieurs) serait les containers.
> Selon l'utilité Tony appel différentes armure parfois il en appel plusieurs afin de pouvoir combattre sur tous les fronts.

La conteneurisation c'est le même principe, on pourrait se dire que chaque armure est une application avec une base de donnée et des librairies auquel on aimerait faire appel à tout moment.
Mais en réalité ça peut aller plus loin que ça on pourrait conteurisé  des librairies, des applications, des base de donnée et faire appel à chaque conteneurs au sein d'un gros conteneur qui réccuperera le tout. Tout comme Tony Stark pourrais assembler différente pièces des ses armures comme bon lui semble pour en fabriquer une voir même plusieurs.

Mais cela n'est pas le seul avantage. La conteurisation permet au Administrateur système de n'avoir à récupérer que le conteur que l'on décide de déployer sur un serveur et avoir toutes nos dépendances. En effet Un projet fait en python 3.2 avec une db Mango nécéssitera l'installation de ses logiciels et de leurs environnements et cela sur chaque serveur que l'on souhaitera utiliser. 

Encore un avantage Les conteuneur peuvent exiter sur un serveur et être éxécuter par un autre serveur et cela grâce au fonctionnement de docker qui fonctionne en client serveur avec comme client le `Docker client` et comme serveur `Docker Deamon` qui lui fait fonctionner le `Docker Engine`

#### Le fonctionnement
Le **conteneur**
Les **images** 
Le **port** est le point d'entré d'un container, il permet de pouvoir accèder au contenus du container

