o=0
e=0
oddsum=0
evensum=0
l=[]
n=int(input("Enter how many numbers you want to input :"))

for i in range(n):
    p=int(input("Enter number :"))
    l.append(p)

for i in l:
    if i%2==0:
        evensum=evensum+i
        e=e+1
    else:
        oddsum=oddsum+i
        o=o+1

print("The sum of all odd numbers is :",oddsum)
print("The sum of all even numbers is :",evensum)
print("Total numbers of odd numbers is :",o)
print("Total numbers of even numbers is :",e)