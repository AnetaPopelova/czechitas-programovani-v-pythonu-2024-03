import re

zaznamy = """
searchNumber: pavca.czechitas action: search phone number of user dita
user: pavca action: send sms to phone number +420728123456
user: jirka: action: send 2 sms to phone number +420734123456
"""

regularni_vyraz = re.compile(r"[+\d]{13}")
vysledky = regularni_vyraz.findall(zaznamy)

for vysledek in vysledky:
    print(vysledek)

anonymni_zaznamy = regularni_vyraz.sub("X" * 9, zaznamy)

print(anonymni_zaznamy)


# re.findall tries to match captures groups (i.e. the portions of the regex that are enclosed in parentheses),
# then it is the groups that are returned, rather than the matched string.
# One way to solve this issue is to use non-capturing groups (prefixed with ?:).

# regularni_vyraz = re.compile(r"(\+420)? ?\d{3} ?\d{3} ?\d{3}") # vraci jen "+420"
# regularni_vyraz = re.compile(r"(?:\+420)? ?\d{3} ?\d{3} ?\d{3}") # vraci cele cislo
