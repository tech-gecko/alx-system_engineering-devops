#!/usr/bin/python3
'''
    For a given employee ID, this script returns info about
    his/her TODO list progress using a testing REST API.
'''

if __name__ == "__main__":
    import requests
    import sys

    ID = int(sys.argv[1])
    name_URL = 'https://jsonplaceholder.typicode.com/users' + '/' + str(ID)
    TODOs_URL = 'https://jsonplaceholder.typicode.com/todos'

    r = requests.get(name_URL)
    user_dict = r.json()
    name = user_dict["name"]

    params = {
            "userId": ID
            }
    r = requests.get(TODOs_URL, params=params)
    tasks = r.json()
    total_tasks = len(tasks)
    tasks_done = 0
    for task in tasks:
        if task["completed"] is True:
            tasks_done += 1

    print(
        "Employee {} is done with tasks({}/{}):"
        .format(name, tasks_done, total_tasks)
    )

    for task in tasks:
        if task["completed"] is True:
            print("\t {}".format(task["title"]))
