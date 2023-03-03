# Exercice 2 :

# Question 2:

"""
 ---- Réaliser une fonction recevant en paramètre une phrase et renvoyant sa traduction Morse sous forme d’une chaine de caractères. 
 Chaque code (donc chaque suite de points/traits représentant un caractère) sera séparé du suivant par un espace, l’espace étant lui-même codé par un espace.
 Par exemple, cette fonction appelée avec la chaine "Le projet Python." doit renvoyer la chaîne :
 .-.. .   .--. .-. --- .--- . -   .--. -.-- - .... --- -. .-.-.-
"""

#Definition de la structure de données :

code_morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    ',': '--..--', '.': '.-.-.-', ':': '---...', ';': '-.-.-.', "'": '.----.', '-': '-....-', '?': '..--..',
    '!': '-.-.--'
}

caractere = input("Entrez votre phares: ")

#fontion pour la traduction:

def traduction_morse(texte):
    texte = texte.upper()
    morse_texte = []
    for phrase in texte:
        if phrase in code_morse:
            morse_texte.append(code_morse[phrase])
        else:
            morse_texte.append(' ')
    return ' '.join(morse_texte)

print(f"\nVoici la traduction de votre phrase \"{caractere}\" en code morse: {traduction_morse(caractere)}")

# Explication :

"""
En utilisant le dictionnaire de la question précédente et en ajoutant un input pour améliorer le cahier de charges,
 voici l'explication du fonctionnement de la fonction de traduction :
    -- fonction "traduction_morse()" prend en entrée une chaîne de caractères "texte" et renvoie sa traduction en code Morse.
    -- Tout d'abord il utilise la methode ".upper()" pour convertir toutes les lettres de la chaîne en majuscule afin de matcher avec les éléments du dictionnaire
    -- Ensuite, elle parcourt chaque caractère de la chaîne texte et vérifie si ce caractère existe dans le dictionnaire "traduction_morse". 
        Si c'est le cas, elle ajoute le code morse correspondant à la liste "morse_texte" à l'aide de la méthode "append()".
      Si le caractère n'est pas dans le "dictionnaire code_morse", la fonction ajoute un espace à la liste "morse_texte" à la place.
    -- Enfin, la fonction renvoie une chaîne de caractères qui est la traduction de text en code Morse =>" return ' '.join(morse_texte)",
     convertant la liste morse_texte en chaîne de caractères à l'aide de la méthode "join()" en insérant un espace entre chaque élément de la liste.
"""
