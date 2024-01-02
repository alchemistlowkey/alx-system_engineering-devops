#!/usr/bin/python3
"""
A Python script that, using this
https://intranet.alxswe.com/rltoken/7cr7aLYdaWAZWBKrBKS12A,
for a given employee ID, returns information about his/her TODO list progress
"""

import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    my_endpoint = "{}users/{}".format(url, argv[1])
    my_response = requests.get(my_endpoint)
    my_data = my_response.json()
    get_employee_name = my_data.get("name")

    main_endpoint = "{}todos?userId={}".format(url, argv[1])
    main_response = requests.get(main_endpoint)
    main_tasks = main_response.json()

    tasks = []
    for task in main_tasks:
        if task.get("completed"):
            tasks.append(task)

    tasks_count = len(main_tasks)

    completed_tasks = len(tasks)

    print("Employee {} is done with tasks({}/{}):".format(get_employee_name,
                                                          completed_tasks,
                                                          tasks_count))

    for task in tasks:
        print("\t {}".format(task.get("title")))
