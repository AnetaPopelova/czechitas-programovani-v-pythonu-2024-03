pohyby = [1200, -250, -800, 540, 721, -613, -222]

# Vypište v pořadí třetí pohyb z uvedeného seznamu
print("Třetí pohyb:", pohyby[2])

# Vypište všechny pohyby kromě prvních dvou
print("Všechny pohyby kromě prvních dvou:", pohyby[2:])

# Vypište kolik je všech pohybů dohromady
print("Celková suma pohybů:", sum(pohyby))

# Vypište nejvyšší a nejnižší pohyb
print("Nejvyšší pohyb:", max(pohyby))
print("Nejnižší pohyb:", min(pohyby))

# Spočítejte celkový přírůstek na účtu za dané období
celkovy_prirustek = sum(pohyby)
print("Celkový přírůstek na účtu:", celkovy_prirustek)