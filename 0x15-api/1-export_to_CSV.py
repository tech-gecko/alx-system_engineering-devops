#!/usr/bin/python3
'''
    For a given employee ID, this script returns info about
    his/her TODO list progress using a testing REST API.

    This script also exports employee data in CSV format to
    a file, "<USER_ID>.csv".
'''

if __name__ == "__main__":
    import csv
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

    '''Export happens here'''
    file_name = str(ID) + '.csv'
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for task in tasks:
            data = [
                str(user_dict["id"]),
                str(user_dict["username"]),
                str(task["completed"]),
                str(task["title"])
            ]

            writer.writerow(data)