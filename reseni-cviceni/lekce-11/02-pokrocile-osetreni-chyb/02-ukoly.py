def load_tasks(filename):
    try:
        with open(filename, "r") as file:
            tasks = [line.strip() for line in file]
        print("Úkoly byly načteny.")
        return tasks
    except FileNotFoundError:
        print(f"Soubor {filename} neexistuje, bude založen při přidání prvního úkolu.")
        return []


def add_task(tasks):
    task = input("Zadejte název úkolu: ")
    priority = int(input("Zadejte prioritu úkolu (1=vysoká, 2=střední, 3=nízká): "))
    if priority not in [1, 2, 3]:
        raise ValueError("Priorita musí být číslo 1, 2, nebo 3.")
    tasks.append(f"{task},{priority}")


def save_tasks(filename, tasks):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")
        print("Úkoly byly uloženy do souboru.")


filename = "tasks.txt"
tasks = load_tasks(filename)

try:
    add_task(tasks)
    save_tasks(filename, tasks)
except ValueError as e:
    print(e)
