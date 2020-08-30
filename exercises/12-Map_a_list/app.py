Celsius_values = [-2,34,56,-10]



def fahrenheit_values(Celsius_values): # se añade el arreglo de arriba
    # como propiedad creo
# the magic go here:
    fahrenheit_values = []
     # en el arreglo de arriba se guarda el resultado del return de abajo
     # y es mapeado y luego guardado en la variable result
    return (Celsius_values * 1.8) + 32
   
result = list(map(fahrenheit_values, Celsius_values))
print(result)



