import requests


def fetch_data(url):
    """Načte data z API a vrátí je jako Python slovník."""
    try:
        with requests.get(url) as response:
            response.raise_for_status()  # Vyvolá výjimku pro HTTP chybové kódy
            return response.json()
    except requests.RequestException as e:
        print(f"Chyba při načítání dat z API: {e}")
        return None


def analyze_data(data):
    """Analyzuje data a vypisuje relevantní informace."""
    if not data:
        print("Nebyla obdržena žádná data k analýze.")
        return

    # Zjistit celkový počet lidí
    total_people = len(data)
    print("Celkový počet lidí:", total_people)

    # Zjistit, jaké všechny informace máme o jednotlivých osobách
    if total_people > 0:
        print("Informace dostupné o osobách:", list(data[0].keys()))

    # Zjistit počet mužů a žen
    male_count = sum(1 for person in data if person.get("gender") == "Male")
    female_count = sum(1 for person in data if person.get("gender") == "Female")
    print("Počet mužů:", male_count)
    print("Počet žen:", female_count)


if __name__ == "__main__":
    url = "https://api.kodim.cz/python-data/people"
    data = fetch_data(url)
    analyze_data(data)
