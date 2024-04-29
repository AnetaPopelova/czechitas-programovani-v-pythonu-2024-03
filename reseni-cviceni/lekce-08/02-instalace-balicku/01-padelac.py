# Abyste mohli používat balíček Faker ve vašem Python programu, musíte jej nejprve nainstalovat. 
# To lze udělat pomocí následujícího příkazu, který spustíte ve vašem terminálu nebo příkazové řádce:

# pip install Faker
# pip3 install Faker

from faker import Faker

# Kód pro generování základních údajů vypadá následovně:
fake = Faker()

print(fake.name())
print(fake.address())
print(fake.text())

# Pro generování 10 náhodných jmen můžete použít tento kód:
for _ in range(10):
    print(fake.name())

fake = Faker('cs_CZ')

for _ in range(10):
    print(fake.name())  # Vygeneruje česká jména

fake = Faker('cs_CZ')

for _ in range(10):
    print(fake.first_name_female())  # Vygeneruje 10 náhodných českých ženských jmen

for _ in range(5):
    print(fake.address())  # Vygeneruje 5 náhodných českých adres

'''
V Pythonu se znak _ (podtržítko) často používá jako dočasná nebo "anonymní" proměnná ve smyčkách a výrazech. 
Specificky v kontextu smyčky for, když použijete _ v for _ in range(n), to signalizuje, že v daném cyklu nebudete hodnotu proměnné vůbec používat. 
Proměnná _ zde funguje jako zástupný symbol pro každý průběh cyklu, ale její hodnota se nikde nevyužije.
'''