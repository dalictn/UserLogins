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
#Check if username is one of the keys, then return true for next function
    def is_valid_username():
        '''if u == "Katz" and pw == "123":
            print("Your deepest, darkest secret")
        else:
            print("Access Denied")'''

        if user in Userlist:
            passw = Userlist.get(str(user.lower()))
            print('////user found... Authenticating////')

        def is_valid_password():
            if int(Pass) == passw:
                print('Secret')
            else:
                print('Authentication failed')
        
        is_valid_password()
    '''if is_valid_username():
        print("Username found...")
    
    else:
        print("Username Not found...")

    if is_valid_password():
        print("Password Authenticated. (secret)")
    
    else:
        print("Authentication error.")'''


    is_valid_username()
    

    

    



is_valid_credentials()