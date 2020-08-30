names = ['Alice','Bob','Marry','Joe','Hilary','Stevia','Dylan']


def prepender(name):
    return "My name is: " + name
#Your code go here:

result = list(map(prepender, names)) ## como en el ejercicio anterior
## mapeamos la funcion prepender con la propiedad name que es 
## devuelta en el return

print(result)