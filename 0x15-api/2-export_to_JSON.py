#!/usr/bin/python3
"""Returns information about employee's
TODO list progress in JSON format
"""
from json import dump
from requests import get
from sys import argv


def todo_json(employee_id):
    """
    Fetches the employee's TODO list progress
    from a REST API and prints the information.
    """
    file_name = "{}.json".format(employee_id)
    user_url = 'https://jsonplaceholder.typicode.com/users/'
    todo_url = 'https://jsonplaceholder.typicode.com/todos/'

    user = get(user_url + employee_id).json().get("username")

    if user:
        params = {"userId": employee_id}
        tasks = get(todo_url, params=params).json()

        todo_list = []
        for task in tasks:
            todo_list.append({"task": task.get("title"),
                             "completed": task.get("completed"),
                              "username": user})

        with open(file_name, "w", encoding="utf8") as f:
            dump({employee_id: todo_list}, f)


if __name__ == "__main__":
    if len(argv) > 1:
        todo_json(argv[1])
