# Toyceptron

Toyceptron est un projet pédagogique dont le but est de comprendre le fonctionnement d’un perceptron multi-couches (réseau de neurones simple), sans utiliser de bibliothèques externes comme numpy ou pytorch.

Le projet se concentre uniquement sur la propagation avant (*forward pass*), sans phase d’apprentissage.

---

## Objectif du projet

L’objectif est de construire un réseau de neurones simple afin de comprendre :
- ce qu’est un neurone
- comment fonctionnent les couches
- comment les données circulent dans un réseau
- le rôle des poids, du biais et des fonctions d’activation

---

## Contraintes

- Langage utilisé : Python
- Aucune bibliothèque externe autorisée
- Utilisation de listes Python pour représenter les vecteurs
- Pas d’entraînement du réseau (pas de backpropagation)

---

## Structure du projet

toyceptron/
│
├── neuron.py # Définition d’un neurone
├── layer.py # Définition d’une couche de neurones
├── network.py # Définition du réseau de neurones
├── activation.py # Fonctions d’activation
├── main.py # Fichier de test fourni
└── README.md



---

## Description des fichiers

### `neuron.py`
Contient la classe `Neuron`, qui représente un neurone.
Un neurone calcule une somme pondérée des entrées et ajoute un biais.

### `layer.py`
Contient la classe `Layer`, qui est une collection de neurones.
Chaque neurone d’une couche reçoit le même vecteur d’entrée.

### `network.py`
Contient la classe `Network`, qui permet de créer un réseau composé de plusieurs couches
et d’effectuer une propagation avant complète.

### `activation.py`
Contient des fonctions d’activation simples :
- identité
- seuil
- ReLU

### `main.py`
Fichier de test permettant de vérifier le bon fonctionnement du réseau.

---

## Fonctionnement général

1. Les données d’entrée sont envoyées au réseau
2. Chaque couche applique ses neurones aux données
3. Une fonction d’activation est appliquée après chaque couche
4. La sortie finale est retournée

---

## Exécution

Pour tester le projet (d’exécuter) :

python main.py
