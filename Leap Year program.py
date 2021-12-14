leap_year=int(input("Enter year to find the Leap Year. "))
if leap_year%4==0:
    print("It is leap year.")
    if leap_year%100==0:
        print("It is a leap year that is divided by 100")
    elif leap_year%400==0:
        print("It is leap year divisible by 400")
    else:
        print("It is not a leap year that is divisible by 100")

else:
    print("It is not leap year bitch, party hard.")
