theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:


def yesOrNo(variable):
    if variable == 1:
        return "wiki"
    else:
        return "woko"


lista = list(map(yesOrNo, theBools)) # cada vez que mapea lleva un 
# numero del arreglo al condicional yesOrNo y lo guarda en lista
print(lista)