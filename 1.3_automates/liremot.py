def liremot(T, E, m):
    lst_etat = set()
    for etat in E:
        etat_mot = etat
        mot_rest = m
        while mot_rest:
            lettre_actuelle = mot_rest[0]
            transition_trouvee = False
            for transition in T:
                if transition[0] == etat_mot and transition[1] == lettre_actuelle:
                    etat_mot = transition[2]
                    mot_rest = mot_rest[1:]
                    transition_trouvee = True
                    break
            if not transition_trouvee:
                break
        if mot_rest == "":
            lst_etat.add(etat_mot)
    return list(lst_etat)


if __name__ == "__main__":
    pass
