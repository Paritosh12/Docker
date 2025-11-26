import sys

TASKS = []

def add_task(task):
    TASKS.append(task)
    return task

def list_tasks():
    return TASKS

def main():
    if len(sys.argv) < 2:
        print("Usage: python app.py [add <task> | list]")
        return

    cmd = sys.argv[1]

    if cmd == "add":
        if len(sys.argv) < 3:
            print("Task cannot be empty")
            return
        task = add_task(sys.argv[2])
        print(f"Task added: {task}")

    elif cmd == "list":
        print("Tasks:")
        for t in list_tasks():
            print(f"- {t}")

if __name__ == "__main__":
    main()
