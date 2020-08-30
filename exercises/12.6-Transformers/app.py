incomingAJAXData = [
	{ "name": 'Mario', "lastName": 'Montes' },
	{ "name": 'Joe', "lastName": 'Biden' },
	{ "name": 'Bill', "lastName": 'Clon' },
	{ "name": 'Hilary', "lastName": 'Mccafee' },
	{ "name": 'Bobby', "lastName": 'Mc birth' }
]

#Your code go here:

def my_var(nombreCompleto): ## paso 1
    name = nombreCompleto["name"]   ## paso 3
    last_name = nombreCompleto ["lastName"] ## paso 3
    return name + " " + last_name   ## paso 3


transformedData = list(map(my_var, incomingAJAXData)) ## paso 2 y 3
print(transformedData)