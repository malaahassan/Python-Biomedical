import json

with open('users.json', 'r') as file:
    users = json.loads(file.read())
    print("Username: {}, Password: {}".format(users[0]["username"], users[0]["password"]))