
def tousmots(L1, n):
    """
    la fonction  tousmots qui étant donné un alphabet A passé en paramètre
    renvoie la liste de tous les mots de A* de longueur inférieure à n.

    Args:
        L1 (list): langage.
        n (int): longueur inférieur a ce chiffre.

    Returns:
        list: l'étoile de `L1` jusqu'a sa longueur maximum de n.

    Examples:
        >>> tousmots(['aa','ab','ba','bb'], 3)

        >>> tousmots([""])

    """
    if n == 0:
        return ['']
    else:
        mots = set()
        for lettre in L1:
            for mot in tousmots(L1, n-1):
                mots.add(lettre + mot)
        return list(mots.union(tousmots(L1, n-1)))


if __name__ == "__main__":
    L1 = ['a', 'b']
    print(tousmots(L1, 3))
