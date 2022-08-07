import json 
      
# Data to be written 
Userlist = {
    "katz": "9c24f45a7ea9e4668ee31dc18bd0a9153f1413ceb3fad18b0a07e16e6a9bc587",
    "juan": "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3",
    "snek": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"
}
      
with open('config.json', 'r') as f:
  users = json.load(f)


inputt = input('info: ')

print(users.get(str(inputt.lower())))
