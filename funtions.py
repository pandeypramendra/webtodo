
FILEPATH="todos.txt"

def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as file_local:
        todo_local=file_local.readlines()
        return todo_local

def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath,"w") as file_local:
        file_local.writelines(todos_arg)