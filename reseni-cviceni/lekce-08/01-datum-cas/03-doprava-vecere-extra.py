from datetime import datetime, timedelta
import sys

def validate_duration(duration_str):
    """
    Převede řetězec představující dobu trvání na timedelta objekt.
    
    Args:
        duration_str (str): Doba trvání ve formátu 'minuty sekundy' (např. '30 0').
    
    Returns:
        timedelta: Objekt timedelta odpovídající zadané době trvání.
        
    Raises:
        ValueError: V případě, že řetězec není ve správném formátu nebo obsahuje neplatné číselné hodnoty.
    """
    try:
        minutes, seconds = map(int, duration_str.split(" "))
        return timedelta(minutes=minutes, seconds=seconds)
    except ValueError:
        print("Chyba: Nesprávný formát doby, správný formát je 'minuty sekundy' (např. '30 0').")
        sys.exit(1)

def calculate_delivery_time(order_time_str, acceptance_duration_str, preparation_duration_str, delivery_duration_str):
    """
    Vypočítá očekávaný čas doručení jídla na základě zadaného času objednávky a dob trvání jednotlivých kroků.
    
    Args:
        order_time_str (str): Čas objednání ve formátu '13. November 2020 19:47'.
        acceptance_duration_str (str): Doba potřebná pro převzetí objednávky ve formátu 'minuty sekundy'.
        preparation_duration_str (str): Doba potřebná pro přípravu jídla ve formátu 'minuty sekundy'.
        delivery_duration_str (str): Doba potřebná pro doručení jídla ve formátu 'minuty sekundy'.
    
    Returns:
        str: Očekávaný čas doručení ve formátu '13. November 2020 19:47'.
        
    Raises:
        ValueError: V případě nesprávného formátu času objednání nebo doby trvání.
    """
    try:
        order_time = datetime.strptime(order_time_str, "%d. %B %Y %H:%M")
    except ValueError:
        print("Chyba: Nesprávný formát data, očekávaný formát je '13. November 2020 19:47'.")
        sys.exit(1)

    acceptance_duration = validate_duration(acceptance_duration_str)
    preparation_duration = validate_duration(preparation_duration_str)
    delivery_duration = validate_duration(delivery_duration_str)

    total_duration = acceptance_duration + preparation_duration + delivery_duration
    delivery_time = order_time + total_duration

    return delivery_time.strftime("%d. %B %Y %H:%M")

if __name__ == "__main__":
    order_time = "13. November 2020 19:47"
    acceptance_duration = "8 35"
    preparation_duration = "30 0"
    delivery_duration = "25 30"

    expected_delivery_time = calculate_delivery_time(order_time, acceptance_duration, preparation_duration, delivery_duration)
    print("Očekávaný čas doručení:", expected_delivery_time)
