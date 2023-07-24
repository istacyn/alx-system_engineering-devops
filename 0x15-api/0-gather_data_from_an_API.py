#!/usr/bin/python3
"""Returns information about employee's TODO list progress"""
from requests import get
from sys import argv


def todo(employee_id):
    """
    Fetches the employee's TODO list progress
    from a REST API and prints the information.
    """
    total = 0
    completed = 0
    user_url = 'https://jsonplaceholder.typicode.com/users/'
    todo_url = 'https://jsonplaceholder.typicode.com/todos/'

    # check if user exists
    user = get(user_url + employee_id).json().get('name')

    if user:
        params = {'userId': employee_id}
        #  get all tasks
        tasks = get(todo_url, params=params).json()
        if tasks:
            total = len(tasks)
            #  get number of completed tasks
            params.update({'completed': 'true'})
            completed = len(get(todo_url, params=params).json())

        print("Employee {} is done with tasks({}/{}):".format(
            user, completed, total))
        for task in tasks:
            if task.get('completed') is True:
                print("\t {}".format(task.get('title')))


if __name__ == '__main__':
    if len(argv) > 1:
        todo(argv[1])
