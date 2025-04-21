import json

with open('users.json', 'r') as file:
    users = json.loads(file.read())
    username = input("Enter Username:")
    password = input("Enter Password:")
    found = False
    for user in users:
        if user["username"] == username and user["password"] == password:
            print("Logged in.")
            found = True
    if not(found):
        print("Creds do not match.")
