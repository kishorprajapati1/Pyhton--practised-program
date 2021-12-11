#Calculate how many days,weeks,months are remaining after the user enter the current age upto 90 years.
current_age=int(input("Enter the Current Age: "))

#Subtracting current age from 90
age_remaining=90-int(current_age)

months=age_remaining*12
days=age_remaining*365
weeks=age_remaining*52

#Here f strings are used before the quotation so value can be inserted between the string.
print(f"You have {days} days, {months} months, {weeks} weeks left.")

#Result can also be printed in the below way.Remove the below comment to see the result

