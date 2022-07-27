#Ask user for their username
Username = input("Hello, User. Please enter your username here: ")
Pass = input("Please input your password here: ")


str(Username)
int(Pass)

Userlist = {
    "katz": 123,
    "juan": 123,
    "snek": 123
}

def is_valid_credentials(u,pw):
#Check if username is one of the keys, then return true for next function
    def is_valid_username():
        '''if u == "Katz" and pw == "123":
            print("Your deepest, darkest secret")
        else:
            print("Access Denied")'''

        if str(u) in Userlist:
            return(True)

    def is_valid_password():
        if is_valid_username == True:
            if int(pw) in Userlist:
                return(True)

    if is_valid_username == True:
        print("Username found...")
    
    else:
        print("Username Not found...")

    if is_valid_password == True:
        print("Password Authenticated. (secret)")
    
    else:
        print("Authentication error.")


    is_valid_username()
    is_valid_password()

    

    



is_valid_credentials(Username,Pass)