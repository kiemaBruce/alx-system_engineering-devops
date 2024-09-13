#!/usr/bin/python3
"""Exports some data in the JSON format.
"""


if __name__ == "__main__":
    import csv
    import json
    import sys
    import urllib.request

    base_url = "https://jsonplaceholder.typicode.com/"
    url = f"{base_url}/users"
    # Get all users
    with urllib.request.urlopen(url) as response:
        body = response.read()
        decoded_body = body.decode('utf-8')
        all_users_list = json.loads(decoded_body)
    file_name = "todo_all_employees.json"
    final_dict = {}
    for user in all_users_list:
        # Get username of user and their id
        username = user.get('username')
        user_id = user.get('id')
        # Get all tasks for current user
        url = f"{base_url}/users/{user_id}/todos"
        with urllib.request.urlopen(url) as response:
            body = response.read()
            decoded_body = body.decode('utf-8')
            tasks_list = json.loads(decoded_body)
        data_dict = {}
        my_list = []
        for task in tasks_list:
            my_dict = {}
            my_dict['task'] = task.get('title')
            my_dict['completed'] = task.get('completed')
            my_dict['username'] = username
            my_list.append(my_dict)
        final_dict[user_id] = my_list
    with open(file_name, mode='w', newline='') as file:
        json.dump(final_dict, file)
