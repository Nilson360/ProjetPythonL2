# Exercice  :

#Question 3:

"""
 --- Réaliser la fonction inverse, recevant en paramètre un code Morse et renvoyant sa traduction sous forme de chaine de caractères.
"""
# Structure de données :
code_morse = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
        '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
        '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
        '-.--': 'Y', '--..': 'Z',
        '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6',
        '--...': '7', '---..': '8', '----.': '9',
        '--..--': ',', '.-.-.-': '.', '---...': ':', '-.-.-.': ';', '.----.': "'", '-....-': '-',
        '..--..': '?', '-.-.--': '!', '/': ' '
    }
def traduction_texte(morse_texte):

    morse_texte = morse_texte.split()
    texte = []
    for code in morse_texte:
        if code in code_morse:
            texte.append(code_morse[code])
        else:
            texte.append(' ')
    return ''.join(texte)

print(traduction_texte(".- -. --. --- .-.. .-"))



# Explication :
"""
    --- Tout d'abord j'ai change la structure du dictionnnaire, le code morse est l'élément et la clé le caractère.
    --- Explication de la fonction traduction_caractere :
        --- À l'aide du dictionnaire code_morse la fonction traduction_morse associe chaque code Morse à sa lettre, chiffre ou caractère de ponctuation correspondant.
        --- D'abord, j'utilise la methode split() pour divirser la chaîne morse_texte en une liste qui sera stocké dans texte = [].
        --- Ensuite, la fonction, avec le for code in morse_texte parcourt le dictionnaire afin de trouver chaque élément, s'il est trouvé, la fonction ajoute
        l'élément trouvé dans la liste "texte" à l'aide de la methode .append(), sinon, on ajoute un espace.
        --- Finalement, avec la méthode .join(), la fonction renvoie une chaîne de caractère qui est la traduction de morse_code => return ''.join(texte)
        """
