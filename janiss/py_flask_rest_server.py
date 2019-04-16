from flask import Flask
from flask_restful import reqparse, abort, Resource, Api
from subprocess import Popen, PIPE

class Ping(Resource):
	def get(self,ip):		
		process = Popen(['ping',ip,'-n','2'], shell=True, stdout=PIPE, stderr=PIPE)
		out = proccess.stdou.read()
		return out
		
class TodoList(Resource):
	def get(self):
		print("debug: sending fill list")
		return TODOS

	def delete(self,todo_id):
		print("debug: deleting task with id {}".format(todo_id))
		#abort_if_doenst_exist
		del TODOS[todo_id] #deletes a dictionary
		return TODOS[todo_id]

	def post(self):
		args = parser.parse_args()
		todo_id = int(max(TODOS.keys()).lstrip('todo'))+1
		todo_id = 'todo%i' % todo_id
		TODOS[todo_id]={'task':args['task']}
		print("debug: added task with id {}".format(todo_id))
		return TODOS[todo_id], 201

	def put(self,todo_id):
		args = parser.parse_args()
		task = {'task': args['task']}
		TODOS[todo_id] = task
		return task, 201

class Todo(Resource):
	def get(self, todo_id):
		#abort_if_todo_doesnt(todo_id)
		return TODOS[todo_id]

# Creates a dictionary with content ..
TODOS = {
'todo1':{'task':'build an API'},
'todo2':{'task':'rest a bit'},
'todo3':{'task':'do some workout'}
}

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('task')


# Adding handlers to an App
api.add_resource(TodoList,'/todos')
api.add_resource(Todo,'/todos/<todo_id>')
api.add_resource(Ping,'/ping/<ip>')


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
