#Calculate the given number is even or odd.
#For even number its remainder must be 0.For example 4/2 it is even as remainder is 0.
#For odd number it will give remanider more than 0, For example 5/3 its remainder is 2 so it is odd number.
#I will be using Modulo operator(%) as it gives the value of remainder.

enter_number=float(input("Enter the number you want to check?: "))
number=enter_number%2
if number%2==0:
    print("The number is even: ",enter_number)
else:
    print("The number is odd: ",enter_number)