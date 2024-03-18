# Definice seznamu obsahujícího čísla od 1 do 4
seznam = [1, 2, 3, 4]
# Vytiskne typ proměnné 'seznam', což je <class 'list'>
print(type(seznam))

# Definice n-tice (tuple) obsahujícího čísla od 1 do 4
ntice = 1, 2, 3, 4
# Vytiskne typ proměnné 'ntice', což je <class 'tuple'>
print(type(ntice))

# Definice n-tice s různými typy dat: řetězec, číslo a logickou hodnotu
moje_ntice = "Aneta", 8, True

# Rozbalení n-tice 'moje_ntice' do jednotlivých proměnných
jmeno, cislo, ma_hlad = moje_ntice
# Vytiskne hodnotu proměnné 'cislo', která byla získána z n-tice 'moje_ntice'
print(cislo)

# Vytvoření prázdné množiny 'names'
names = set() 
# Přidání řetězců 'Zuzana' a 'Jitka' do množiny 'names'
names.add('Zuzana')
names.add('Jitka')

# Vytiskne obsah množiny 'names'
# Pozor, množiny (sety) nezachovávají pořadí, takže výstup může být v libovolném pořadí
print(names)
