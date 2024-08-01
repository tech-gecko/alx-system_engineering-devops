#!/usr/bin/python3
'''
    This script also exports all employee data
    (from an API for testing and prototyping) in JSON format
    to a file, "todo_all_employees.json".
'''

if __name__ == "__main__":
    import json
    import requests

    users_URL = 'https://jsonplaceholder.typicode.com/users'
    TODOs_URL = 'https://jsonplaceholder.typicode.com/todos'

    r = requests.get(users_URL)
    users_dict = r.json()

    r = requests.get(TODOs_URL)
    tasks = r.json()

    '''Export happens here.'''
    with open('todo_all_employees.json', mode='w') as file:
        data = {
            user["id"]: [
                {
                    "username": user["username"],
                    "task": task["title"],
                    "completed": task["completed"]
                } for task in tasks if task["userId"] == user["id"]
            ] for user in users_dict
        }

        json.dump(data, file)
