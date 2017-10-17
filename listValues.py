temp=[1,2,3,4,[9,8,7],0];
tempVal=[];
for val in temp:
    print(type(val));
    if(isinstance(val,int)):
        tempVal.append(val);
        print("Integer");
    else:
        tempVal.extend(val);
        print("List");

print(tempVal);



