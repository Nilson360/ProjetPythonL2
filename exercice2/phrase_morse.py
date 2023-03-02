# Exercice 2 :

# Question 2:

"""
 ---- Réaliser une fonction recevant en paramètre une phrase et renvoyant sa traduction Morse sous forme d’une chaine de caractères. 
 Chaque code (donc chaque suite de points/traits représentant un caractère) sera séparé du suivant par un espace, l’espace étant lui-même codé par un espace.
 Par exemple, cette fonction appelée avec la chaine "Le projet Python." doit renvoyer la chaîne :
 .-.. .   .--. .-. --- .--- . -   .--. -.-- - .... --- -. .-.-.-
"""

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

def traduction_morse(texte):
    texte = texte.upper()
    morse_texte = []
    for phrase in texte:
        if phrase in code_morse:
            morse_texte.append(code_morse[phrase])
        else:
            morse_texte.append(' ')
    return ' '.join(morse_texte)

print(traduction_morse("Le projet Python"))

# Explication :