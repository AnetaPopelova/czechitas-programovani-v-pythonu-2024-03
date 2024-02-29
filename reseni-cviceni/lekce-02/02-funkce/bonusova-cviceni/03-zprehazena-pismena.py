import random

def shuffle_letters(word):
    # Pokud má slovo méně nebo rovno 3 písmenů, není co zamíchat
    if len(word) <= 3:
        return word
    
    # Převedení slova na list, aby bylo možné písmena zamíchat
    letters = list(word[1:-1])  # Vyjmutí prvního a posledního písmena
    random.shuffle(letters)  # Zamíchání písmen mezi prvním a posledním písmenem
    shuffled_word = word[0] + ''.join(letters) + word[-1]  # Sestavení slova s ponechanými prvním a posledním písmenem
    
    return shuffled_word

# Testování funkce pro jednotlivá slova
slovo = "Slovo"
print(shuffle_letters(slovo))

# Testování funkce pro delší text více slov
text = '''Slovo je stále možné pohodlně přečíst, když jsou pomíchaná písmena.
Stačí, když první a poslední písmeno je na své pozici zachováno. Napiš funkci,
která bude mít jako vstupní parametr slovo a vrátí slovo, kde zpřehází všechny
znaky kromě prvního a posledního.
'''
shuffled_text = ' '.join(shuffle_letters(word) for word in text.split())
print(shuffled_text)
