#do pip install names
import names
f=open(input("Filename :"),"w")
for i in range(int(input("Number of names:"))):
    f.write(names.get_full_name()+"\n")