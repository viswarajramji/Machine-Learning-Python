dict={1:[1,2,3],
      2:[4,5,6],
      3:[7,8,9]};
#searching a map:
for  temp in dict.keys():
    tempList=dict[temp];
    for i in tempList:
        print(i);

print(dict.items());
