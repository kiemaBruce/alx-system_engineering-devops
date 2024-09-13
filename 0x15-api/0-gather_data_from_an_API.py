#!/usr/bin/python3
"""Gathers and displays employee data from a REST API
"""


if __name__ == "__main__":
    import json
    import sys
    import urllib.request

    employee_id = sys.argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    with urllib.request.urlopen(url) as response:
        body = response.read()
        decoded_body = body.decode('utf-8')
        tasks_list = json.loads(decoded_body)
        total_no_tasks = 0
        no_completed_tasks = 0
        names_completed_tasks = []
        for task in tasks_list:
            total_no_tasks += 1
            if task.get('completed') is True:
                no_completed_tasks += 1
                names_completed_tasks.append(task.get('title'))
            url2 = "https://jsonplaceholder.typicode.com/users/" + employee_id
            # Get the employee name
            with urllib.request.urlopen(url2) as response:
                body = response.read()
                decoded_body = body.decode('utf-8')
                user_info_dict = json.loads(decoded_body)
                name = user_info_dict.get('name')
    output_str = (f'Employee {name} is done with tasks' +
                  f'({no_completed_tasks}/{total_no_tasks}):' +
                  '')
    print(output_str)
    for task_name in names_completed_tasks:
        print(f'\t {task_name}')
