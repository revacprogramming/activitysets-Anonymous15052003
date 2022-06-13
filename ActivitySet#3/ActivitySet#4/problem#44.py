l=[]

while True:
    a=input("Enter the contents :")
    if a=="Done":
        break
    f=float(a)
    c=l.append(f)

print(l)