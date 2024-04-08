# Jak na GitHub a odevzdávání úkolů

## Obsah
1. [Jak na GitHub](#jak-na-github)
2. [Přidání kouče do repozitáře](#p%C5%99id%C3%A1n%C3%AD-kou%C4%8De-do-repozit%C3%A1%C5%99e)
3. [Odevzdávání úkolů](#odevzd%C3%A1v%C3%A1n%C3%AD-%C3%BAkol%C5%AF)


## Jak na GitHub

### Vytvoření repozitáře

1. V první řadě je potřeba si vytvořit účet na stránce [github.com](https://github.com/). K tomu by měla stačit e-mailová adresa a nějaké uživatelské jméno. Pokud už na GitHubu účet máš, nemusíš si zakládat nový.

2. Přihlaš se do svého účtu a vytvoř si nový repozitář kliknutím na symbol `+` v pravém horním rohu:
<img src="../img/new-repository.png" width="300">

3. V dialogu vytváření repozitáře postupuj podle obrázku:
<img src="../img/new-repository-2.jpeg" width="600">

4. Na závěr potvrď stisknutím zeleného tlačítka *Create repository*.

### Jak propojit repozitář na GitHubu s VS Code

1. Otevři VS Code. Pokud už je otevřené, zadej na horní liště *File → New Window*, aby se ti otevřelo úplně nově. Klikni na ikonu papírů v levé liště a pak na *Clone Repository*:
<img src="../img/clone-repository.png" width="400">

2. Klikni na *Clone from GitHub*:
<img src="./img/clone-from-github.png" width="600">

3. V prohlížeči potvrď autorizaci a případně zadej své GitHub přihlašovací údaje:
<img src="../img/authorize-vs-code.png" width="600">

4. Při návratu do VS Code by teď mělo být možné vybrat tvůj repozitář. Klikni na jeho název, a vyber umístění v rámci tvého systému, kam se repozitář stáhne. Složku s repozitářem můžeš rovnou otevřít (možnost *Open*).
<img src="../img/open-cloned-repository.png" width="400">

Hurá, máš propojený repozitář na GitHubu s jeho lokální verzí u tebe na počítači. :tada: Od teď už nemusíš výše uvedené kroky opakovat. Když budeš chtít pracovat na úkolu, otevři si Visual Studio a pak pomocí *Open Folder* otevři složku s tvým repozitářem.

## Přidání kouče do repozitáře

1. Na stránce tvého repozitáře (url by mělo vypadat jako `github.com/<uzivatelske-jmeno>/<nazev-repozitare>`) přejdi do nastavení kliknutím na *Settings*, a dále pak v levé liště klikni na *Collaborators* a pak na *Add people* (tlačítka jsou označeny modrými hvězdičkami):
<img src="../img/add-collaborator.png" width="800">

2. Otevře se okno, do kterého zadej uživatelské jméno tvého kouče (přiřazení ke koučům proběhne na první lekci). Výběr potvrď.

## Odevzdávání úkolů
Jakmile máme vytvořený repozitář na GitHubu a jeho kopii ve VS Code, můžeme nahrávat úkoly a posílat je koučům.

### Vytvoření souboru s úkolem a nahrání na GitHub

1. Ve Visual Studiu vypracuj úkol jako soubor s příponou `.py`, například `ukol-x.py`.

2. Klikni na levé liště na obrázek "větví" (*Source Control*). V sekci *Changes* by se měl nacházet tvůj soubor.
<img src="../img/vs-code-git-1.png" width="400">

3. U souboru, který chceš nahrát, klikni na znamení `+`. Soubor se přesune do sekce *Staged Changes*.
<img src="../img/vs-code-git-2.png" width="400">
<img src="../img/vs-code-git-3.png" width="400">

4. Nyní úkol připravíme k odevzdání, provedeme takzvaný *commit* a nahrajeme změnu na GitHub. Do okýnka nad tlačítko *Commit* napiš krátký popis úkolu, například *Úkol X*. 
<img src="../img/vs-code-git-4.png" width="400">
Následně zvol možnost *Commit & Push*, čímž pošleš soubor nebo jeho změny na GitHub - změna se projeví ihned v tvém repozitáři.
<img src="../img/vs-code-git-5.png" width="600">

