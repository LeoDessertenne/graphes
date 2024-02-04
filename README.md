# graphes
SAE 2.02 - The aim is to implement a variety of graph-related algorithms.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

Make sure to have Python installed on your machine.

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
