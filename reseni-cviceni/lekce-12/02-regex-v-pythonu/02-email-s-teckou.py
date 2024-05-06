import re

regularni_vyraz = re.compile(r"\w+\.?\w+@\w+\.cz")
email = "jiripesik@python.cz"
vysledek = regularni_vyraz.fullmatch(email)

if vysledek:
    print("E-mail jméno je v pořádku.")

# regex_email_better = re.compile(r"\w+\.?+(\w+)?@\w+\.cz")
# email = "m@email.cz"
# if regex_email_better.fullmatch(email):
#     print("Okay")
