#!/usr/bin/python3
"""Exports some data in the CSV format.
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
    file_name = f'{user_id}.csv'
    # Get username of user
    url2 = f'{base_url}/users/{user_id}'
    with urllib.request.urlopen(url2) as response:
        body = response.read()
        decoded_body = body.decode('utf-8')
        user_info_dict = json.loads(decoded_body)
        username = user_info_dict.get('username')
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks_list:
            csv_data_list = []
            csv_data_list.append(user_id)
            csv_data_list.append(username)
            csv_data_list.append(task.get('completed'))
            csv_data_list.append(task.get('title'))
            writer.writerow(csv_data_list)
