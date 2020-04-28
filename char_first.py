#Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.

fref = open("school_prompt.txt","r")
beginning_chars = fref.read(30)
print(beginning_chars)
