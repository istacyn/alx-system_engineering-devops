#!/usr/bin/python3
"""Returns information about employee's TODO list progress"""
from requests import get
from sys import argv


def employee_todo(employee_id):
    """
    Fetches the employee's TODO list progress
    from a REST API and prints the information.
    """
    total_tasks = 0
    completed = 0

    user_url = "https://jsonplaceholder.typicode.com/users"
    todo_url = "https://jsonplaceholder.typicode.com/todos"

    user = get(user_url + employee_id).json().get("name")

    if user:
        param = {"user_id": employee_id}

        tasks = get(todo_url, param=param).json()
        if tasks:
            total_tasks = len(tasks)
            param.update({"completed": "true"})
            completed = len(get(todo_url, param=param).json())

        print("Employee {} is done with tasks ({}/{}):"
              .format(user, completed, total_tasks))

        for task in tasks:
            if task.get("completed") is True:
                print("\t {}".format(task.get("title")))


if __name__ == '__main__':
    if len(argv) > 1:
        employee_todo(argv[1])
