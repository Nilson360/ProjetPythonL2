# Exercice  :

#Question 3:

"""
 --- Réaliser la fonction inverse, recevant en paramètre un code Morse et renvoyant sa traduction sous forme de chaine de caractères.
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

def traduction_morse_texte(morse_texte):
  
    morse_texte = morse_texte.split()
    texte = []
    for code in morse_texte:
        if code in code_morse:
            texte.append(code_morse[code])
        else:
            texte.append(' ')
    return ''.join(texte)

print(traduction_morse_texte('.-.. .   .--. .-. --- .--- . -   .--. -.-- - .... --- -. .-.-.-'))

# Explication :

