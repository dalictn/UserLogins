#Ask user for their username
Username = input("Hello, User. Please enter your username here: ")
Pass = input("Please input your password here: ")

Userlist = {
    "Katz": 123,
    "Juan": 123,
    "Snek": 123
}


#Authenticate the user on if they are Katz
def is_valid_credentials(u,pw):
    '''if u == "Katz" and pw == "123":
        print("Your deepest, darkest secret")
    else:
        print("Access Denied")'''
    auth = {u,pw}

    if str(u) in Userlist and int(pw) in Userlist:
        print("Your deepest, darkest secret")
    
    else:
        print("Access Denied")
    



is_valid_credentials(Username,Pass)