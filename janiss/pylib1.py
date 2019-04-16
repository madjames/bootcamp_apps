import requests

url = 'https://www.google.com'

r = requests.get(url)

print("URL: {0}".format(str(url)))
print("Status: {0}".format(str(r.status_code)))
print("Header: {0}".format(str(r.headers['content-type'])))
print("Encoding: {0}".format(str(r.encoding)))
print("Body: {0}".format(r.text))


