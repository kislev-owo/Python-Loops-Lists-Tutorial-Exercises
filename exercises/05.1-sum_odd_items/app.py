arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:

def sumaImpar():
    auxiliar = 0 
    for i in arr:
        if i % 2 != 0:
            auxiliar = auxiliar + i 
    return auxiliar
 

print(sumaImpar())

## https://www.geeksforgeeks.org/python-program-to-print-all-odd-numbers-in-a-range/