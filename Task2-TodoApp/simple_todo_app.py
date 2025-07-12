import json
import os

# my todo list will be saved here
todo_file = "my_todos.json"

# function to load todos from file
def load_todos():
    if os.path.exists(todo_file):
        try:
            with open(todo_file, 'r') as f:
                return json.load(f)
        except:
            return []
    else:
        return []

# function to save todos to file
def save_todos(todos):
    with open(todo_file, 'w') as f:
        json.dump(todos, f)

# function to show all todos
def show_todos():
    todos = load_todos()
    if len(todos) == 0:
        print("No tasks yet!")
        return
    
    print("\nYour Todo List:")
    print("-" * 20)
    for i, todo in enumerate(todos, 1):
        status = "DONE" if todo['done'] else "NOT DONE"
        print(f"{i}. {todo['task']} - {status}")
    print("-" * 20)

# function to add new todo
def add_todo():
    task = input("Enter your task: ")
    todos = load_todos()
    new_todo = {
        'task': task,
        'done': False
    }
    todos.append(new_todo)
    save_todos(todos)
    print(f"Task '{task}' added!")

# function to mark todo as done
def mark_done():
    todos = load_todos()
    if len(todos) == 0:
        print("No tasks to mark as done!")
        return
    
    show_todos()
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(todos):
            todos[num-1]['done'] = True
            save_todos(todos)
            print("Task marked as done!")
        else:
            print("Invalid task number!")
    except:
        print("Please enter a valid number!")

# function to delete todo
def delete_todo():
    todos = load_todos()
    if len(todos) == 0:
        print("No tasks to delete!")
        return
    
    show_todos()
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(todos):
            deleted_task = todos.pop(num-1)
            save_todos(todos)
            print(f"Task '{deleted_task['task']}' deleted!")
        else:
            print("Invalid task number!")
    except:
        print("Please enter a valid number!")

# main menu
def show_menu():
    print("\n=== My Todo App ===")
    print("1. Show all tasks")
    print("2. Add new task")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")
    print("=================")

# main program
def main():
    print("Welcome to My Todo App!")
    
    while True:
        show_menu()
        choice = input("What do you want to do? (1-5): ")
        
        if choice == '1':
            show_todos()
        elif choice == '2':
            add_todo()
        elif choice == '3':
            mark_done()
        elif choice == '4':
            delete_todo()
        elif choice == '5':
            print("Bye bye!")
            break
        else:
            print("Please choose 1, 2, 3, 4, or 5!")
        
        input("Press Enter to continue...")
        

# run the program
if __name__ == "__main__":
    main()