immutable_var = tuple([True,["Arsen","Vardanyan"],"man",32,"Georgia"])

print("Immutable tuple:",immutable_var)

#immutable_var[1]=12.1 #ERROR! Other type of element Нельзя менять значения элементов 
# кортежа, однако содержание списков - элементов кортежа можно менять,обращаясь к элементам
# такого списка

immutable_var[1][0] = "Sergey"#,"Anokhin"]

immutable_var[1][1] = 1#"Anokhin"

print("Immutable tuple:",immutable_var)

mutable_list = list([True,["Arsen","Vardanyan"],"man",32,"Georgia"])

print (mutable_list)

mutable_list[1]=["Pacим","Абушариф","Оглы"]

mutable_list.append("12.01.1983")

mutable_list.extend("A3")

print (mutable_list)

mutable_list.remove ("man")

print (mutable_list)
