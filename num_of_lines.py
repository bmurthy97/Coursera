#Assign to the variable num_lines the number of lines in the file school_prompt.txt.

fill = open("school_prompt.txt","r")
num_lines = 0
for i in fill.readlines():
    num_lines += 1
print(num_lines)
