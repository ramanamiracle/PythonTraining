import requests

url = 'http://127.0.0.1:5000/api/user/100'

r = requests.delete(url)

print(r)
print(r.content)