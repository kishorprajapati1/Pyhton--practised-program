#Body Mass Index Calculator
print("BMI Calculator\n")

# BMI formula= weight/height*height. 
height=float(input("Enter the height in meters: "))
weight=int(input("Enter the Weight is Kilograms: "))

# Here height will be calculate first due to PEDMAS rule and then divided by weight and stored in bmi_calc variable
bmi_calc=weight/(height*height)

# converting bmi_calc value to whole numbers
bmi=int(bmi_calc)

#Printing the result
print("The BMI is: ",int(bmi))