#!/usr/bin/python3
"""Returns information about employee's
TODO list progress in CVS format
"""
from csv import writer, QUOTE_ALL
from requests import get
from sys import argv


def todo_csv(employee_id):
    """
    Fetches the employee's TODO list progress
    from a REST API and prints the information.
    """
    file_name = "{}.csv".format(employee_id)
    user_url = 'https://jsonplaceholder.typicode.com/users/'
    todo_url = 'https://jsonplaceholder.typicode.com/todos/'

    user = get(user_url + employee_id).json().get("username")

    if user:
        params = {"userId": employee_id}
        tasks = get(todo_url, params=params).json()
        if tasks:
            with open(file_name, "w", newline="", encoding="utf8") as f:
                task_writer = writer(f, quoting=QUOTE_ALL)
                for task in tasks:
                    task_writer.writerow([employee_id, user, task.get
                                         ("completed"), task.get("title")])


if __name__ == '__main__':
    if len(argv) > 1:
        todo_csv(argv[1])
