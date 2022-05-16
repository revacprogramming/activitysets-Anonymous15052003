name = input("Enter file name: ")

file = open(name)

l = list()   

for line in file:                    
    word= line.rstrip().split()    
    for i in word:               
        if i in l:         
            continue               
        else :                     
            l.append(i)    

l.sort()               

print(l)                          