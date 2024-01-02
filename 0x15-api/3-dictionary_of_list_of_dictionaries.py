#!/usr/bin/python3
"""
A Python script to export data in JSON format
"""

import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    my_response = requests.get(url + "users")
    my_data = my_response.json()

    datas = {}

    for users in my_data:
        user_id = users.get("id")
        username = users.get("username")

        url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
        todos_url = url + "/todos/"
        response_url = requests.get(todos_url)
        tasks = response_url.json()
        datas[user_id] = []
        for task in tasks:
            datas[user_id].append({"task": task.get("title"),
                                   "completed": task.get("completed"),
                                   "username": username})

    with open("todo_all_employees.json", mode="w") as f:
        json.dump(datas, f)
