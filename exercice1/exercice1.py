# EXERCICE 1 :

# --- Soit L1 le type liste non vide d’entiers. Soit L2 le type liste non vide d’éléments de type L1.
#Question 1 :

"""
 --- Ecrire une fonction recevant en paramètre une liste de type L2, et renvoyant la liste composée des sommes des sous-listes d’origine.
 --- Par exemple, pour un paramètre égal à [[1,2],[3,2],[4,5,6]] la fonction doit renvoyer : [3,5,15]
"""

list1 = [[1, 2], [3, 2], [4, 5, 6]]

def somme_sousLists(list1):
    return [sum(souslist) for souslist in list1]

sommes = somme_sousLists(list1)
print(sommes)  # affiche -> [3, 5, 15]

# Explications:
"""
La fonction somme_sousList utilise une compréhension de listes pour créer une nouvelle liste
combiné avec la fonction sum() pour calculer la somme de  chaque sous liste : [sum(souslist) for souslist in list]
"""

# Question 2 :

"""
 --- Créer un programme Python qui teste la fonction précédente pour quelques listes de type L2.
 --- Déposer ce programme dans Moodle, ainsi qu’un petit texte expliquant la démarche.
"""

def somme_sousLists(liste):
    return [sum(sousliste) for sousliste in liste]

# Test avec quelques listes de type L2 :

liste1 = [[1, 2], [3, 2], [4, 5, 6]]
liste2 = [[10, 20, 30], [40, 50], [60]]
liste3 = [[-1, -2, -3], [-4, -5], [-6, -7, -8, -9]]


# Affichage des résultats :

print("-------------------- Question 2 --------------------")
print(somme_sousLists(liste1))  # doit afficher -> [3, 5, 15]
print(somme_sousLists(liste2))  # doit afficher -> [60, 90, 60]
print(somme_sousLists(liste3))  # doit afficher -> [-6, -9, -30]


# Explications : 

"""
"""

