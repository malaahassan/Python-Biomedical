import json

users = [
    {"username": "user1", "password": "pass1"},
    {"username": "user2", "password": "pass2"},
    {"username": "user3", "password": "pass3"}
]

users = json.dumps(users)

with open('users.json', 'w') as file:
    file.write(users)
