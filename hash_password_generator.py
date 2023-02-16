import random 
import hashlib
f=open("hashed_password.txt","w")
chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()1234567890"
for i in range(20000):
    pwd=""
    for i in range(10):
        pwd+=chars[random.randint(0,71)]
    hash_pwd=hashlib.sha256(pwd.encode())
    f.write(hash_pwd.hexdigest()+"\n")