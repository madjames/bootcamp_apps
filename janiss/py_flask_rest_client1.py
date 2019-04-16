from requests import get,post

ret = get('http://localhost:5000/todos/todo1')
print("GET({}): ".format(ret.status_code,ret.text))
