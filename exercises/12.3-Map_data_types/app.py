list_Strings = ['1','5','45','34','343','34',6556,323]


def type_list(items):
        return type(items) ## devuelve de una vez los tipos de datos a items
        
new_list = list(map(type_list, list_Strings))
print(new_list)


