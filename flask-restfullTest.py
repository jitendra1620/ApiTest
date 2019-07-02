from flask import Flask, jsonify, request, abort, make_response
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


class GetTask(Resource):
    def get(self, taskID):
	    taskToSend = None
	    for task in tasks:
	        if task['id'] == taskID:
	            taskToSend = task
	            return jsonify({'task': task})
	    if taskToSend == None:
	    	return {"message": "Contact does not exist."}, 404

class CreateTask(Resource):
	def post( self):
		if not request.get_json() or not 'title' in request.get_json():
			return {"error": "bad request paramter."}, 404
		task = {
	    'id': tasks[-1]['id'] + 1,
	    'title': request.json['title'],
	    'description': request.json.get('description', ""),
	    'done': False
		}
		tasks.append(task)
		return jsonify({'task': task})  
		
api.add_resource(GetAllTask, '/allTask/')
api.add_resource(GetTask, '/taskID/<int:taskID>')
api.add_resource(CreateTask,'/')

if __name__ == '__name__':
    app.run(debug=True)
