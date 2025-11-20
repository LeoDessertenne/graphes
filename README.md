# graphes
SAE 2.02 - The aim is to implement a variety of graph-related algorithms.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

Make sure to have Python installed on your machine and you can run the script

## Usage
You can create new variables to build your automaton using the following format:
```py
automate = {
        "alphabet": ['a', 'b'], # your alphabet
        "etats": [1, 2, 3, 4], # your statuses
        "transitions": [[1, 'a', 2], [2, 'a', 2], [2, 'b', 3], [3, 'a', 4]], # your states [start state, 'letter', end state]...
        "I": [1], # initial states
        "F": [4] # final states
    } 
```


- Correction des fonctions de lecture d'automate : `lirelettre` renvoie désormais les états atteignables, `liremot` consomme le mot tout en arrêtant proprement quand aucune transition ne correspond.
- Produit d'automates revu pour gérer toutes les paires d'états et les transitions manquantes, évitant les erreurs de déballage.
- Ajout de tests unitaires (`tests/test_automates.py`) couvrant `lirelettre` et `liremot` sur des automates simples.
