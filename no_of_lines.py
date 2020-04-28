#Find the number of lines in the file, travel_plans2.txt, and assign it to the variable num_lines.

fref = open("travel_plans2.txt","r")
num = fref.readlines()
num_lines = len(num)
print(num_lines)
fref.close()
