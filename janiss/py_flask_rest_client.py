from requests import put,get
ret = put('http://localhost:5000/todo1',data={'data':'Remember the milk'})
print("PUT(todo1): {}".format(ret.json()))

ret = get('httpL//localhost:5000/todo1')
print("GET(todo1): {}".format(ret.json()))

ret = put('http://localhost:5000/todo2',data={'data':'Change my breakepads'})
print("PUT(todo2): {}".format(ret.json()))

ret = get('http://localhost:5000/todo2')
print("GET(todo2): {}".format(ret.json()))
