
def suf(word):
    """
    Cette fonction calcule les suffixes d'un mot.

    Args:
        word (string): Le mot dont on veut les suffixes.

    Returns:
        list: Les suffixes de  `word`.

    Examples:
        >>> suf("")
        [""]
        >>> suf("test")
        ['test', 'est', 'st', 't', '']
        >>> suf("ab")
        ['ab', 'b', '']
    """
    
    lst = []
    for i in range(len(word)+1):
        lst.append(word[i:])
    return lst


if __name__ == "__main__":
    print(suf("coucou"))