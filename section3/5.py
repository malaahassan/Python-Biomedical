USERS = {'user1': 'password1', 'user2': 'password2'}

user = input("Enter username: ").strip()
while(len(user) < 1):
    user = input("Enter username: ").strip()
    
password = input("Enter password: ")
while(len(password) < 1):
    password = input("Enter password: ")

USERS[user] = password
