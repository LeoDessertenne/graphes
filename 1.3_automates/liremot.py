def liremot(T, E, m):
    lst_etat = set()
    for etat in E:
        mot = m
        i = 0
        etat_mot = etat
        while mot != "":
            lettre_actuelle = mot[i]
            for transition in T:
                if transition[0] == etat_mot and transition[1] == lettre_actuelle:
                    etat_mot = transition[2]
                    mot = mot[1:]
        if mot == "":
            lst_etat.add(etat_mot)
    return list(lst_etat)


if __name__ == "__main__":
    pass