# Správce úkolů

## Cíl projektu
Cílem tohoto projektu je vytvořit jednoduchou aplikaci pro správu úkolů v Pythonu. Aplikace umožní uživatelům přidávat, odstraňovat a prohlížet úkoly.

## Podrobný popis kroků projektu

### 1. Inicializace projektu
- Vytvořte nový Python soubor (např. `task_manager.py`).
- Na začátek souboru přidejte import potřebného modulu `datetime`, který bude využit pro přidávání časových razítek k úkolům.

### 2. Definice třídy Task
- Definujte třídu `Task`, která bude reprezentovat jednotlivé úkoly.
- Třída bude mít konstruktor `__init__`, který přijímá jeden parametr `description` (popis úkolu).
- V konstruktoru nastavte atributy `description` a `timestamp`. Atribut `timestamp` bude automaticky nastaven na aktuální datum a čas.

### 3. Vytvoření datové struktury pro ukládání úkolů
- Použijte slovník `tasks` pro ukládání úkolů, kde klíče budou jedinečná ID úkolů a hodnoty budou instance třídy `Task`.

### 4. Implementace funkcí pro manipulaci s úkoly
- `add_task(description)`: Funkce pro přidání nového úkolu. Generuje unikátní ID pro každý úkol, přidává úkol do slovníku a vypisuje informaci o přidání.
- `remove_task(task_id)`: Funkce pro odstranění úkolu. Kontroluje, zda úkol s daným ID existuje, a pokud ano, odstraní ho.
- `show_tasks()`: Funkce pro zobrazení všech aktuálně uložených úkolů společně s jejich popisem a časem přidání.

### 5. Hlavní smyčka programu
- Napište funkci `main()`, která bude obsahovat nekonečnou smyčku, jež načítá příkazy od uživatele.
- Umožněte uživateli zadat příkazy `add`, `remove` a `show`. Na základě vstupu volajte odpovídající funkce.

### 6. Testování a spuštění aplikace
- Ujistěte se, že skript správně zpracovává všechny typy příkazů a že úkoly jsou správně přidávány, odstraňovány a zobrazovány.
- Spusťte skript v terminálu nebo příkazové řádce a otestujte jeho funkčnost.

### 7. Verzování kódu pomocí Git
- Inicializujte Git repozitář v adresáři projektu.
- Uložte změny (commit) a pushněte je na GitHub. Tento krok poskytne studentům základní praxi s verzováním kódu.

