s=input("Enter a string of letters and numbers : ")

a=0
b=0

for i in range(0,len(s)):
    if s[i].isdigit():
        a=a+1
    if s[i].isalpha():
        b=b+1
    
print("Digits :",a)
print("Alphabets :",b)