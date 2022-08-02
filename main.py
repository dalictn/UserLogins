#Ask user for their username
Username = input("Hello, User. Please enter your username here: ")
Pass = input("Please input your password here: ")


user = str(Username.lower())


Userlist = {
    "katz": 123,
    "juan": 123,
    "snek": 123
}

def is_valid_credentials():
#Check if username is one of the keys, then get password, and compare to user input
    def is_valid_username():


        if user in Userlist:
            global passw
            passw = Userlist.get(str(user.lower()))
            print('////user found... Authenticating////')
            
        else:
            print('User not found')
            exit()

    def is_valid_password():
            if int(Pass) == passw:
                print('Secret')
            else:
                print('Authentication failed')
                exit()
                
                
        
    is_valid_username()
    is_valid_password()
    

    

    



is_valid_credentials()