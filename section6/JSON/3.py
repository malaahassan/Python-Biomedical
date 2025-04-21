import json


users = []
with open('users.json', 'r') as file:
    users = json.loads(file.read())

new_user = {"username": "user4", "password": "pass4"}
users.append(new_user)
users = json.dumps(users)

with open('users.json', 'w') as file:
   file.write(users)