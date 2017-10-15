list=[1,2,3,"abc"];
#slicing the list
print(list[:]);
print(list[2:]);
print(list[:2]);
print(list[::-1]);
#modifying the list
list.insert(0,"hello")
print("Inserting ",list);
list.append([1,2,3])
print("Appending ",list);
list.extend([9,8,7])
print("Extending",list);
#searching a list
isContains=1 in list;
print(isContains);
for key in list :
    print(key);
print("-----------------------------------");
del list;
print(type(list));