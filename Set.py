a_set={1,2,3,4,4};
print(a_set);
#modifying a set
a_set.add(6);
print(a_set);
a_set.update({1,2,3,4,7});
print(a_set);
a_set.add(9);
print(a_set);
print(9 in a_set);
lister=[];
lister=(list(a_set));
print(lister[::-1]);
print(a_set);
a_set.discard(9);
print(a_set);
try:
    a_set.remove(9);
except KeyError:
    print("Key Error occured using the params Remove");
