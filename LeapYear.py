def leapYear(year):
    if year%4==0:
        print(year," Leap Year ");
    else:
        print(year," Not a Leap Year");
if __name__=="__main__":
     print("Enter the input");
     year= int(input());
     leapYear(year);
