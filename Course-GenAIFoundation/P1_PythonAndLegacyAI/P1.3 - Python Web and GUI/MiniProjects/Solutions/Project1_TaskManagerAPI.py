"""
Mini Project 1: Task Manager Web API (Solution)
"""

from flask import Flask, request, jsonify

app = Flask(__name__)
tasks = {}

def get_next_id():
    return str(len(tasks) + 1)

# Helper: filter tasks by status
def filter_tasks_by_status(status):
    return [task for task in tasks.values() if task['status'] == status]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    status = request.args.get('status')
    if status:
        return jsonify(filter_tasks_by_status(status))
    return jsonify(list(tasks.values()))

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task_id = get_next_id()
    tasks[task_id] = {
        'id': task_id,
        'title': data['title'],
        'description': data['description'],
        'due_date': data.get('due_date', ''),
        'status': data.get('status', 'pending')
    }
    return jsonify(tasks[task_id]), 201

@app.route('/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    if task_id in tasks:
        tasks[task_id].update({
            'title': data.get('title', tasks[task_id]['title']),
            'description': data.get('description', tasks[task_id]['description']),
            'due_date': data.get('due_date', tasks[task_id].get('due_date', '')),
            'status': data.get('status', tasks[task_id].get('status', 'pending'))
        })
        return jsonify(tasks[task_id])
    return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    if task_id in tasks:
        deleted = tasks.pop(task_id)
        return jsonify(deleted)
    return jsonify({'error': 'Task not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
