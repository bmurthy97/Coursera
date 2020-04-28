#Using the file school_prompt.txt, assign the third word of every line to a list called three.

fref = open("school_prompt.txt","r")
three = []
for i in fref.readlines():
    k = i.split()
    three.append(k[2])
print(three)
