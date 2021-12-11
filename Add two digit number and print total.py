#Crreating a program to print addition of two digits
two_digit=input("Enter two Digits: ")
# fetching the first number index               #index value starts from[0,1,2,3,......]
First_digit=two_digit[0]                #here [0] is the index value of 1st digit 
print("First number is: ",First_digit)
# fetching the second number index
Second_digit=two_digit[1]                #here [1] is the index value of 2nd digit
print("Second Number is: ",Second_digit)
# adding the number as integer
add=int(First_digit)+int(Second_digit)      #int type conversion is used as without int adding the first_digit & Second_digit would just added as a string
print("The sum of two digit is:",add)