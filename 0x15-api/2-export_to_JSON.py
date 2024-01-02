#!/usr/bin/python3
"""
A Python script to export data in JSON format
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    my_endpoint = "{}users/{}".format(url, argv[1])
    my_response = requests.get(my_endpoint)
    my_data = my_response.json()
    get_employee_name = my_data.get("username")

    main_endpoint = "{}todos?userId={}".format(url, argv[1])
    main_response = requests.get(main_endpoint)
    main_tasks = main_response.json()

    json_format = "{}.json".format(argv[1])
    data_format = {argv[1]: []}
    for task in main_tasks:
        data_format[argv[1]].append({"task": task.get("title"),
                                     "completed": task.get("completed"),
                                     "username": get_employee_name})

    with open("{}.json".format(argv[1]), mode="w") as f:
        json.dump(data_format, f)
