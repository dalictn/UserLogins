import hashlib

global Pass
#Ask user for their username
Username = input("Hello, User. Please enter your username here: ")
Pass = input("Please input your password here: ")



user = str(Username)


Userlist = {
    "katz": "9c24f45a7ea9e4668ee31dc18bd0a9153f1413ceb3fad18b0a07e16e6a9bc587",
    "juan": "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3",
    "snek": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"
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