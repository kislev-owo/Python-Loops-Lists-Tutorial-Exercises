
my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]


#your code go here:

hello = []

for i in my_list:
    if type(i) == list or type(i) == dict:
        hello.append(i)



print(hello)
