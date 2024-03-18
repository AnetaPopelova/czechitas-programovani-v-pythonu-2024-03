books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]

# Spočítání celkového počtu stran
celkem_stran = 0
for book in books:
    celkem_stran += book["pages"]
print("Celkový počet přečtených stran:", celkem_stran)

# Spočítání počtu knih s hodnocením alespoň 8
pocet_knih_s_vysokym_hodnocenim = 0
for book in books:
    if book["rating"] >= 8:
        pocet_knih_s_vysokym_hodnocenim += 1
print("Počet knih s hodnocením alespoň 8:", pocet_knih_s_vysokym_hodnocenim)