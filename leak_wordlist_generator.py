import random
mail_l=["@gmail.com","@gmail.com","@yahoo.com","@hotmail.com"]
f=open("emp_names_20000.txt","r")
g=open("email_names.txt","w")
fname_l=f.readlines()
for i in fname_l:
    st=i.split()
    e_mail=st[0]+'.'+st[1]+mail_l[random.randint(0,3)]
    g.write(e_mail+"\n")