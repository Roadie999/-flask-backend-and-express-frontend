from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from the frontend

# Simple in-memory data store (for demo)
TODOS = [
    {"id": 1, "task": "Buy groceries", "done": False},
    {"id": 2, "task": "Call Alice", "done": True},
]
next_id = 3


@app.route('/api/hello')
def hello():
    return jsonify({"message": "Hello from Flask backend!"})


@app.route('/api/todos', methods=['GET'])
def list_todos():
    return jsonify(TODOS)


@app.route('/api/todos', methods=['POST'])
def add_todo():
    global next_id
    data = request.get_json() or {}
    task = data.get('task', '').strip()
    if not task:
        return jsonify({"error": "task is required"}), 400
    todo = {"id": next_id, "task": task, "done": False}
    TODOS.append(todo)
    next_id += 1
    return jsonify(todo), 201


@app.route('/api/todos/<int:todo_id>', methods=['PATCH'])
def update_todo(todo_id):
    data = request.get_json() or {}
    for t in TODOS:
        if t['id'] == todo_id:
            t['done'] = data.get('done', t['done'])
            t['task'] = data.get('task', t['task'])
            return jsonify(t)
    return jsonify({"error": "not found"}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
