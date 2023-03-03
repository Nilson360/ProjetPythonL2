# Exercice 2 :

# Question 1:

"""
 --- Ecrire une structure de données associant chaque lettre et caractère de ponctuation ( , . : ; ' - ? ! ) à son code Morse. 
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
print("=============================================================================")
print("ICI VOUS POUVEZ TRADUIRE UNE LETTRE, UN NUMÉRO OU UN CARACTÈRE EN CODE MORSE ")
print("=============================================================================")

caractere = input("\nEntrez la lettre ou le caractère: ")
#print(code_morse['F'])

print("\n")
print(f"Voici la traduction de votre saisie \"{caractere}\" en morse : {code_morse[caractere]}")
print("\n")

# Explication :

"""
Pour la réalisation de cet exercice, j'ai utilisé la structure de données du type dictionnaire. Pour chaque lettre,numéro ou caractère 
de ponctuation est associé à son code Morse correspondant d'après Wikipédia

Nous pouvons accéder à un code Morse spécifique en utilisant la notation des crochets, comme ceci : code_morse['F']
Pour améliorer le code, j'ai ajouté un input.

"""