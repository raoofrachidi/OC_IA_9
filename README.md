# Réalisez une application mobile de recommandation de contenu

My Content est une start-up qui veut encourager la lecture en recommandant des contenus pertinents pour ses utilisateurs.

Vous êtes le CTO et cofondateur de la start-up avec Samia qui est CEO. Vous êtes en pleine construction d’un premier MVP qui prendra la forme d’une application mobile. 

Dans un premier temps, votre start-up souhaite tester une solution de recommandation d’articles et de livres à des particuliers.

Comme vous ne disposez pas à ce jour de données utilisateurs, vous allez utiliser des données disponibles en ligne pour développer votre MVP (https://www.kaggle.com/datasets/gspmoreira/news-portal-user-interactions-by-globocom).

Ces données représentent les interactions des utilisateurs avec les articles disponibles. Elles contiennent des informations sur les articles (par exemple le nombre de mots dans l’article), ainsi que les informations sur les sessions des utilisateurs (par exemple heures de début et de fin) et les interactions des utilisateurs avec les articles (Sur quel article l’utilisateur a-t-il cliqué lors de sa session ?).

En résumé, votre mission est la suivante :

* développer une première version de votre application mobile avec le système de recommandation que vous aurez développé ;
* stocker les scripts développés dans un dossier GitHub ;
* intégrer le système de recommandation à l'application mobile développée par Julien ;
* synthétiser vos premières réflexions sur :
  * l’architecture technique et la description fonctionnelle de votre application mobile à date, et le système de recommandation,
  * l’architecture cible pour pouvoir prendre en compte l’ajout de nouveaux utilisateurs ou de nouveaux articles, que vous présenterez à Samia.

## Livrables 

* L’application mobile complétée avec le système de recommandation en serverless qui recevra en entrée un identifiant utilisateur (et éventuellement l’heure), et retournera les recommandations d’articles associées (par exemple le top 5).
  * Ce livrable permettra de démontrer les fonctionnalités de l’application à Samia et à de futurs utilisateurs.
* Les scripts développés stockés dans un système de gestion de version permettant le déploiement de l’application mobile de bout-en-bout.
  * Ce livrable vous servira à présenter le caractère “industrialisable” de votre travail.
* Un support de présentation contenant une brève description fonctionnelle de l’application, un schéma de l’architecture retenue, une présentation du système de recommandation utilisé et un schéma de l’architecture cible permettant de prendre en compte la création de nouveaux utilisateurs et de nouveaux articles.
  * Ce livrable vous permettra de présenter votre travail à Samia.
