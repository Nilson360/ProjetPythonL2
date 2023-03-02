# ENNONCÉ
"""
Soit L1 le type liste non vide d’entiers. Soit L2 le type liste non vide d’éléments de type L1.
Question 1
Ecrire une fonction recevant en paramètre une liste de type L2, et renvoyant la liste composée des sommes des sous-listes d’origine.
Par exemple, pour un paramètre égal à [[1,2],[3,2],[4,5,6]] la fonction doit renvoyer : [3,5,15]
"""

list = [[1, 2], [3, 2], [4, 5, 6]]

def somme_sousLists(list):
    return [sum(souslist) for souslist in list]

sums = somme_sousLists(list)
print(sums)  # affiche -> [3, 5, 15]

# Explications:
"""
La fonction somme_sousList utilise une compréhension de listes pour créer une nouvelle liste
combiné avec la fonction sum() pour calculer la somme de  chaque sous liste : [sum(souslist) for souslist in list]
"""