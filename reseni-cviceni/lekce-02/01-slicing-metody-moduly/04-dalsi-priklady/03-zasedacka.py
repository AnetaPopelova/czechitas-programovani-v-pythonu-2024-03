# Seznam akcí
akce = [
    "školení - řízení firemních vozidel",
    "jazykový kurz - angličtina",
    "pohovor - Jan Dvořák",
    "pohovor - Antonín Sova",
    "jazykový kurz - němčina",
    "pohovor - Iveta Hájková",
    "pohovor - Ivan Brož",
    "pohovor - Katarína Martináková",
    "setkání se zákazníkem - Metrostav",
    "jazykový kurz - angličtina",
    "školení - vykazování práce",
    "pohovor - Klaudie Moudrusová",
]

# Kolik se uskutečnilo pohovorů?
pocet_pohovoru = sum("pohovor" in akce for akce in akce)
print(f"Počet uskutečněných pohovorů: {pocet_pohovoru}")

# V jakých jazycích se mohou zaměstnanci firmy vzdělávat?
jazyky = []
for akce in akce:
    if "jazykový kurz" in akce:
        jazyky.append(akce.split(" - ")[1])

unikatni_jazyky = []
for jazyk in jazyky:
    if jazyk not in unikatni_jazyky:
        unikatni_jazyky.append(jazyk)

print("Zaměstnanci se mohou vzdělávat v následujících jazycích:")
for jazyk in unikatni_jazyky:
    print(jazyk)
