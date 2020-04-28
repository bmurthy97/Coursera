#Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.

gill = open("travel_plans.txt","r")
first_chars = gill.read(33)
print(first_chars)
