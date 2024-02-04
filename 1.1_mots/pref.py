
def pref(word):
    """
    Cette fonction calcule les préfixes d'un mot.

    Args:
        word (string): Le mot dont on veut les préfixes.

    Returns:
        list: Les préfixes de  `word`.

    Examples:
        >>> pref("")
        [""]
        >>> pref("test")
        ['', 't', 'te', 'tes', 'test']
        >>> pref("ab")
        ['', 'a', 'ab']
    """
    
    lst = []
    for i in range(len(word)+1):
        lst.append(word[:i])
    return lst


if __name__ == "__main__":
    print(pref("coucou"))