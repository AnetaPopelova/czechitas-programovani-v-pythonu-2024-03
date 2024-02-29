numbers = [7728, 88, 958621, 5941, 959847272, 3944, 80, 521, 57035, 3967894]

# Zjistění délky nejdelšího čísla
max_length = len(str(max(numbers)))

# # Inicializace délky nejdelšího čísla jako délka prvního čísla ve seznamu
# max_length = len(str(numbers[0]))

# # Procházení zbývajících čísel ve seznamu a aktualizace délky nejdelšího čísla
# for number in numbers[1:]:
#     length = len(str(number))
#     if length > max_length:
#         max_length = length

# print("Maximální délka:", max_length)

# Funkce pro zarovnání textu na zadanou délku s volitelným znakem pro vyplnění
def align_right(text, length, fill_char=' '):
    return fill_char * (length - len(text)) + text

# Vypsání seznamu čísel zarovnaných vpravo
for number in numbers:
    print(align_right(str(number), max_length))

for number in numbers:
    print(align_right(str(number), max_length, '.'))
