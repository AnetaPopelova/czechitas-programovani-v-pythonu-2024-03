# Balíčky v Pythonu

V Pythonu je "balíček" sada modulů nebo knihoven, které jsou zabaleny dohromady, aby poskytovaly funkce, které mohou být sdíleny mezi více projekty. Balíčky mohou obsahovat funkce, třídy, skripty, datové soubory a další komponenty, které usnadňují vývoj aplikací tím, že poskytují znovupoužitelné bloky kódu.

## Principy balíčků v Pythonu
## Struktura: Balíček v Pythonu obvykle obsahuje:
* Moduly: Jednotlivé soubory .py, které obsahují Python kód.
__init__.py: Speciální soubor, který Pythonu říká, že adresář obsahující tento soubor je Python balíček. Soubor `__init__.py` může být prázdný, nebo může obsahovat kód pro inicializaci balíčku.
* Dokumentace: Součástí balíčku mohou být také dokumentační soubory, které vysvětlují, jak balíček funguje a jak ho používat.
* Metadata: Soubory, které obsahují informace o balíčku, jako jsou závislosti, autor, verze a další.
* Instalace balíčků: Balíčky se obvykle distribuují přes *Python Package Index (PyPI)* a instalují se pomocí nástroje `pip`, který je standardním správcem balíčků pro Python.Instalace balíčku pomocí `pip` je jednoduchá. Například pro instalaci balíčku `requests` použijete příkaz:
```
pip install requests
``` 

Tento příkaz stáhne balíček `requests` z *PyPI* a nainstaluje ho do vašeho Python prostředí.

## Jak pip spravuje balíčky
* Stahování balíčků: pip se připojí k PyPI, vyhledá požadovaný balíček a jeho závislosti, a stáhne je do vašeho systému.
* Instalace balíčků: Po stažení pip rozbalí balíček a spustí příslušný instalační skript. Skript obvykle zkopíruje soubory balíčku do správných umístění ve vašem systému.
* Správa závislostí: pip automaticky zpracovává závislosti balíčků, což znamená, že když instalujete jeden balíček, který vyžaduje další balíčky k fungování, pip je stáhne a nainstaluje.

## Důležité aspekty balíčků
* Virtuální prostředí: K izolaci závislostí a verzí balíčků pro různé projekty se doporučuje používat virtuální prostředí. To umožňuje mít různé verze stejného balíčku pro různé projekty bez konfliktů.
* Aktualizace a odinstalace: Balíčky lze snadno aktualizovat pomocí příkazu `pip install <balicek> --upgrade` a odinstalovat pomocí `pip uninstall <balicek>`.

Balíčky tedy v Pythonu poskytují způsob, jak organizovat, sdílet a znovu používat kód mezi projekty a mezi vývojáři, což vede k efektivnějšímu a udržitelnějšímu vývoji softwaru.

Všechny nainstalované balíčky můžeme vypsat pomocí příkazu `pip list`.

---

> *V kontextu programování v Pythonu, termíny "modul" a "knihovna" mají specifické významy a rozlišují se způsobem, jakým jsou používány ve vývoji softwaru*

### Modul
Modul v Pythonu je jednoduše soubor, který obsahuje definice Python kódu, včetně proměnných, funkcí, tříd nebo jakýchkoli spustitelných kódů. Moduly umožňují logicky organizovat Python kód do menších, spravovatelných částí. Díky modulům můžete vytvářet znovupoužitelný kód, který je snadno importovatelný a použitelný v jiných Python skriptech nebo programech.

Příklad modulu: Soubor s názvem `math.py`, který obsahuje funkce pro matematické operace.

### Knihovna
Knihovna v Pythonu je kolekce modulů, která poskytuje sadu nástrojů a funkcionality, které můžete použít ve svých programech. Knihovny obvykle řeší specifický problém nebo poskytují specifické funkcionality, jako je práce se soubory, manipulace s daty, grafické uživatelské rozhraní atd. Knihovna může obsahovat jednoduché moduly, složité balíčky s mnoha moduly, nebo kombinaci obojího.

Příklad knihovny: Knihovna `NumPy`, která je kolekcí modulů poskytujících pokročilé matematické funkce a operace s polemi.


### Rozdíly
* Rozsah: Modul je jednotlivý soubor, zatímco knihovna je kolekce modulů nebo balíčků.
* Účel: Modul je základní stavební blok, který lze importovat a používat v rámci většího programu. Knihovna poskytuje širší sadu funkcionalit, často zahrnující mnoho modulů, které spolupracují na poskytnutí komplexních služeb nebo řešení specifických problémů.
* Použití: Import modulu znamená přístup k jednotlivým funkcím, třídám nebo atributům definovaným v daném modulu. Použití knihovny znamená využití různých modulů nebo funkcí, které knihovna nabízí, pro širší spektrum úkolů.
* Shrnutí: Modul je základním stavebním kamenem, zatímco knihovna je soubor těchto stavebních kamenů sestavený tak, aby poskytoval širší funkčnost nebo řešil konkrétní sadu problémů.