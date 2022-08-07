import hashlib
import json
import os

cwd = os.getcwd()

print(cwd)
global Pass
# Ask user for their username
Username = input("Hello, User. Please enter your username here: ")
Pass = input("Please input your password here: ")

os.getcwd()

user = str(Username)

with open('config.json', 'r') as f:
  users = json.load(f)




def is_valid_credentials():
    # Check if username is one of the keys, then get password, and compare to user input
    def is_valid_username():

        if user in users:
            global passw
            passw = users.get(str(user.lower()))
            print('////user found... Authenticating////')

        else:
            print('User not found')
            exit()

    def hashing():
        global Pass

        plaintext = Pass

        encoded = plaintext.encode()

        result = hashlib.sha256(encoded)

        Pass = result.hexdigest()

    def is_valid_password():
        if str(Pass) == passw:
            print('Secret')
        else:
            print('Authentication failed')
            exit()

    is_valid_username()
    hashing()
    is_valid_password()


is_valid_credentials()
