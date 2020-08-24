chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    #Your code go here:

   
    lista = []    # 1.- lista vacia

    for names in chunk_one:     # 2. ciclo en la 2da lista

        lista.append(names)  # 3. resultado en la lista vacia 
   
    for names in chunk_two:         # 4 lo mismo
       
        lista.append(names)

    return lista     # 5. devolver las 2 listas

print(merge_list(chunk_one, chunk_two))


