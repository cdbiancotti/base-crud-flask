from flask import Flask, request, jsonify
from app_service import AppService
import json

app = Flask(__name__)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

appService = AppService()


@app.route('/')
def home():
    info = {
        "A": "Bienvenido a la CRUDAPI con Flask.",
        "B": [
            "GET /api/tasks",
            "POST /api/task",
            "PUT /api/task",
            "DELETE /api/task/<int:id>"
        ]
    }
    return jsonify(info)


@app.route('/api/tasks')
def get_tasks():
    return jsonify(appService.tasks)


@app.route('/api/task', methods=['POST'])
def post_task():
    request_data = request.get_json()
    task = request_data['task']
    return appService.create_task(task)


@app.route('/api/task', methods=['PUT'])
def put_task():
    request_data = request.get_json()
    request_task = request_data['task']
    return appService.update_task(request_task)


@app.route('/api/task/<int:id>', methods=['DELETE'])
def delete_task(id):
    return appService.delete_task(id)


if __name__ == '__main__':
    app.run()
