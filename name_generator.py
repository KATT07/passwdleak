#do pip install names
import names
import random
import hashlib

LST=[]
for i in range(int(input("Enter how many to generate :"))):
    LST.append([names.get_full_name()])

mail_l=["@gmail.com","@gmail.com","@yahoo.com","@hotmail.com"]
email_l=[]
for i in LST:
    st=i[0].split()
    email_l.append([st[0]+'.'+st[1]+mail_l[random.randint(0,3)]])

pwd_l=[]
chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()1234567890"
for i in range(len(email_l)):
    pwd=""
    for i in range(10):
        pwd+=chars[random.randint(0,71)]
    hash_pwd=hashlib.sha256(pwd.encode())
    pwd_l.append([hash_pwd.hexdigest()])

f=open("output_100k_hashed.txt",'w')
for i in range(len(email_l)):
    f.write(email_l[i][0]+":"+pwd_l[i][0]+'\n')
