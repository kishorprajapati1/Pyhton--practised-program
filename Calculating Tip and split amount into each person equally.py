#Program to calculate tip and share the Amount of bill equally
print("Welcome to Tip Calculator: ")
enter_amount=float(input("Enter the Bill Amount: "))

#calculating the tip percentage
enter_tip=int(input("Enter the tip percentage you want to add: "))/100
tip=(enter_amount*enter_tip)+enter_amount

#Enter the value which needs to be split into the each individual
person_split_bill=int(input("Enter the number of person you want to divide the bill: "))

#here round() is used to get the result in 2 decimals places.
person_split_bill=round((tip/person_split_bill), 2)

print("Each person would pay: ", person_split_bill)


#OUTPUT
# Enter the Bill Amount: 124.56
# Enter the tip percentage you want to add: 12
# Enter the number of person you want to divide the bill: 7
# Each person would pay:  19.93