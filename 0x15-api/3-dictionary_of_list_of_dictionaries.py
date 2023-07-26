#!/usr/bin/python3
"""Returns information about employee's
TODO list progress in JSON format
"""
from json import dump
from requests import get
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = get(url + "users").json()

    with open("todo_all_employees.json", "w") as file:
        dump({
            user.get("id"): [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user.get("username")
            } for task in get(url + "todos", params={"userId": user.get("id")}).json()]
            for user in users}, file)
