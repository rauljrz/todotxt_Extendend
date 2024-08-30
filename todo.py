"""Módulo para gestionar tareas en formato todo.txt con funcionalidades extendidas."""

import argparse
import datetime
import re
import os
from typing import List

TODO_FILE = "todo.txt"
DONE_FILE = "done.txt"
HELP_FILE = "todohelp.txt"

def parse_arguments():
    """Analiza y devuelve los argumentos de línea de comandos."""
    parser = argparse.ArgumentParser(
        description="Extended todo.txt Management Script", add_help=False)
    parser.add_argument("--add", "-a", help="Add a new task")
    parser.add_argument("--start", "-s", type=int, help="Mark a task as in progress")
    parser.add_argument("--pause", "-P", type=int, help="Pause a task")
    parser.add_argument("--complete", "-C", type=int, help="Mark a task as completed")
    parser.add_argument("--list", "-l", action="store_true", help="List tasks")
    parser.add_argument("--archive", "-A", action="store_true",
        help="Move completed tasks to done.txt")
    parser.add_argument("--order", "-o", help="Sort tasks")
    parser.add_argument("--delete", "-D", type=int, help="Delete a task")
    parser.add_argument("--filter", "-f", help="Filter tasks")
    parser.add_argument("--reverse", "-R", action="store_true", help="Reverse sort order")
    parser.add_argument("--help", "-h", action="store_true", help="Show help")
    parser.add_argument("--manual", "-m", action="store_true", help="Show extended help")
    return parser.parse_args()

def read_tasks(filename: str) -> List[str]:
    """Lee y devuelve las tareas desde un archivo."""
    if not os.path.exists(filename):
        return []
    # Start of Selection
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip() for line in file]

def write_tasks(filename: str, tasks: List[str]):
    """Escribe las tareas en un archivo."""
    with open(filename, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(f"{task}\n")

def parse_date(date_str: str) -> str:
    """Analiza y devuelve la fecha correspondiente a una cadena de texto."""
    today = datetime.date.today()
    date_map = {
        "today": today,
        "ty": today,
        "tomorrow": today + datetime.timedelta(days=1),
        "tomow": today + datetime.timedelta(days=1),
        "tw": today + datetime.timedelta(days=1),
        "year": today + datetime.timedelta(days=365),
        "nextweek": today + datetime.timedelta(days=7),
        "nextwk": today + datetime.timedelta(days=7),
        "nextmonth": (today.replace(day=1) + datetime.timedelta(days=32)).replace(day=1)
    }
    if date_str in date_map:
        return date_map[date_str].strftime("%Y-%m-%d")
    if date_str.startswith("next"):
        days = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3,
                 "friday": 4, "saturday": 5, "sunday": 6}
        day = date_str[4:].lower()
        if day in days:
            days_ahead = (days[day] - today.weekday() + 7) % 7 or 7
            return (today + datetime.timedelta(days=days_ahead)).strftime("%Y-%m-%d")
    return date_str

def add_task(task: str) -> int:
    """Agrega una nueva tarea al archivo todo.txt."""
    tasks = read_tasks(TODO_FILE)
    today = datetime.date.today().strftime("%Y-%m-%d")

    # Parse task components
    priority_match = re.search(r'\(([A-Z])\)', task)
    priority = priority_match.group(1) if priority_match else None
    context_match = re.findall(r'@(\w+)', task)
    project_match = re.findall(r'\+(\w+)', task)
    tag_match = re.findall(r'#(\w+)', task)

    # Check for due date keywords
    due_date = None
    for keyword in ["today", "ty", "tomorrow", "tomow", "tw", "year",
                    "nextweek", "nextwk", "nextmonth", "nextmonday",
                    "nexttuesday", "nextwednesday", "nextthursday",
                    "nextfriday", "nextsaturday", "nextsunday"]:
        if keyword in task.lower():
            due_date = parse_date(keyword)
            task = task.replace(keyword, "").strip()
            break

    rec_match = re.search(r'rec:(\d+[dwmy])', task)
    rec = rec_match.group(1) if rec_match else None

    # Remove parsed components from description
    description = re.sub(r'\([A-Z]\)|\s@\w+|\s\+\w+|\s#\w+|rec:\d+[dwmy]', '', task).strip()

    # Construct new task
    new_task = f"{priority and f'({priority}) ' or ''}{today} {description}"
    new_task += f"{' '.join(f' @{c}' for c in context_match)}"
    new_task += f"{' '.join(f' +{p}' for p in project_match)}"
    new_task += f"{' '.join(f' #{t}' for t in tag_match)}"
    new_task += f"{due_date and f' due:{due_date}' or ''}"
    new_task += f"{rec and f' rec:{rec}' or ''}"

    tasks.append(new_task.strip())
    write_tasks(TODO_FILE, tasks)
    return len(tasks)

def start_task(task_id: int):
    """Marca una tarea como en progreso."""
    tasks = read_tasks(TODO_FILE)
    if 1 <= task_id <= len(tasks):
        for i, task in enumerate(tasks):
            if not task.startswith(("#", "//")) and "[=]" in task:
                tasks[i] = task.replace("[=]", "")
                print(f"Task {task_id} resumed.")
        if not tasks[task_id - 1].startswith(("#", "//")):
            start_time = datetime.datetime.now().strftime('%H%M')
            tasks[task_id - 1] = tasks[task_id - 1].strip() + f" [=] start:{start_time}"
            print(f"Task {task_id} started.")
        write_tasks(TODO_FILE, tasks)
    else:
        print(f"Invalid task ID: {task_id}")

def pause_task(task_id: int):
    """Pausa una tarea en progreso."""
    tasks = read_tasks(TODO_FILE)
    if 1 <= task_id <= len(tasks):
        task = tasks[task_id - 1]
        if not task.startswith(("#", "//")) and "[=]" in task:
            end_time = datetime.datetime.now().strftime("%H%M")
            start_time_match = re.search(r'start:(\d{4})', task)
            if start_time_match:
                start_time = datetime.datetime.strptime(start_time_match.group(1), "%H%M")
                end_time_obj = datetime.datetime.strptime(end_time, "%H%M")
                time_spent = end_time_obj - start_time
                spent_str = f"{time_spent.seconds//3600:02d}{(time_spent.seconds % 3600)//60:02d}"
                tasks[task_id - 1] = task.replace("[=]", "[?]").replace(
                    f"start:{start_time_match.group(1)}",
                    f"start:{start_time_match.group(1)} end:{end_time} spent:{spent_str}"
                )

                print(f"Task {task_id} paused.")
            else:
                tasks[task_id - 1] = task.replace("[=]", "[?]")
                print(f"Task {task_id} paused. - ")
            write_tasks(TODO_FILE, tasks)
        else:
            print("This task is not currently in progress or is a comment.")
    else:
        print(f"Invalid task ID: {task_id}")

def complete_task(task_id: int):
    """Marca una tarea como completada."""
    tasks = read_tasks(TODO_FILE)
    done_tasks = read_tasks(DONE_FILE)
    if 1 <= task_id <= len(tasks):
        task = tasks[task_id - 1]
        if not task.startswith(("#", "//")):
            tasks.pop(task_id - 1)
            today = datetime.date.today().strftime("%Y-%m-%d")
            priority_match = re.search(r'\(([A-Z])\)', task)
            priority = f"({priority_match.group(1)}) " if priority_match else ""
            creation_date_match = re.search(r'(\d{4}-\d{2}-\d{2})', task)
            creation_date = creation_date_match.group(1) if creation_date_match else ""
            completed_task = f"x {priority}{today} {creation_date} {task.split(' ', 2)[-1]}"
            done_tasks.append(completed_task)
            write_tasks(TODO_FILE, tasks)
            write_tasks(DONE_FILE, done_tasks)
            print(f"Task {task_id} completed.")
        else:
            print("Cannot complete a comment task.")
    else:
        print(f"Invalid task ID: {task_id}")

def list_tasks(filter_str: str = None, order_by: str = None, reverse: bool = False):
    """Lista las tareas según los criterios de filtrado y ordenamiento."""
    tasks = read_tasks(TODO_FILE)

    if filter_str:
        tasks = filter_tasks(tasks, filter_str)

    if order_by:
        tasks = sort_tasks(tasks, order_by, reverse)

    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def filter_tasks(tasks: List[str], filter_str: str) -> List[str]:
    """Filtra las tareas según el criterio especificado."""
    filtered_tasks = []
    for task in tasks:
        if task.startswith(("#", "//")):
            continue
        if (filter_str.startswith("p:") and f"({filter_str[2:].upper()})" in task) or \
           (filter_str.startswith("y:") and f"+{filter_str[2:]}" in task) or \
           (filter_str.startswith("c:") and f"@{filter_str[2:]}" in task) or \
           (filter_str.startswith("t:") and f"#{filter_str[2:]}" in task) or \
           (filter_str.startswith("s:") and filter_by_status([task], filter_str[2:])) or \
           (filter_str.lower() in task.lower()):
            filtered_tasks.append(task)
    return filtered_tasks

def filter_by_status(tasks: List[str], status: str) -> List[str]:
    """Filtra las tareas por estado."""
    status_map = {
        "debt": lambda t: "[?]" not in t and "[=]" not in t and not t.startswith("x"),
        "done": lambda t: t.startswith("x"),
        "paused": lambda t: "[?]" in t,
        "now": lambda t: "[=]" in t
    }
    return [t for t in tasks if not t.startswith(("#", "//"))
            and status_map.get(status, lambda _: True)(t)]

def sort_tasks(tasks: List[str], order_by: str, reverse: bool) -> List[str]:
    """Ordena las tareas según el criterio especificado."""
    order_key = order_by.lower().rstrip('-')
    print("por ordenar: ", order_key)
    if order_key in ["p", "priority"]:
        tasks.sort(key=lambda t: re.search(r'\(([A-Z])\)', t).group(1)
                   if re.search(r'\(([A-Z])\)', t) else "Z")
        print("Ordenado por prioridad.")
    elif order_key in ["y", "project"]:
        tasks.sort(key=lambda t: re.search(r'\+(\w+)', t).group(1)
                   if re.search(r'\+(\w+)', t) else "")
    elif order_key in ["c", "context"]:
        tasks.sort(key=lambda t: re.search(r'@(\w+)', t).group(1)
                   if re.search(r'@(\w+)', t) else "")
    elif order_key in ["t", "tag"]:
        tasks.sort(key=lambda t: re.search(r'#(\w+)', t).group(1)
                   if re.search(r'#(\w+)', t) else "")
    elif order_key in ["s", "status"]:
        tasks.sort(key=status_key)

    if order_by.endswith('-') or reverse:
        tasks.reverse()

    return tasks

def status_key(task: str) -> int:
    """Devuelve una clave numérica para ordenar por estado."""
    if task.startswith("x"):
        return 0
    if "[=]" in task:
        return 1
    if "[?]" in task:
        return 2
    return 3
def archive_tasks():
    """Mueve las tareas completadas al archivo done.txt."""
    tasks = read_tasks(TODO_FILE)
    done_tasks = read_tasks(DONE_FILE)
    completed_tasks = [t for t in tasks if t.startswith("x") and not t.startswith(("#", "//"))]
    tasks = [t for t in tasks if not t.startswith("x") or t.startswith(("#", "//"))]
    done_tasks.extend(completed_tasks)
    write_tasks(TODO_FILE, tasks)
    write_tasks(DONE_FILE, done_tasks)

def delete_task(task_id: int):
    """Elimina una tarea del archivo todo.txt."""
    tasks = read_tasks(TODO_FILE)
    if 1 <= task_id <= len(tasks):
        if not tasks[task_id - 1].startswith(("#", "//")):
            del tasks[task_id - 1]
            write_tasks(TODO_FILE, tasks)
            print(f"Task {task_id} deleted.")
        else:
            print("Cannot delete a comment task.")
    else:
        print(f"Invalid task ID: {task_id}")

def show_help(extended: bool = False):
    """Muestra la ayuda para el script."""
    if extended and os.path.exists(HELP_FILE):
        with open(HELP_FILE, 'r', encoding="utf-8") as file:
            print(file.read())
    else:
        print("Todo.txt Extended Management Script")
        print("Usage:")
        print("  --add, -a TEXT    Add a new task")
        print("  --start, -s ID    Mark a task as in progress")
        print("  --pause, -P ID    Pause a task")
        print("  --complete, -C ID Complete a task")
        print("  --list, -l        List tasks")
        print("  --archive, -A     Archive completed tasks")
        print("  --order, -o FIELD Order tasks")
        print("  --delete, -D ID   Delete a task")
        print("  --filter, -f TEXT Filter tasks")
        print("  --reverse, -R     Reverse sort order")
        print("  --help, -h        Show this help")
        print("  --manual, -m      Show extended help")

def main():
    """Función principal del script."""
    args = parse_arguments()
    if args.help:
        show_help()
    elif args.manual:
        show_help(extended=True)
    elif args.add:
        new_id = add_task(args.add)
        print(f"Task added with ID: {new_id}")
    elif args.start:
        start_task(args.start)
    elif args.pause:
        pause_task(args.pause)
    elif args.complete:
        complete_task(args.complete)
    elif args.list:
        list_tasks(args.filter, args.order, args.reverse)
    elif args.archive:
        archive_tasks()
    elif args.order:
        list_tasks(order_by=args.order, reverse=args.reverse)
    elif args.delete:
        delete_task(args.delete)
    else:
        print("No valid command provided. Use --help for usage information.")

if __name__ == "__main__":
    main()
