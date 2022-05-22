# Dictionary

# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.


name = input("Enter the name of the file : ")

file = open(name)

l = []

for line in file:
    if not line.startswith("From:"): 
        continue

    line = line.split()
    l.append(line[1])

count = {}

for word in l:
    count[word] = count.get(word,0) + 1
    #get() method returns the value for the specified key if the key is in the dictionary.

maxcount = None
maxword = None

for word,count in count.items(): 
    if maxcount == None or count > maxcount:
        maxcount = count
        maxword = word

print (maxword,maxcount)