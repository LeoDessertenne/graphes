import copy


def fact(word):
    """
    Cette fonction calcule les facteurs d'un mot.

    Args:
        word (string): Le mot dont on veut les facteurs.

    Returns:
        list: Les facteurs de  `word`.

    Examples:
        >>> fact("")
        [""]
        >>> fact("test")
        ['', 'est', 'st', 'te', 'es', 'tes', 'test', 's', 'e', 't']
        >>> fact("ab")
        ['', 'a', 'b', 'ab']
    """

    facteurs = set()
    facteurs.add("")
    for i in range(len(word)):
        for j in range(i+1, len(word)+1):
            facteur = word[i:j]
            facteurs.add(facteur)
    return list(facteurs)


def mir(word):
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


def puis(L1, n):
    """
    Cette fonction puis qui étant donnés un langage L et un entier n renvoie le langage L^n (sans doublons).

    Args:
        L1 (list): langage.

    Returns:
        list: Le produit de la concatenation de  `L1` et `L1`.

    Examples:
        >>> puis(['aa','ab','ba','bb'], 2)
        ['aaaa', 'aaab', 'aaba', 'aabb', 'abaa', 'abab', 'abba', 'abbb', 'baaa', 'baab', 'baba', 'babb', 'bbaa', 'bbab', 'bbba', 'bbbb']
        >>> puis([""])

    """
    if n == 0:
        return ['']
    else:
        L_n_1 = puis(L1, n - 1)
        L_n = []
        for mot in L1:
            for mot_n_1 in L_n_1:
                nouveau_mot = mot + mot_n_1
                if nouveau_mot not in L_n:
                    L_n.append(nouveau_mot)
        return L_n

# 1.2.3
# La raison en est que l'ensemble des langages est infini, et certains de ces langages sont indécidables,
# c'est-à-dire qu'il n'y a pas de méthode algorithmique qui puisse déterminer si une chaîne donnée
# appartient ou non au langage.


def tousmots(L1, n):
    """
    la fonction  tousmots qui étant donné un alphabet A passé en paramètre
    renvoie la liste de tous les mots de A* de longueur inférieure à n.

    Args:
        L1 (list): langage.
        n (int): longueur inférieur a ce chiffre.

    Returns:
        list: l'étoile de `L1` jusqu'a sa longueur maximum de n.

    Examples:
        >>> tousmots(['aa','ab','ba','bb'], 3)

        >>> tousmots([""])

    """
    if n == 0:
        return ['']
    else:
        mots = set()
        for lettre in L1:
            for mot in tousmots(L1, n-1):
                mots.add(lettre + mot)
        return list(mots.union(tousmots(L1, n-1)))


def defauto():
    """
    cette fonction permet de faire la saisie d'un automate.

    Args:


    Returns:
        dictionnary : the automate that you just filled out
    """

    automate = {
        "alphabet": ['a', 'b'],
        "etats": list(),
        "transitions": list(),
        "I": list(),
        "F": list()
    }

    automate["etats"] = [i for i in range(int(input("Combien d'états : ")))]

    nb_etats_i = int(input("Combien d'états initiaux : "))
    while nb_etats_i > len(automate["etats"]) or nb_etats_i < 0:
        nb_etats_i = int(
            input("Il ne peut pas y avoir ce nombre d'états intitiaux entrez un nouveau : "))

    for i in range(nb_etats_i):
        etat_i = int(input("Entrez un état initial : "))
        if etat_i in automate["etats"]:
            if etat_i not in automate["I"]:
                automate["I"].append(etat_i)
        else:
            print("Cet état n'existe pas Veuillez entrer un état qui existe entre 0 et ", len(
                automate["etats"]))
            i -= 1

    nb_etats_f = int(input("Combien d'états finaux : "))
    while nb_etats_f > len(automate["etats"]) or nb_etats_f < 0:
        nb_etats_f = int(
            input("Il ne peut pas y avoir ce nombre d'états finals entrez un nouveau : "))
    for i in range(nb_etats_f):
        etat_f = int(input("Entrez un état final : "))
        if etat_f in automate["etats"]:
            if etat_f not in automate["F"]:
                automate["F"].append(etat_f)
        else:
            print("Cet état n'existe pas Veuillez entrer un état qui existe entre 0 et ", len(
                automate["etats"]))
            i -= 1

    com = 0
    while com != (len(automate["etats"]) ** len(automate["alphabet"])):
        transition = input(
            "Entrer votre transition avec des virgule entre elle (-1 si vous avez fini): ")
        if transition == "-1":
            break
        liste = transition.split(",")
        nouvelle_liste = []
        for element in liste:
            element = element.strip()  # supprime les espaces en début et fin de l'élément
            if element.isnumeric():  # vérifie si l'élément est numérique
                nouvelle_liste.append(int(element))
            else:
                nouvelle_liste.append(element)
        if nouvelle_liste not in automate["transitions"]:
            if nouvelle_liste[0] in automate["etats"] and nouvelle_liste[1] in automate["alphabet"] and nouvelle_liste[2] in automate["etats"]:
                automate["transitions"].append(nouvelle_liste)
                com += 1
            else:
                print("pas valide")
        else:
            print("existe deja ")

    return automate


def lirelettre(T, E, a):
    """
    La fonctions lirelettre qui étant donner une liste de transition une liste 
    d'états et une lettre renvoie la liste des états dans lesquels on peut arriver en partant 
    d'un état de E en lisant la lettre de a

    Args:
        T (list): transitions.
        E (list): états.
        a (character) lettre.

    Returns:
        list: liste des états dans lesquels on peut arriver.

    Examples:
        >>> lirelettre(auto["transitions"],auto["etats"],'a')
        [2, 4]

    """
    listReadLetter = []
    for transition in T:
        if transition[0] in E and transition[1] == a:
            listReadLetter.append(transition[2])

    return listReadLetter


def liremot(T, E, m):
    """
    La fonctions liremot qui étant donner une liste de transition une liste 
    d'états et un mot renvoie la liste des états dans lesquels on peut arriver en partant 
    d'un état de E en lisant le mot m

    Args:
        T (list): transitions.
        E (list): états.
        m (string) mot.

    Returns:
        list: liste des états dans lesquels on peut arriver.

    Examples:
        >>> liremot(auto["transitions"],auto["etats"],'aba')
        [4]

    """
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


def accepte(auto, mot):
    """
    La fonction accepte qui prend en paramètres un automate et un mot m et
    renvoie True si le mot m est accepté par l'automate.

    Args:
        auto (dictionnaire): automate.
        mot (string) mot.

    Returns:
        boolean: si le mot est accepté par le langage ou pas.

    Examples: avec un automate acceptant a^+ba
        >>> accepte(auto, 'aba') 
        Ture

    """
    for etat in auto["I"]:
        mot_tmp = mot
        i = 0
        etat_mot = etat
        lst_transi = set()
        while mot != "" and len(lst_transi) < len(auto["etats"]):
            lettre_actuelle = mot[i]
            for transition in auto["transitions"]:
                if transition[0] == etat_mot and transition[1] == lettre_actuelle:
                    etat_mot = transition[2]
                    mot = mot[1:]
                    break
                lst_transi.add(auto["transitions"].index(transition))
        if mot == "" and etat_mot in auto["F"]:
            return True
    return False


def langage_accept(automate, n):
    """
    Cette fonction permet de générer la liste des mots de longueur n acceptés par un automate.

    Args:
        automate (dict): l'automate à utiliser sous forme de dictionnaire.
        n (int): la longueur des mots à générer.

    Returns:
        list: une liste contenant tous les mots de longueur n acceptés par l'automate.
    """
    # Initialisation de la liste des mots acceptés
    mots = []
    mots_valide = []

    def generate_words(n, current_word="", mots=[]):
        if len(current_word) == n:
            mots.append(current_word)
            return
        generate_words(n, current_word + 'a', mots)
        generate_words(n, current_word + 'b', mots)

    generate_words(n, "", mots)

    for mot in mots:
        if accepte(automate, mot):
            mots_valide.append(mot)

    return mots_valide

# 1.3.6 On ne peut pas faire une fonction qui renvoie le langage accepté par un automate car il existe
# des langages qui sont infinis et donc il n'est pas possible d'énumérer tous les mots de ce langage.
#  De plus, même si le langage est fini, il peut être très grand, ce qui le rendrait impraticable à
# énumérer.


def deterministe(automate):
    """
    Vérifie si un automate est déterministe, c'est-à-dire s'il n'y a pas de deux transitions sortant d'un même état 
    avec le même symbole, et s'il y a une transition pour chaque symbole de l'alphabet sortant de chaque état.

    Args:
        automate (dict): un automate au format dict avec les clés "etats", "alphabet", "transitions", "I", et "F".

    Returns:
        bool: True si l'automate est déterministe, False sinon.
    """
    # On vérifie si chaque transition est unique
    transitions = set()
    for transition in automate["transitions"]:
        if (transition[0], transition[1]) in transitions:
            return False
        transitions.add((transition[0], transition[1]))

    # On vérifie si chaque état a une transition pour chaque symbole de l'alphabet
    for etat in automate["etats"]:
        transitions_etat = set()
        for transition in automate["transitions"]:
            if transition[0] == etat:
                transitions_etat.add(transition[1])
        if transitions_etat != set(automate["alphabet"]):
            return False

    # L'automate est déterministe
    return True


def determinise(auto):
    """
    Déterminise l'automate passé en paramètre.

    Args:
        auto (dict): l'automate à déterminiser.

    Returns:
        dict: l'automate déterminisé.
    """
    # Initialisation de l'automate déterminisé
    auto_det = {"alphabet": auto["alphabet"],
                "etats": [], "transitions": [], "I": [], "F": []}
    etats_initiaux = auto["I"]
    etats_finaux = auto["F"]
    etats_traites = []
    etats_a_traiter = [etats_initiaux]

    # Traitement des états
    while etats_a_traiter:
        # Création de l'état courant représentant l'ensemble d'états
        etat_courant = sorted(etats_a_traiter.pop())
        if etat_courant in etats_traites:
            continue

        # Ajout de l'état courant à l'automate déterminisé
        auto_det["etats"].append(etat_courant)
        etats_traites.append(etat_courant)

        # Vérification si l'état courant est final
        if any(e in etat_courant for e in etats_finaux):
            auto_det["F"].append(etat_courant)

        # Ajout de l'état courant comme état initial si nécessaire
        if etat_courant == etats_initiaux:
            auto_det["I"].append(etat_courant)

        # Traitement des transitions
        for symbole in auto["alphabet"]:
            nouvel_etat = []
            for e in etat_courant:
                for transition in auto["transitions"]:
                    if transition[0] == e and transition[1] == symbole:
                        nouvel_etat.append(transition[2])
            if nouvel_etat:
                nouvel_etat = sorted(list(set(nouvel_etat)))
                auto_det["transitions"].append(
                    [etat_courant, symbole, nouvel_etat])
                if nouvel_etat not in etats_a_traiter and nouvel_etat not in etats_traites:
                    etats_a_traiter.append(nouvel_etat)

    return auto_det


def renommage(auto):
    """
    Cette fonction renomme les états d'un automate, de façon à ce qu'ils soient des entiers consécutifs
    de 0 à n-1, où n est le nombre d'états de l'automate. Elle retourne une nouvelle représentation de l'automate
    avec les nouveaux états renommés.

    Args:
        auto (dict): L'automate à renommer, sous forme d'un dictionnaire contenant les clés "alphabet", "etats",
                     "transitions", "I" et "F".

    Returns:
        dict: Une nouvelle représentation de l'automate, avec les états renommés.
    """
    ancien_etats = auto["etats"]
    nouveau_etats = list(range(0, len(auto["etats"])))
    ancien_I = auto["I"]
    nouveau_I = []
    for i in range(len(ancien_etats)):
        if ancien_etats[i] in ancien_I:
            nouveau_I.append(nouveau_etats[i])

    ancien_F = auto["F"]
    nouveau_F = []
    for i in range(len(ancien_etats)):
        if ancien_etats[i] in ancien_F:
            nouveau_F.append(nouveau_etats[i])

    ancien_transition = auto["transitions"]
    nouveau_transitions = []
    for transition in ancien_transition:
        transition_act = []
        for i in range(len(ancien_etats)):
            if ancien_etats[i] == transition[0]:
                transition_act.append(nouveau_etats[i])
        for i in range(len(ancien_etats)):
            if ancien_etats[i] == transition[2]:
                transition_act.append(transition[1])
                transition_act.append(nouveau_etats[i])
        nouveau_transitions.append(transition_act)

    new_auto = {
        "alphabet": auto["alphabet"],
        "etats": nouveau_etats,
        "transitions": nouveau_transitions,
        "I": nouveau_I,
        "F": nouveau_F
    }

    return new_auto


def complet(automate):
    """
    Vérifie si un automate est complet.

    Args:
        automate (dict): Un automate.

    Returns:
        bool: True si l'automate est complet, False sinon.
    """
    for etat in automate["etats"]:
        res = 0
        for transition in automate["transitions"]:
            if (transition[1] == "a" and transition[0] == etat):
                res += 1
            if (transition[1] == "b" and transition[0] == etat):
                res += 1
        if res != 2:
            return False
    return True


def complete(automate):
    """
    Complète un automate.

    Args:
        automate (dict): Un automate.

    Returns:
        dict: Un automate complet.
    """
    auto_copy = copy.deepcopy(automate)
    if not complet(auto_copy):
        auto_copy["etats"].append(auto_copy["etats"][-1]+1)
        for etat in auto_copy["etats"]:
            res = []
            for transition in auto_copy["transitions"]:
                if (transition[1] == "a" and transition[0] == etat):
                    res.append("a")
                if (transition[1] == "b" and transition[0] == etat):
                    res.append("b")
            if len(res) != 2:
                lettres = []
                if "a" not in res:
                    lettres.append("a")
                if "b" not in res:
                    lettres.append("b")
                for lettre in lettres:
                    auto_copy["transitions"].append(
                        [etat, lettre, auto_copy["etats"][-1]])
    return auto_copy


def complement(automate):
    """
    Calcule le complément d'un automate.

    Args:
        automate (dict): Un automate.

    Returns:
        dict: L'automate qui reconnaît le complément du langage de l'automate en entrée.
    """
    auto_copy = copy.deepcopy(automate)
    auto_copy = renommage(determinise(auto_copy))
    auto_copy = complete(auto_copy)
    F = auto_copy["F"].copy()
    auto_copy["F"].clear()
    for etat in auto_copy["etats"]:
        if etat not in F:
            auto_copy["F"].append(etat)
    return auto_copy


def prefixe(automate):
    """
    Renvoie un automate acceptant l'ensemble des préfixes du langage accepté
    par l'automate donné en entrée.

    Paramètres :
    - automate : un dictionnaire représentant un automate émondé

    Retour :
    - un dictionnaire représentant l'automate acceptant l'ensemble des préfixes
      du langage accepté par l'automate donné en entrée
    """
    auto_copy = copy.deepcopy(automate)
    auto_copy["F"] = auto_copy["etats"].copy()
    return auto_copy


def suffixe(automate):
    """
    Renvoie un automate acceptant l'ensemble des suffixes du langage accepté
    par l'automate donné en entrée.

    Paramètres :
    - automate : un dictionnaire représentant un automate émondé

    Retour :
    - un dictionnaire représentant l'automate acceptant l'ensemble des suffixes
      du langage accepté par l'automate donné en entrée
    """
    auto_copy = copy.deepcopy(automate)
    auto_copy["I"] = auto_copy["etats"].copy()
    return auto_copy


def facteur(automate):
    """
    Renvoie un automate acceptant l'ensemble des facteurs du langage accepté
    par l'automate donné en entrée.

    Paramètres :
    - automate : un dictionnaire représentant un automate émondé

    Retour :
    - un dictionnaire représentant l'automate acceptant l'ensemble des facteurs
      du langage accepté par l'automate donné en entrée
    """
    auto_copy = copy.deepcopy(automate)
    auto_copy["I"] = auto_copy["etats"].copy()
    auto_copy["F"] = auto_copy["etats"].copy()
    return auto_copy


def miroir(automate):
    """
    Renvoie l'automate miroir de l'automate donné en entrée.
     ,
    Paramètres :
    - automate : un dictionnaire représentant un automate émondé

    Retour :
    - un dictionnaire représentant l'automate miroir de l'automate donné en entrée
    """
    auto_copy = copy.deepcopy(automate)
    initiaux = auto_copy["I"].copy()
    auto_copy["I"] = auto_copy["F"].copy()
    auto_copy["F"] = initiaux
    for transition in auto_copy["transitions"]:
        fin = transition[2]
        transition[2] = transition[0]
        transition[0] = fin
    return auto_copy


def minimise(automate):
    """
    Renvoie l'automate minimiser de l'automate donné en entrée.
     ,
    Paramètres :
    - automate : un dictionnaire représentant un automate

    Retour :
    - un dictionnaire représentant l'automate minimiser de l'automate donné en entrée
    """
    auto_copy = {
        "alphabet": ['a', 'b'],
        "etats": [],
        "transitions": [],
        "I": [],
        "F": []
    }
    classe0 = normalisation_classe(Classe0(automate))
    classe1 = normalisation_classe(Classe1(automate))
    egal = check_classe(classe0, classe1)
    if egal == True:
        auto_copy = minimise_rassembler(automate, classe1)
    else:
        nouvelle = classe1
        while True:
            ancienne = nouvelle.copy()
            nouvelle = normalisation_classe(Classe2(automate, classe1))
            if check_classe(nouvelle, ancienne):
                auto_copy = minimise_rassembler(automate, nouvelle)
                break

    return auto_copy


def Classe2(automate, classe):
    """
    Renvoie la classe de niveau 2 et plus de l'automate donné en entrée.
     ,
    Paramètres :
    - automate : un dictionnaire représentant un automate
    - classe : classe de niveau 1

    Retour :
    - la classe au degré maximum de séparation des classes
    """
    # regler problème quand il en reste plus qu'un
    new_classe = []
    for etat in classe:

        classe_inter = []
        while etat != []:
            if len(etat) == 1:
                if etat not in new_classe:
                    new_classe.append(etat)
                    break
            premiers = etat[:2]
            etat1 = Etat_a_b(automate, premiers[0])
            etat1_1 = Etat_a_b(automate, etat1[1])
            etat1_2 = Etat_a_b(automate, etat1[2])
            com1_1 = calcul_com(automate, etat1_1)
            com1_2 = calcul_com(automate, etat1_2)
            etat2 = Etat_a_b(automate, premiers[1])
            etat2_1 = Etat_a_b(automate, etat2[1])
            etat2_2 = Etat_a_b(automate, etat2[2])
            com2_1 = calcul_com(automate, etat2_1)
            com2_2 = calcul_com(automate, etat2_2)
            if com1_1 != com2_1 or com1_2 != com2_2:
                new_classe.append([premiers[0]])
            else:
                if len(etat) == 2:
                    classe_inter.append(premiers[0])
                    classe_inter.append(premiers[1])
                    etat = etat[2:]
                    break
                else:
                    classe_inter.append(premiers[0])

            etat = etat[1:]

        new_classe.append(classe_inter)
    return new_classe


def Etat_a_b(automate, etat_cible):
    """
    Renvoie l'état de a et de l'etat vers les chemin avec un a et un b
     ,
    Paramètres :
    - automate : un dictionnaire représentant un automate
    - etat_cible : etat que vous voulez cibler

    Retour :
    - une liste composée de l'état et de l'etat vers les chemin avec un a et un b
    """
    # Savoir le com d'un etat de la forme [etat, etat_a, etat_b]
    for etat in automate["etats"]:
        if etat == etat_cible:
            liste_inter = [etat]
            com = 0
            for transition in automate["transitions"]:
                if com == 0:
                    if transition[0] == etat and transition[1] == "a":
                        liste_inter.append(transition[2])
                        com += 1
                if com == 1:
                    if transition[0] == etat and transition[1] == "b":
                        liste_inter.append(transition[2])
                        break
            return liste_inter


def calcul_com(automate, etat_a_b):
    """
    Renvoie un compteur pour voir si les etat sont dans la meme classe d'équivalence 
     ,
    Paramètres :
    - automate : un dictionnaire représentant un automate
    - etat_a_b : 

    Retour :
    - liste composée de l'état et de l'etat vers les chemin avec un a et un b
    """
    com = [0, 0, 0]
    if etat_a_b[0] in automate["F"]:
        com[0] += 1
    if etat_a_b[1] in automate["F"]:
        com[1] += 1
    if etat_a_b[2] in automate["F"]:
        com[2] += 1
    return com


def minimise_rassembler(automate, classe):
    """
    Renvoie un automate avec les transitions qui sont dans le meme groupe d'équivalence
     ,
    Paramètres :
    - automate : un dictionnaire représentant un automate
    - classe : la classe d'équivalence de l'automate

    Retour :
    - automate minmisé 
    """
    auto_copy = {
        "alphabet": ['a', 'b'],
        "etats": [],
        "transitions": [],
        "I": [],
        "F": []
    }
    # voir si un etat est final
    for etat in classe:
        etat_set = set(etat)
        set_f = set(automate["F"])
        if etat_set <= set_f:
            auto_copy["F"].append(list(etat_set))
    auto_copy["I"] = automate["I"]
    auto_copy["etats"] = classe
    for etat_min in classe:
        for transition in automate["transitions"]:
            if transition[0] in etat_min:
                for liste in classe:
                    if transition[2] in liste:
                        transitionGroupe2 = liste
                    if transition[0] in liste:
                        transitionGroupe0 = liste
                if [transitionGroupe0, transition[1], transitionGroupe2] not in auto_copy["transitions"]:
                    auto_copy["transitions"].append(
                        [transitionGroupe0, transition[1], transitionGroupe2])
    return auto_copy


def Classe0(automate):
    """
    Renvoie la classe d'équivalence 0
     ,
    Paramètres :
    - automate : un dictionnaire représentant un automate

    Retour :
    - classe d'équivalence 0 
    """
    liste = []
    for etat in automate["etats"]:
        if etat not in automate["F"]:
            liste.append(etat)
    classe0 = [liste, automate["F"]]
    return classe0


def Classe1(automate):
    """
    Renvoie la classe d'équivalence 1
     ,
    Paramètres :
    - automate : un dictionnaire représentant un automate

    Retour :
    - classe d'équivalence 1
    """
    # avoir une srtucture du type [etat ,transition avec a, transition avec b]
    etat_a_b = []
    for etat in automate["etats"]:
        liste_inter = [etat]
        com = 0
        for transition in automate["transitions"]:
            if com == 0:
                if transition[0] == etat and transition[1] == "a":
                    liste_inter.append(transition[2])
                    com += 1
            if com == 1:
                if transition[0] == etat and transition[1] == "b":
                    liste_inter.append(transition[2])
                    break
        etat_a_b.append(liste_inter)
    # construction de la classe de niveau 1
    classe1 = [[], [], [], [], [], [], [], [], [], []]
    for etats in etat_a_b:
        com = [0, 0, 0]
        print(etats)
        if etats[0] in automate["F"]:
            com[0] += 1
        if etats[1] in automate["F"]:
            com[1] += 1
        if etats[2] in automate["F"]:
            com[2] += 1

        if com == [1, 1, 1]:
            classe1[9].append(etats[0])
        elif com == [0, 1, 1]:
            classe1[8].append(etats[0])
        elif com == [1, 0, 1]:
            classe1[7].append(etats[0])
        elif com == [1, 0, 0]:
            classe1[6].append(etats[0])
        elif com == [0, 1, 1]:
            classe1[5].append(etats[0])
        elif com == [1, 1, 0]:
            classe1[4].append(etats[0])
        elif com == [0, 0, 1]:
            classe1[3].append(etats[0])
        elif com == [0, 1, 0]:
            classe1[2].append(etats[0])
        elif com == [0, 0, 0]:
            classe1[0].append(etats[0])
    return classe1


def normalisation_classe(classe):
    """
    Renvoie la classe sans les listes vides
     ,
    Paramètres :
    - list : classe d'équivalence de n'importe quel rang

    Retour :
    - classe d'équivalence sans liste vide
    """
    classe_temp = []
    for liste in classe:
        if liste != []:
            classe_temp.append(liste)
    return classe_temp


def check_classe(classe0, classe1):
    """
    Renvoie un booléen pour voir si les deux classses sont équivalentes
     ,
    Paramètres :
    - classe d'équivalence 1    
    - classe d'équivalence 2

    Retour :
    - le booléen qui dit si les deux listes sont égales
    """
    if len(classe0) != len(classe1):
        return False
    set_classe0 = set()
    set_classe1 = set()
    for liste in classe0:
        set_classe0.add(frozenset(liste))
    for liste in classe1:
        set_classe1.add(frozenset(liste))
    if set_classe0 == set_classe1:
        return True
    return False


def produit(automate1, automate2):
    """Calcule le produit de deux automates.

    Args:
    - automate1 (dict): un dictionnaire représentant un automate
    - automate2 (dict): un dictionnaire représentant un automate de la même manière que `automate1`.

    Returns:
    Un dictionnaire représentant l'automate produit de `automate1` et `automate2`
    """
    auto_copy = {
        "alphabet": ['a', 'b'],
        "etats": [],
        "transitions": [],
        "I": [],
        "F": []
    }
    # Toutes les combinaisons d'états initiaux des deux automates.
    initial_pairs = [(i1, i2) for i1 in automate1["I"] for i2 in automate2["I"]]
    auto_copy["I"].extend(initial_pairs)
    auto_copy["etats"].extend(initial_pairs)

    a_traiter = list(initial_pairs)
    while a_traiter:
        etat1, etat2 = a_traiter.pop(0)
        for symbole in auto_copy["alphabet"]:
            dest1 = [t[2] for t in automate1["transitions"] if t[0] == etat1 and t[1] == symbole] or [-1]
            dest2 = [t[2] for t in automate2["transitions"] if t[0] == etat2 and t[1] == symbole] or [-1]
            for d1 in dest1:
                for d2 in dest2:
                    nouvel_etat = (d1, d2)
                    if nouvel_etat not in auto_copy["etats"]:
                        auto_copy["etats"].append(nouvel_etat)
                        a_traiter.append(nouvel_etat)
                    transition = [(etat1, etat2), symbole, nouvel_etat]
                    if transition not in auto_copy["transitions"]:
                        auto_copy["transitions"].append(transition)

    return auto_copy


def inter(automate1, automate2):
    """
    Calcule l'intersection de deux automates deterministes.

    Args:
        automate1 (dict): Le premier automate, sous forme d'un dictionnaire contenant les clés "alphabet", "etats",
                          "transitions", "I" et "F".
        automate2 (dict): Le second automate, sous forme d'un dictionnaire contenant les clés "alphabet", "etats",
                          "transitions", "I" et "F".

    Returns:
        dict: Une nouvelle représentation de l'automate qui est l'intersection de `automate1` et `automate2`, avec
              les états renommés. Le résultat est un dictionnaire avec les clés "alphabet", "etats", "transitions",
              "I" et "F".
    """
    automate1 = complete(automate1)
    automate2 = complete(automate2)
    auto_copy = produit(automate1, automate2)
    etat_finaux = []
    for etat in auto_copy["etats"]:
        if etat[0] in automate1["F"] and etat[1] in automate2["F"]:
            etat_finaux.append(etat)
    auto_copy["F"] = etat_finaux
    return auto_copy


def difference(automate1, automate2):
    """
    Calcule la différence entre deux automates `automate1` et `automate2`.

    Args:
        automate1 (dict): Le premier automate, représenté sous forme d'un dictionnaire avec les clés "alphabet",
            "etats", "transitions", "I" et "F".
        automate2 (dict): Le deuxième automate, représenté sous forme d'un dictionnaire avec les clés "alphabet",
            "etats", "transitions", "I" et "F".

    Returns:
        dict: Un nouvel automate représentant la différence entre `automate1` et `automate2`.
    """
    automate1 = complete(automate1)
    automate2 = complete(automate2)
    auto_copy = produit(automate1, automate2)
    etat_finaux = []
    for etat in auto_copy["etats"]:
        if etat[0] in automate1["F"] and etat[1] not in automate2["F"]:
            etat_finaux.append(etat)
    auto_copy["F"] = etat_finaux
    return auto_copy


if __name__ == "__main__":
    auto = {
        "alphabet": ['a', 'b'],
        "etats": [1, 2, 3, 4],
        "transitions": [[1, 'a', 2], [2, 'a', 2], [2, 'b', 3], [3, 'a', 4]],
        "I": [1],
        "F": [4]
    }

    auto0 = {
        "alphabet": ['a', 'b'],
        "etats": [0, 1, 2, 3],
        "transitions": [[0, 'a', 1], [1, 'a', 1], [1, 'b', 2], [2, 'a', 3]],
        "I": [0],
        "F": [3]
    }

    auto1 = {
        "alphabet": ['a', 'b'],
        "etats": [0, 1],
        "transitions": [[0, 'a', 0], [0, 'b', 1], [1, 'b', 1], [1, 'a', 1]],
        "I": [0],
        "F": [1]
    }

    auto2 = {
        "alphabet": ['a', 'b'],
        "etats": [0, 1],
        "transitions": [[0, 'a', 0], [0, 'a', 1], [1, 'b', 1], [1, 'a', 1]],
        "I": [0],
        "F": [1]
    }

    auto2_d = {
        'alphabet': ['a', 'b'],
        'transitions': [[[0], 'a', [0, 1]], [[0, 1], 'a', [0, 1]], [[0, 1], 'b', [1]], [[1], 'a', [1]], [[1], 'b', [1]]],
        'etats': [[0], [0, 1], [1]],
        'I': [[0]],
        'F': [[0, 1], [1]]
    }

    auto3 = {
        "alphabet": ['a', 'b'],
        "etats": [0, 1, 2],
        "transitions": [[0, 'a', 1], [0, 'a', 0], [1, 'b', 2], [1, 'b', 1]],
        "I": [0],
        "F": [2]
    }

    auto4 = {
        "alphabet": ['a', 'b'],
        "etats": [0, 1, 2],
        "transitions": [[0, 'a', 1], [1, 'b', 2], [2, 'b', 2], [2, 'a', 2]],
        "I": [0],
        "F": [2]
    }
    auto5 = {
        "alphabet": ['a', 'b'],
        "etats": [0, 1, 2],
        "transitions": [[0, 'a', 0], [0, 'b', 1], [1, 'a', 1], [1, 'b', 2], [2, 'a', 2], [2, 'b', 0]],
        "I": [0],
        "F": [0, 1]
    }
    auto6 = {
        "alphabet": ['a', 'b'],
        "etats": [0, 1, 2, 3, 4, 5],
        "transitions": [[0, 'a', 4], [0, 'b', 3], [1, 'a', 5], [1, 'b', 5], [2, 'a', 5], [2, 'b', 2], [3, 'a', 1], [3, 'b', 0], [4, 'a', 1], [4, 'b', 2], [5, 'a', 2], [5, 'b', 5]],
        "I": [0],
        "F": [0, 1, 2, 5]
    }

    autotd7 = {
        "alphabet": ['a', 'b'],
        "etats": [1, 2, 3, 4, 5, 6],
        "transitions": [[1, 'a', 2], [1, 'b', 2], [2, 'a', 3], [2, 'b', 4], [3, 'a', 4], [3, 'b', 5], [4, 'a', 3], [4, 'b', 6], [5, 'a', 6], [5, 'b', 5], [6, 'a', 5], [6, 'b', 6]],
        "I": [1],
        "F": [5, 6]
    }

    auto_ez = {
        "alphabet": ['a', 'b'],
        "etats": [1, 2, 3],
        "transitions": [[1, 'a', 2], [1, 'b', 3], [2, 'a', 3], [2, 'b', 3], [3, 'a', 3], [3, 'b', 3]],
        "I": [1],
        "F": [2, 3]
    }

    auto_det = {
        "alphabet": ['a', 'b'],
        "etats": [1, 2, 3, 4],
        "transitions": [[1, 'a', 2], [1, 'b', 2], [1, 'a', 3], [2, 'b', 1], [2, 'a', 4], [3, 'b', 4], [4, 'b', 3], [4, 'a', 2]],
        "I": [1, 4],
        "F": [3, 4]
    }

    auto_inter_1 = {
        "alphabet": ['a', 'b'],
        "etats": [0, 1, 2],
        "transitions": [[0, 'a', 1], [0, 'b', 0], [1, 'a', 1], [1, 'b', 2], [1, 'a', 2], [2, 'a', 1]],
        "I": [0],
        "F": [0, 1, 2]
    }
    auto_inter_2 = {
        "alphabet": ['a', 'b'],
        "etats": [0, 1],
        "transitions": [[0, 'a', 0], [0, 'b', 1], [1, 'a', 1], [1, 'b', 0]],
        "I": [0],
        "F": [0]
    }
    auto_minimisation = {
        "alphabet": ['a', 'b'],
        "etats": [1, 2, 3, 4, 5, 6, 7],
        "transitions": [[1, 'b', 2], [1, 'a', 4], [2, 'a', 3], [2, 'b', 7], [3, 'a', 2], [3, 'b', 5], [4, 'a', 7], [4, 'b', 7], [5, 'a', 7], [5, 'b', 6], [6, 'b', 5], [6, 'a', 7], [7, 'a', 5], [7, 'b', 7]],
        "I": [1],
        "F": [1, 2, 4, 7]
    }
    print("pref :")
    print(pref("coucou"))
    print("suf:")
    print(suf("coucou"))
    print("fact:")
    print(fact("coucou"))
    print("miroir (mir):")
    print(mir("coucou"))

    L1 = ['aa', 'ab', 'ba', 'bb']
    L2 = ['a', 'b', '']
    print("concatenation :")
    print(concatene(L1, L2))
    print("puis :")
    print(puis(L1, 2))
    print("tousmots :")
    print(tousmots(['a', 'b'], 3))
    print("lirelettre :")
    print(lirelettre(auto["transitions"], auto["etats"], 'a'))
    print("liremot :")
    print(liremot(auto["transitions"], auto["etats"], 'aba'))
    print("accepte :")
    print(accepte(auto, 'aba'))
    print("langage accept:")
    print(langage_accept(auto, 4))
    print("deterministe :")
    print(deterministe(auto_det))
    print("determinise :")
    print(determinise(auto_det))
    print("renommage determinise :")
    print(renommage(determinise(auto_det)))
    print("complet:")
    print(complet(auto0))
    print(complet(auto1))
    print("complete :")
    print(complete(auto0))
    print("complement:")
    print(complement(auto3))
    print("intersection :")
    print(inter(auto_inter_1, auto_inter_2))
