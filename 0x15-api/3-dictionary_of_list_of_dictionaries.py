#!/usr/bin/python3
"""Returns information about employee's
TODO list progress in JSON format
"""
from json import dump
from requests import get
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"

    users = get(url + "users").json()

    dictionary = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
        url = url + "todos"
        response = requests.get(url)
        tasks = response.json()
        dictionary[user_id] = []
        for task in tasks:
            dictionary[user_id].append({
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            })
    with open("todo_all_employees.json", "w") as file:
        dump(dictionary, file)
