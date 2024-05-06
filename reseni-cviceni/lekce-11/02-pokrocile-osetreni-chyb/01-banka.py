from datetime import datetime


def read_balance():
    try:
        with open("balance.txt", "r") as file:
            return float(file.read().strip())
    except Exception as e:
        print(f"Chyba při čtení souboru: {e}")
        exit()


def write_balance(new_balance):
    try:
        with open("balance.txt", "w") as file:
            file.write(f"{new_balance}\n")
    except Exception as e:
        print(f"Chyba při zápisu do souboru: {e}")
        exit()


try:
    # Načtení aktuálního zůstatku
    account_balance = read_balance()

    # Žádost o částku k převodu
    amount = float(input("Zadejte částku k převodu: "))

    # Kontrola, zda je částka k převodu platná
    if amount < 0:
        raise ValueError("Částka k převodu nesmí být záporná.")
    if amount > account_balance:
        raise ValueError("Částka k převodu přesahuje zůstatek na účtu.")

    # Výpočet nového zůstatku a zápis do souboru
    new_balance = account_balance - amount
    write_balance(new_balance)
    print(f"Převod proběhl úspěšně. Nový zůstatek je: {new_balance} Kč")

except ValueError as e:
    print(e)
except Exception as e:
    print(f"Neočekávaná chyba: {e}")
