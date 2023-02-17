import random
chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()1234567890"
f=open("output.txt","w")
for i in range(50000):
    ln=""
    for j in range(120):
        ln+=chars[random.randint(0,71)]
    f.write(ln+"\n")
