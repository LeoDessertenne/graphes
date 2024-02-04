
def concatene(L1, L2):
    """
    Cette fonction qui concatene qui étant donnés deux langages L1 et L2 renvoie le
    produit de concaténation (sans doublons) de L1 et L2

    Args:
        L1 (list): le premier langage.
        L2 (list): le deuxième langage.

    Returns:
        list: Le produit de la concatenation de  `L1` et `L2`.

    Examples:
        >>> concatene(['aa','ab','ba','bb'], ['a', 'b', ''])
        ['aaa', 'aab', 'aa', 'aba', 'abb', 'ab', 'baa', 'bab', 'ba', 'bba', 'bbb', 'bb']
        >>> concatene([""], [""])
        ['']
    """
        
    lst = []
    for element1 in L1:
        for element2 in L2:
            lst.append(element1+element2)
    return lst

if __name__ == "__main__":
    L1 = ['aa','ab','ba','bb']
    L2 = ['a', 'b', '']
    print(concatene(L1, L2))