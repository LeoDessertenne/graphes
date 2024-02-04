def fact(word):
    """
    Cette fonction calcule les facteurs d'un mot.

    Args:
        word (string): Le mot dont on veut les facteurs.

    Returns:
        list: Les facteurs de  `word`.

    Examples:
        >>> fact("")
        [""]
        >>> fact("test")
        ['', 'est', 'st', 'te', 'es', 'tes', 'test', 's', 'e', 't']
        >>> fact("ab")
        ['', 'a', 'b', 'ab']
    """

    facteurs = set()
    facteurs.add("")
    for i in range(len(word)):
        for j in range(i+1, len(word)+1):
            facteur = word[i:j]
            facteurs.add(facteur)
    return list(facteurs)

    

if __name__ == "__main__":
    print(fact("coucou"))