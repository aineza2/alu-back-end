#!/usr/bin/python3
import requests
import sys

def get_employee_todo_progress(employee_id):
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')
    todos = response.json()

    completed_todos = [todo for todo in todos if todo['completed']]
    total_todos = len(todos)

    print(f'Employee {todos[0]["userId"]} is done with tasks({len(completed_todos)}/{total_todos}):')
    for todo in completed_todos:
        print(f'\t {todo["title"]}')

if __name__ == "__main__":
    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
