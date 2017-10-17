class Test:
    isVoteValid=False;
    __age=0;
    def __init__(self,age):
        self.__age=age;
        print("Calling contructor");
    def printName(self,name):
        print("the name of the Value=",name);
    def calculateVote(self):
        if(self.__age>=18):
            self.isVoteValid=True;
    def print(self):
        print(self.isVoteValid);

test=Test(22);
test.printName("Hello");
test.calculateVote();
test.print();
print("Valid/Not =",test.isVoteValid," Age = ",test._Test__age);
