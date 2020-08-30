myNumbers = [23,234,345,4356234,243,43,56,2]

#Your code go here:

def increment_by_one(number): ## paso 1 de instructions

 return number * 3 ## paso 1 de instructions

new_list = list(map(increment_by_one, myNumbers)) ## paso 2 y 3

print(new_list)