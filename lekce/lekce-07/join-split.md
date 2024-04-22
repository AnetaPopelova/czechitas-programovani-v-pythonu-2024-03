## Cvičení: Práce s metodou split

**Úkol 1:**
Vytvořte proměnnou veta s hodnotou: `"Ahoj světe, učíme se Python!"`
Použijte metodu split k rozdělení této věty na slova.
Výsledek uložte do proměnné slova a vypište ji.

Očekávaný výstup:
```py
['Ahoj', 'světe,', 'učíme', 'se', 'Python!']
```

Modifikujte úkol tak, aby se věta dělila pouze na věty, tedy použijte split s parametrem , .

**Úkol 2:**

Vytvořte proměnnou text s hodnotou: `"Ahoj! Jak se máš? Já se mám skvěle. A co ty? Už jsi dokončil Python projekt?"`
Rozdělte text na jednotlivé věty a odstraňte z nich veškeré interpunkční znaménka.
Výsledek uložte do seznamu `vety_bez_interpunkce` a každou větu rozdělte na slova.
Vytvořte slovník, kde klíčem bude číslo věty a hodnotou seznam slov z této věty.
Očekávaný výstup (příklad):

```py
{
  1: ['Ahoj'],
  2: ['Jak', 'se', 'máš'],
  3: ['Já', 'se', 'mám', 'skvěle'],
  4: ['A', 'co', 'ty'],
  5: ['Už', 'jsi', 'dokončil', 'Python', 'projekt']
}
```


## Cvičení: Práce s metodou join
**Úkol 1:**
Mějte seznam slov: `['Python', 'je', 'skvělý', 'jazyk']`.
Použijte metodu join k spojení slov v seznamu do jedné věty s mezerami mezi slovy.
Výsledek uložte do proměnné veta a vypište ji.

Očekávaný výstup:

```py
Python je skvělý jazyk
```

Vytvořte větu, kde budou slova oddělena čárkou a mezerou, například: `"Python, je, skvělý, jazyk".`


**Úkol 2:**

Mějte seznam seznamů slov, například: `[["Python", "je", "zábavný"], ["Ale", "také", "náročný!"], ["Začněte", "s", "námi", "dnes!"]]`.
Spojujte slova v každém vnitřním seznamu do vět pomocí metody join.
Výsledné věty spojte do jednoho odstavce, kde každá věta bude oddělena dvěma mezerami.
Očekávaný výstup:

```py
Python je zábavný.  Ale také náročný!  Začněte s námi dnes!
```

---
### Řešení: Práce s metodou split

```py
veta = "Ahoj světe, učíme se Python!"
slova = veta.split()
print(slova)

vety = veta.split(", ")
print(vety)


text = "Ahoj! Jak se máš? Já se mám skvěle. A co ty? Už jsi dokončil Python projekt?"
# Odstranění interpunkcí potřebných pro rozdělení na věty
interpunkce = "!?,."
for znak in interpunkce:
    text = text.replace(znak, '')

# Rozdělení textu na věty podle teček
vety = text.split('. ')

# Vytvoření slovníku s čísly vět a jejich slovy
vety_bez_interpunkce = {}
index_vety = 1
for veta in vety:
    slova = veta.split()
    vety_bez_interpunkce[index_vety] = slova
    index_vety += 1

print(vety_bez_interpunkce)

## V tomto způsobu řešení jsou zaměrně použité pokročilé postupy
import string

text = "Ahoj! Jak se máš? Já se mám skvěle. A co ty? Už jsi dokončil Python projekt?"
# Odstranění interpunkcí a rozdělení textu na věty
vety = text.translate(str.maketrans('', '', string.punctuation)).split()
# Rozdělení vět na slova
slova_ve_vetach = [veta.split() for veta in vety]
# Vytvoření slovníku s čísly vět
vety_bez_interpunkce = {i + 1: slova for i, slova in enumerate(slova_ve_vetach)}

print(vety_bez_interpunkce)
```

### Řešení: Práce s metodou join
```py
slova = ['Python', 'je', 'skvělý', 'jazyk']
veta = " ".join(slova)
print(veta)

slova = ['Python', 'je', 'skvělý', 'jazyk']
veta = ", ".join(slova)


slova_v_listech = [["Python", "je", "zábavný"], ["Ale", "také", "náročný!"], ["Začněte", "s", "námi", "dnes!"]]
# Spojení slov v každém vnitřním seznamu do vět
vety = [" ".join(slova) for slova in slova_v_listech]
# Spojení vět do jednoho odstavce s dvojitými mezerami mezi větami
odstavec = "  ".join(vety)
# Výsledek
print(odstavec)
```