import json

# Vytvoření prázdného slovníku
words_dict = {}

# Čtení vstupního souboru a naplnění slovníku
with open("reseni-cviceni/lekce-10/words.txt", "r") as file:
    for line in file:
        word = line.strip()
        if word:  # ověření, že řádek není prázdný
            first_letter = word[0].lower()  # získání prvního písmene
            if first_letter not in words_dict:
                words_dict[first_letter] = []
            words_dict[first_letter].append(word)

# Seřazení slov na každém klíči
for letter in words_dict:
    words_dict[letter].sort()

# Zápis do JSON souboru s odsazením 4 mezery
with open("reseni-cviceni/lekce-10/output.json", "w") as json_file:
    json.dump(words_dict, json_file, indent=4, sort_keys=True)
