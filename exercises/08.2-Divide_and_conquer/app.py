list_of_numbers = [4,	80,	85,	59,	37,25,	5,	64,	66,	81,20,	64,	41,	22,	76,76,	55,	96,	2,	68]


#Your code here:


def merge_two_list(list_of_numbers):
    impar=[]
    par=[]
    for i in list_of_numbers:
        if i %2==0:
            par.append (i)
        else:
            impar.append (i)
    lista=[]
    lista.append(impar)
    lista.append(par)
    return lista

print(merge_two_list(list_of_numbers))




