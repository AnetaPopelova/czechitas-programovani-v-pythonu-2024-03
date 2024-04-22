# Funkce Main v Pythonu

## Proč používáme funkci `main()`?

Funkce `main()` hraje klíčovou roli ve větších a složitějších Python skriptech a aplikacích. Zde jsou některé klíčové důvody, proč je výhodné tuto funkci v Pythonu používat:

### 1. Organizace kódu
Funkce `main()` umožňuje programátorům udržet kód strukturovaný. Umožňuje centrální místo pro volání dalších funkcí a metod, což zvyšuje čitelnost a usnadňuje údržbu kódu.

### 2. Kontrola toku programu
Definování funkce `main()` jako vstupního bodu programu umožňuje řídit, jaké funkce se budou kdy a v jakém pořadí vykonávat. Toto je zvláště užitečné, pokud může být váš skript použit samostatně nebo jako modul importovaný v jiném skriptu.

### 3. Snadnější testování a ladění
Když je hlavní funkčnost programu soustředěna do funkce `main()`, je jednodušší psát testy a ladit kód. Funkci `main()` lze volat v testovacím prostředí s různými parametry, což usnadňuje identifikaci a opravu chyb.

### 4. Podmíněné spuštění
Struktura:
```python
if __name__ == "__main__":
    main()
```
zajišťuje, že funkce main() se spustí pouze tehdy, když je soubor spuštěn jako hlavní program. Pokud je soubor importován jako modul, tento blok se nevykoná, což zabrání nechtěnému spouštění kódu.

## Závěr

Použití funkce `main()` je dobrá praxe, která vede k lepší strukturovanosti, čitelnosti a udržovatelnosti kódu v Pythonu.