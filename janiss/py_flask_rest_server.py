from flask import Flask
from flask_restful import reqparse, abort, Resource, Api


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
        'todo2':{'task':'?????'},
        }

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('task')


# Adding handlers to an App
api.add_resource(TodoList,'/todos')
api.add_resource(Todo,'/todos/<todo_id>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
