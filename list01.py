# ENNONCÉ
"""
Soit L1 le type liste non vide d’entiers. Soit L2 le type liste non vide d’éléments de type L1.
Question 1
Ecrire une fonction recevant en paramètre une liste de type L2, et renvoyant la liste composée des sommes des sous-listes d’origine.
Par exemple, pour un paramètre égal à [[1,2],[3,2],[4,5,6]] la fonction doit renvoyer : [3,5,15]
"""
list = [[1, 2], [3, 2], [4, 5, 6]]

def sum_sublists(list):
    return [sum(sublst) for sublst in list]

sums = sum_sublists(list)
print(sums)  # affiche [3, 5, 15]