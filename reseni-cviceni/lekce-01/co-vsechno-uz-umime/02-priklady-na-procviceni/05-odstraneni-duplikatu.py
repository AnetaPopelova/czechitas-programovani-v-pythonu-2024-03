# Původní seznam
seznam = [1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 8, 9, 9]

# Inicializace prázdného seznamu pro uchování prvků bez duplikátů
bez_duplicit = []

# Projdi všechny prvky původního seznamu
for prvek in seznam:
    # Pokud prvek ještě není v seznamu bez duplicit, přidej ho
    if prvek not in bez_duplicit:
        bez_duplicit.append(prvek)

# Vypsání nového seznamu bez duplicit
print("Nový seznam bez duplicit:", bez_duplicit)
