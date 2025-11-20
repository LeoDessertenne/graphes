def lirelettre(T, E, a):
    listReadLetter = []
    for transition in T:
        if transition[0] in E and transition[1] == a:
            listReadLetter.append(transition[2])
    return listReadLetter

if __name__ == "__main__":
    pass
