#prime number by Sqrt
import math
def primeNumber(number):
    #calcutation
    flag=True;
    if(number==1):
        print(number,"-> not a prime numnber");
    elif(number==2):
        print(number," prime nunber");
    else:
        i=2
        n=int(math.sqrt(number));
        while(i<=n):
            if(number%i==0):
                flag=False;
                break;
            i+=1;
    if flag:
         print(number, "Prime number");
    else:
        print(number,"Not a Prime Number");


if __name__=="__main__":
    print("Enter an input");
    number=int(input());
    primeNumber(number);
