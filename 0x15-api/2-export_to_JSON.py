#!/usr/bin/python3
"""Exports some data in the JSON format.
"""


if __name__ == "__main__":
    import csv
    import json
    import sys
    import urllib.request

    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    url = f"{base_url}/users/{user_id}/todos"
    # Get all tasks for user
    with urllib.request.urlopen(url) as response:
        body = response.read()
        decoded_body = body.decode('utf-8')
        tasks_list = json.loads(decoded_body)
    # Get username of user
    url2 = f'{base_url}/users/{user_id}'
    with urllib.request.urlopen(url2) as response:
        body = response.read()
        decoded_body = body.decode('utf-8')
        user_info_dict = json.loads(decoded_body)
        username = user_info_dict.get('username')
    file_name = f'{user_id}.json'
    data_dict = {}
    my_list = []
    for task in tasks_list:
        my_dict = {}
        my_dict['task'] = task.get('title')
        my_dict['completed'] = task.get('completed')
        my_dict['username'] = username
        my_list.append(my_dict)
    final_dict = {}
    final_dict[user_id] = my_list
    with open(file_name, mode='w', newline='') as file:
        json.dump(final_dict, file)
