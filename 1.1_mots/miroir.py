
def miroir(word):
    """
    Cette fonction calcule le miroir d'un mot.

    Args:
        word (string): Le mot dont on veut le miroir.

    Returns:
        string: Le mot miroir de  `word`.

    Examples:
        >>> miroir("coucou")
        uocuoc
        >>> miroir("")
    """
        
    word = list(word)
    for i in range(len(word)//2):
        word[i], word[-i-1] = word[-i-1], word[i]
    return "".join(word)


if __name__ == "__main__":
    print(miroir("coucou"))