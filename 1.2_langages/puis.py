
def puis(L1):
    """
    Cette fonction puis qui étant donnés un langage L et un entier n renvoie le langage L^n (sans doublons).

    Args:
        L1 (list): langage.

    Returns:
        list: Le produit de la concatenation de  `L1` et `L1`.

    Examples:
        >>> puis(['aa','ab','ba','bb'])
        ['aaaa', 'aaab', 'aaba', 'aabb', 'abaa', 'abab', 'abba', 'abbb', 'baaa', 'baab', 'baba', 'babb', 'bbaa', 'bbab', 'bbba', 'bbbb']
        >>> puis([""])
        
    """
        
    lst = []
    for element1 in L1:
        for element2 in L1:
            lst.append(element1+element2)
    return lst

if __name__ == "__main__":
    L1 = ['aa','ab','ba','bb']
    print(puis(L1))