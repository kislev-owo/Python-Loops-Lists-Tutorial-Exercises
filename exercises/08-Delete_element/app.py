people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    #Your code go here:

    newperson = []
    for person in people:
        people2 = people
        if person != person_name:   
            newperson.append(person)
    
    return newperson
    
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))



