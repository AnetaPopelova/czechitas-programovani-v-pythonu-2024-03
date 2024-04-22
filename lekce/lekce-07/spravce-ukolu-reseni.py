# Import modulu datetime pro práci s časovými údaji
import datetime

# Definice třídy Task, která reprezentuje úkol
class Task:
    def __init__(self, description):
        self.description = description  # Popis úkolu
        self.timestamp = datetime.datetime.now()  # Časové razítko přidání úkolu

# Slovník pro ukládání úkolů, kde klíče jsou ID úkolů a hodnoty jsou instance třídy Task
tasks = {}
last_id = 0  # Proměnná pro uchování posledního použitého ID


# Funkce pro přidání nového úkolu
def add_task(description):
    global last_id
    last_id += 1    
    tasks[last_id] = Task(description)  # Uložení úkolu do slovníku
    print(f"Task added with ID: {last_id}")  # Výpis zprávy o úspěšném přidání

# Funkce pro odstranění úkolu
def remove_task(task_id):
    if task_id in tasks:  # Kontrola, zda úkol s daným ID existuje
        del tasks[task_id]  # Odstranění úkolu ze slovníku
        print(f"Task {task_id} removed")  # Výpis zprávy o úspěšném odstranění
    else:
        print("Task not found")  # Výpis zprávy, pokud úkol nebyl nalezen

# Funkce pro zobrazení všech úkolů
def show_tasks():
    for task_id, task in tasks.items():  # Iterace přes všechny úkoly v slovníku
        print(f"{task_id}: {task.description} added on {task.timestamp}")  # Výpis ID, popisu a času přidání úkolu

# Hlavní funkce aplikace
def main():
    while True:  # Neustálý cyklus pro zpracování příkazů uživatele
        command = input("Enter command (add, remove, show): ")  # Vstup příkazu od uživatele
        if command == 'add':  # Příkaz pro přidání úkolu
            description = input("Enter task description: ")  # Získání popisu úkolu od uživatele
            add_task(description)  # Volání funkce add_task
        elif command == 'remove':  # Příkaz pro odstranění úkolu
            task_id = int(input("Enter task ID to remove: "))  # Získání ID úkolu, který má být odstraněn
            remove_task(task_id)  # Volání funkce remove_task
        elif command == 'show':  # Příkaz pro zobrazení úkolů
            show_tasks()  # Volání funkce show_tasks
        else:
            print("Unknown command")  # Zpráva pro neznámý příkaz

# Kontrola, zda je skript spuštěn jako hlavní program
if __name__ == "__main__":
    main()
