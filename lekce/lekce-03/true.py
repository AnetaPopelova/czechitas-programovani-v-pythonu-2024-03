# a = (10 > 9) # Logický výraz 10 > 9 vyhodnotí jako True, protože 10 je skutečně větší než 9. 
a = 1 # 1 je sice pravdivostně ekvivalentní s True (protože cokoliv jiného než 0 je v Pythonu považováno za pravdivé), ala není to přesně stejná hodnota jako True.

# Při použití == True Python porovnává, zda je výsledek výrazu a roven True. 
# V tomto případě b == True vyhodnotí jako True, protože hodnota výrazu 10 > 9 je True.
if a == True:
    print("'b == True' je pravda")
else:
    print("'b == True' není pravda")

# Při použití is True Python kontroluje, zda je objekt b přesně ten samý objekt jako True. 
# V tomto případě b is True také vyhodnotí jako True, protože b je přímo výsledkem logického výrazu, který je True.
if a is True:
    print("'b is True' je pravda")
else:
    print("'b is True' není pravda")
