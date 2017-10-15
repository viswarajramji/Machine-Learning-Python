#prime number by Sqrt
import math
def primeNumber(number):
    #calcutation
    if(number==1):
       return False;
    elif(number==2):
       return True;
    else:
        i=2
        n=int(math.sqrt(number));
        while(i<=n):
            if(number%i==0):
                return False;
            i+=1;
    return True;


if __name__=="__main__":
    print("Enter an input");
    number=int(input());
    isPrime=primeNumber(number);
    if isPrime:
        print(number,"-> Prime Number");
    else:
        print(number,"-> Not Prime");