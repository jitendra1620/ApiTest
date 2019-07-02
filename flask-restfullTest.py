from flask import Flask, jsonify, request, abort
from flask_restful import Resource, Api
from taskJson import tasks

app = Flask(__name__)
api = Api(app)


class GetAllTask(Resource):
    def get(self):
        return jsonify({'allTask': tasks})

    def post(self):
        some_json = request.get_json()
        return {'you sent': some_json}


class Multi(Resource):
    def get(self, num):
        return {'result': num * 10}


class GetTask(Resource):
    def get(self, taskID):
	    taskToSend = None
	    for task in tasks:
	        if task['id'] == taskID:
	            taskToSend = task
	            return jsonify({'task': task})
	    if taskToSend == None:
	    	return jsonify({'task': ""})


api.add_resource(GetAllTask, '/allTask/')
api.add_resource(Multi, '/multi/<int:num>')
api.add_resource(GetTask, '/taskID/<int:taskID>')

if __name__ == '__name__':
    app.run(debug=True)
