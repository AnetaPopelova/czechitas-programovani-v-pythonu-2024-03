# Virtuální prostředí v Pythonu

Virtuální prostředí v Pythonu jsou izolované pracovní prostředky, které umožňují programátorům spravovat závislosti pro různé projekty nezávisle na sobě. 

Toto izolované prostředí zajišťuje, že každý projekt může mít svou vlastní specifickou sadu knihoven a balíčků, aniž by to ovlivnilo ostatní projekty nebo globální konfiguraci Pythonu na systému. Tím se minimalizují konflikty mezi knihami a usnadňuje se správa verzí a závislostí.

## Jak virtuální prostředí funguje
### Izolace
Každé virtuální prostředí má svůj vlastní Python interpreter a sadu nainstalovaných knihoven. Když aktivujete virtuální prostředí a instalujete balíčky pomocí PIP, jsou tyto balíčky instalovány pouze do tohoto prostředí. Tím se oddělují od systémové instalace Pythonu a od jakýchkoli jiných virtuálních prostředí.

### Instalace balíčků
Během aktivního virtuálního prostředí, když použijete příkaz pip install, balíček se nainstaluje pouze do tohoto prostředí. To vám umožňuje mít pro různé projekty různé verze téhož balíčku bez vzájemného ovlivnění.

### Práce s virtuálním prostředím
* Vytvoření: Virtuální prostředí můžete vytvořit pomocí modulu venv (dříve virtualenv), který je součástí standardní knihovny Pythonu. Příkaz pro vytvoření nového prostředí je obvykle `python -m venv nazev_prostredi`.
* Aktivace: Pro aktivaci virtuálního prostředí se používají specifické skripty v adresáři virtuálního prostředí. Na Windows použijete `nazev_prostredi\Scripts\activate`, na Unix-like systémech je to `source nazev_prostredi/bin/activate`.
* Deaktivace: Virtuální prostředí deaktivujete příkazem `deactivate`, který zpětně nastaví vaše proměnné prostředí tak, aby znovu používaly globální instalaci Pythonu.

### Výhody používání virtuálních prostředí
* Konflikty: Omezení konfliktů mezi knihami různých projektů.
* Závislosti: Jednoduché správa specifických závislostí pro každý projekt.
* Vývoj: Umožňuje bezpečný vývoj a testování nových knihoven a aktualizací bez rizika narušení stabilního prostředí.
* Portabilita: Snadné sdílení a replikace vývojového prostředí, což usnadňuje kolaboraci a nasazování.


Virtuální prostředí je klíčovým nástrojem pro efektivní a organizovaný vývoj software v Pythonu, a jeho použití se doporučuje pro téměř všechny Python projekty.