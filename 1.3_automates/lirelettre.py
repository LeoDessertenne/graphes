def lirelettre(T, E, a):
    listReadLetter = list()
    for transition in T:
        if transition[0] == E and transition[1] == a:
            listReadLetter.append(T[2])
    return listReadLetter

if __name__ == "__main__":
    pass