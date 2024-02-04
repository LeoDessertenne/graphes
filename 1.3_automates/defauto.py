
def defauto() :
    """
    cette fonction permet de faire la saisie d'un automate.

    Args:
        none

    Returns:
        dictionnary : the automate that you just filled out
    """

    auto = {
        "alphabet": ['a', 'b'],
        "etats": list(),
        "transitions": list(),
        "I": list(),
        "F": list()
    }

    auto["etats"] = [i for i in range(1, int(input("Combien d'états : "))+1)]

    nb_etats_i = int(input("Combien d'états initiaux : "))
    while nb_etats_i > len(auto["etats"]) or  nb_etats_i < 0:
        nb_etats_i = int(input("Il ne peut pas y avoir ce nombre d'états intitiaux entrez un nouveau : "))

    for i in range(nb_etats_i) :
        etat_i = int(input("Entrez un état initial : "))
        if etat_i in auto["etats"] :
            if etat_i not in auto["I"]:
                auto["I"].append(etat_i)
        else :
            print("Cet état n'existe pas Veuillez entrer un état qui existe entre 0 et ", len(auto["etats"]))
            i -= 1

    nb_etats_f = int(input("Combien d'états finaux : "))
    while nb_etats_f > len(auto["etats"]) or  nb_etats_f < 0:
            nb_etats_f = int(input("Il ne peut pas y avoir ce nombre d'états finals entrez un nouveau : "))
    for i in range(nb_etats_f) :
        etat_f = int(input("Entrez un état final : "))
        if etat_f in auto["etats"] :
            if etat_f not in auto["F"]:
                auto["F"].append(etat_f)
        else :
            print("Cet état n'existe pas Veuillez entrer un état qui existe entre 0 et ", len(auto["etats"]))
            i -= 1

    com = 0
    while com != (len(auto["etats"])**len(auto["alphabet"])):
        transition = input("Entrer votre transition avec des virgule entre elle (-1 si vous avez fini): ")
        if transition == "-1":
            break
        liste = transition.split(",")
        nouvelle_liste = []
        for element in liste:
            element = element.strip() # supprime les espaces en début et fin de l'élément
            if element.isnumeric(): # vérifie si l'élément est numérique
                nouvelle_liste.append(int(element))
            else:
                nouvelle_liste.append(element)
        if nouvelle_liste not in auto["transitions"]:
            if nouvelle_liste[0] in auto["etats"] and nouvelle_liste[1] in auto["alphabet"] and nouvelle_liste[2] in auto["etats"]:
                auto["transitions"].append(nouvelle_liste)
                com += 1
            else :
                print("pas valide")
        else :
            print("existe deja ")



    print(auto["alphabet"])
    print(auto["etats"])
    print(auto["transitions"])
    print(auto["I"])
    print(auto["F"])
    return auto

if __name__ == "__main__":
    defauto()
