f=open("emp_names_20000.txt","r")
g=open("emp_names.txt","r")
L1=f.readlines()
L2=g.readlines()
for i in L2:
    for j in L1:
        if i==j:
            print(i)