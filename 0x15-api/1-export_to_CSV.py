#!/usr/bin/python3
"""
A Python script to export data in the CSV format
"""

import csv
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

    with open("{}.csv".format(argv[1]), mode="w") as f:
        for task in main_tasks:
            f.write('"{}","{}","{}","{}"\n'.format(argv[1], get_employee_name,
                                                   task.get("completed"),
                                                   task.get("title")))
