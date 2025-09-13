
def get_todos(filepath = "todos.txt"):
    # Doc Strings are used for documentation in functions for future purposes
    """ This get_todos function is responsible for reading todos file  and returning them """
    with open(filepath) as file:
        local_file = file.readlines()
    return local_file


def write_todos(todos_arg,filepath = "todos.txt"):# this is a default function
    """ This write_todos function is responsible for writing todos file """
    with open(filepath,"w") as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello World")
    print("executes only here ")