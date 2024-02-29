# Časy vítěze a časy běžců ve formátu [číslo běžce, čas v minutách]
cas_vitez = 128.5
casy_bezcu = [
    [1, 130.2],
    [2, 131.0],
    [3, 129.8],
    [4, 132.1],
    [5, 129.5]
]

# Seznam pro uchování rozdílů mezi časy běžců a vítěze
rozdily_casu = []

# Vypočet rozdílů časů pro každého běžce
for cas_bezce in casy_bezcu:
    rozdil = cas_bezce[1] - cas_vitez
    rozdily_casu.append([cas_bezce[0], rozdil])

# Výpis výsledků
for rozdil in rozdily_casu:
    print(f"Běžci číslo {rozdil[0]} chybělo k vítězství {rozdil[1]} minut.")
