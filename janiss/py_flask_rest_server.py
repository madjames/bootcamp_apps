from flask import Flask
from flask_restful import reqparse, abort, Resource, Api


class TodoList(Resource):
    def get(self):
        print("debug: sending fill list")
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo'))+1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id]={'task':args['task']}
        print("debug: added task with id {}".format(todo_id))
        return TODOS[todo_id], 201

TODOS = {
        'todo1':{'task':'build an API'},
        'todo2':{'task':'?????'},
        }


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('task')

api.add_resource(TodoList,'/todos')

if __name__ == '__main__':
    app.run(debug=True)
