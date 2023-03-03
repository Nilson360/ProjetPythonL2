# Exercice 2 :

#Question 4:

"""
En utilisant les 2 fonctions précédentes, créer un programme Python qui demande à saisir une chaine de caractères au clavier, 
puis détermine si ces caractères lus représentent un texte ou bien un code Morse, et enfin écrit le code Morse correspondant 
(dans le premier cas) ou le texte décodé (dans le second cas).
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
def morse_translate(text):
    
    text = text.upper()
    morse_text = []
    for char in text:
        if char in code_morse:
            morse_text.append(code_morse[char])
        else:
            morse_text.append(' ')
    return ' '.join(morse_text)

def morse_decode(morse_text):
 

    morse_text = morse_text.split()
    text = []
    for code in morse_text:
        if code in code_morse :
            text.append(code_morse [code])
        else:
            text.append(' ')
    return ''.join(text)

def main():
    input_text = input("Entrez une chaîne de caractères : ")

    # Déterminer si l'entrée est un texte ou un code Morse

print(code_morse['F'])

# Explication :
