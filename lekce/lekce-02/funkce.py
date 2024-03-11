# Definice funkce pozdrav() bez parametrů, která vypíše "Ahoj!"
def pozdrav():
    print("Ahoj!")

# Volání funkce pozdrav() - vypíše "Ahoj!"
pozdrav()

# Redefinice funkce pozdrav() s parametrem jmeno, vypíše pozdrav s daným jménem
def pozdrav(jmeno):
    print(f"Ahoj {jmeno}")

# Volání redefinované funkce pozdrav() s různými jmény
pozdrav(jmeno="Jano")
pozdrav("Katko")

# Definice funkce soucet_cisel() s parametry a a b, vrací jejich součet
def soucet_cisel(a, b):
    return a + b
    # Tento print se nikdy nevykoná, protože je za příkazem return
    print(a + b)

# Volání funkce soucet_cisel() a výpis jejího výsledku
vysledek = soucet_cisel(2, 9)
print(vysledek)
print(soucet_cisel(2, 9))

# Definice globální proměnné smenny_kurz
smenny_kurz = 25

# Definice funkce pro převod eur na koruny pomocí globálního směnného kurzu
def smena_na_koruny(eura):
    return eura * smenny_kurz

# Volání funkce s pevně nastaveným směnným kurzem
print(smena_na_koruny(2))

# Redefinice funkce s možností specifikovat směnný kurz
def smena_na_koruny(eura, kurz):
    return eura * kurz

# Volání redefinované funkce s uvedením směnného kurzu
print(smena_na_koruny(2, 25))

# Definice proměnných eura a kurz
eura = 2
kurz = 25
# Redefinice funkce smena_na_koruny() bez parametrů, používá globální proměnné
def smena_na_koruny():
    return eura * kurz

# Volání funkce bez parametrů
print(smena_na_koruny())

# Definice funkce jeste_presne_nevim(), která nic nedělá (použití pass)
def jeste_presne_nevim(vstup1, vstup2):
    pass


# Redefinice funkce pozdrav() s výchozí hodnotou parametru
def pozdrav(jmeno='defaultni hodnota'):
    print(f"Ahoj {jmeno}")

# Volání funkce pozdrav() bez parametru a s parametrem
pozdrav()
pozdrav(jmeno="Terezo")
