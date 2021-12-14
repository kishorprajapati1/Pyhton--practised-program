#Program for Leap Year
leap_year=int(input("Enter year to find the Leap Year. "))
if leap_year%4==0:
    print("It is leap year.")
    if leap_year%100==0:
        print("It is a leap year.")
    elif leap_year%400==0:
        print("It is leap year divisible by 400")
    else:
        print("It is not a leap year.")

else:
    print("It is not leap year, party hard.")