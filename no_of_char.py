#Using the file school_prompt2.txt, find the number of characters in the file and assign that value to the variable num_char.

num = open("school_prompt.txt", "r")
num_char = 0
for i in num:
    num_char += int(len(i))
print(num_char)
