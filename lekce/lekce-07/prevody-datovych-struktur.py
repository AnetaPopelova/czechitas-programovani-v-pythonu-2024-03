# 1. Převod seznamu na slovník

seznam = [("klíč1", "hodnota1"), ("klíč2", "hodnota2"), ("klíč3", "hodnota3")]
slovnik = dict(seznam)
print(slovnik)

# {'klíč1': 'hodnota1', 'klíč2': 'hodnota2', 'klíč3': 'hodnota3'}


# 2. Převod slovníku na seznam
slovnik = {'klíč1': 'hodnota1', 'klíč2': 'hodnota2', 'klíč3': 'hodnota3'}
seznam = list(slovnik.items())
print(seznam)

# [('klíč1', 'hodnota1'), ('klíč2', 'hodnota2'), ('klíč3', 'hodnota3')]

# Pouze klíče:
seznam_klicu = list(slovnik.keys())

# Pouze hodnoty:
seznam_hodnot = list(slovnik.values())

# Převod seznamu hodnot na slovník s indexy jako klíče
seznam_hodnot = ['hodnota1', 'hodnota2', 'hodnota3']
slovnik = {}
for index in range(len(seznam_hodnot)):
    slovnik[index] = seznam_hodnot[index]

print(slovnik)

# {0: 'hodnota1', 1: 'hodnota2', 2: 'hodnota3'}

# Alternativní metoda pomocí funkce enumerate a list comprehesion
seznam_hodnot = ['hodnota1', 'hodnota2', 'hodnota3']
slovnik = {index: hodnota for index, hodnota in enumerate(seznam_hodnot)}
print(slovnik)
{0: 'hodnota1', 1: 'hodnota2', 2: 'hodnota3'}
