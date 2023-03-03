# Exercice 2 :

#Question 4:

"""
En utilisant les 2 fonctions précédentes, créer un programme Python qui demande à saisir une chaine de caractères au clavier, 
puis détermine si ces caractères lus représentent un texte ou bien un code Morse, et enfin écrit le code Morse correspondant 
(dans le premier cas) ou le texte décodé (dans le second cas).
"""
#Strutures de données:

"""code_mose = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    ',': '--..--', '.': '.-.-.-', ':': '---...', ';': '-.-.-.', "'": '.----.', '-': '-....-', '?': '..--..',
    '!': '-.-.--'
}"""

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

# Texte -> Morse, fonction  récrite:

def traduction_morse(texte):

    texte = texte.upper()
    morse_texte = []
    for caractere in texte:
        if caractere in code_morse.values():
            for code, caractere_morse in code_morse.items():
                if caractere == caractere_morse:
                    morse_texte.append(code)
        elif caractere == ' ':
            morse_texte.append('/')
    return ' '.join(morse_texte)

 # Morse -> texte, fonction récrite :

def traduction_texte(morse_texte):

    morse_texte = morse_texte.split()
    texte = []
    for code in morse_texte:
        if code in code_morse:
            texte.append(code_morse[code])
        elif code == '/':
            texte.append(' ')
    return ''.join(texte)


# Programme principal

caractere = input("Entrez votre texte ou code Morse : ")

if all(caractere[i] in '-. ' for i in range(len(caractere))):
    texte_decode = traduction_texte(caractere)
    print(f"La traduction de \"{caractere}\" en texte est : \"{texte_decode}\"")
else:
    morse_code = traduction_morse(caractere)
    print(f"La traduction de \"{caractere}\" en code Morse est : \"{morse_code}\"")


# je voulais souligner que ce code je l'ai amélioré avec l'aide de chatGPT, celui que j'ai produit ne marchait pas très bien dû la réecriture des fonctions
# EXPLICATION :

"""
Le programme commence par importer les deux fonctions traduction_morse() et traduction_texte() définies précédentes.
L'utilisateur saisi un texte ou un code morse.
Ensuite, le programme utilise la fonction all() et une compréhension de liste pour déterminer si la chaîne de caractères est un 
code Morse ou un texte. 
    --- Si la chaîne ne contient que des tirets, des points et des espaces, le programme utilise la fonction traduction_texte ()
 pour traduire le code Morse en texte. Sinon, le programme utilise la fonction traduction_morse() pour traduire le texte en code Morse
"""