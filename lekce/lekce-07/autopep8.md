# Práce s knihovnou autopep8

## Úvod
Knihovna `autopep8` je nástroj v Pythonu, který automaticky formátuje Python kód tak, aby odpovídal doporučením PEP 8. PEP 8 je soubor pravidel a doporučení pro psaní čistého a konzistentního Python kódu. Použití `autopep8` pomáhá udržovat kód lépe čitelný a udržovatelný.

## Co je PEP 8?

PEP 8, zkratka pro Python Enhancement Proposal 8, je dokument, který definuje konvence pro psaní kódu v jazyce Python. Jeho cílem je zlepšit čitelnost a konzistenci kódu napříč různými Python projekty. Autory PEP 8 jsou Guido van Rossum, Barry Warsaw a Nick Coghlan, a dokument byl přijat jako oficiální styl psaní kódu pro Python v roce 2001.

### Historie PEP 8

PEP 8 byl vytvořen během období, kdy Python začal být používán ve velkých softwarových projektech s mnoha vývojáři. Existovala zřejmá potřeba standardizace stylu kódu, aby bylo možné lépe sdílet kód mezi vývojáři z různých částí světa s odlišnými programátorskými zvyklostmi. Standardní konvence usnadnily spolupráci a pomohly novým vývojářům lépe se orientovat v existujícím kódu.

### Zajímavosti o PEP 8

- **Flexibilita pravidel:** PEP 8 je napsán s určitou mírou flexibility. Dokument uvádí, že směrnice nejsou pevné a mohou být ignorovány, pokud má odchýlení od pravidel opodstatněný důvod, který vylepšuje čitelnost konkrétního kódu.

- **Použití v komunitě:** Mnoho open-source projektů a firem využívajících Python jako programovací jazyk přijalo PEP 8 jako standard pro psaní kódu, což demonstruje jeho vliv a přijetí v Python komunitě.

- **Nástroje pro kontrolu dodržování PEP 8:** Existují různé nástroje, jako jsou `pycodestyle` (dříve známý jako `pep8`) a `flake8`, které automaticky kontrolují, zda kód splňuje konvence PEP 8. Tyto nástroje mohou být integrovány do vývojových prostředí nebo použity v rámci automatizovaných testů.

PEP 8 není jen soubor pravidel, ale i nástroj pro zjednodušení spolupráce na globální úrovni a pro udržení kódu čitelným a udržovatelným.


## Instalace autopep8
Než začnete `autopep8` používat ve Visual Studio Code, musíte jej nainstalovat. Instalace se provádí přes pip, správce balíčků Pythonu. Otevřete terminál nebo příkazovou řádku a spusťte následující příkaz:

```bash
pip install autopep8
```

## Nastavení ve Visual Studio Code
Pro integraci autopep8 s Visual Studio Code je potřeba nainstalovat rozšíření Pythonu, pokud již není nainstalováno. Následně je třeba nastavit autopep8 jako výchozí formátovač:

1. Otevřete Visual Studio Code.
1. Jděte do File > Preferences > Settings (nebo Ctrl + ,).
1. Vyhledejte "python formatting provider" a nastavte hodnotu na autopep8.
1. Pro automatické formátování při uložení souboru zaškrtněte možnost Editor: Format On Save.

## Použití autopep8
Po nastavení autopep8 jako formátovače ve vašem VS Code můžete začít formátovat vaše Python soubory. Jednoduše otevřete Python soubor a uložte ho (Ctrl + S), případně použijte klávesovou zkratku Shift + Alt + F pro manuální formátování.

### Příklad
Níže je ukázka kódu před a po formátování s autopep8:

Před:
```py
def some_function(x,y):print('Hello World')
```

Po:
```py
def some_function(x, y):
    print('Hello World')
```

Jak můžete vidět, autopep8 automaticky opravil formátování kódu tak, aby odpovídalo standardům PEP 8, včetně správných mezer a odsazení.



# Použití autopep8 bez Visual Studio Code
Použití autopep8 na konkrétní soubor

Pro formátování Python souboru pomocí autopep8 z příkazové řádky, použijte následující příkaz. Tento příkaz zobrazí upravený kód v terminálu:

```bash
autopep8 cesta/k/souboru.py
```

Chcete-li změny aplikovat přímo na soubor, přidejte přepínač -i, který soubor upraví "in-place":


```bash
autopep8 --in-place cesta/k/souboru.py
```
### Další možnosti
Pro zobrazení dalších možností příkazu autopep8, které můžete využít pro specifické úpravy chování nástroje, spusťte následující příkaz:

```bash
autopep8 --help
```

## Závěr
Použití autopep8 je snadný a efektivní způsob, jak udržovat váš Python kód čistý a v souladu s PEP 8. Toto rozšíření doporučujeme všem vývojářům Pythonu pro zlepšení čitelnosti a kvality jejich kódu.