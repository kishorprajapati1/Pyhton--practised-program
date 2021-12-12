#Program to give ticket price based on age and height.
print("Welcome to Roller Coster Ticket Window: ")
height_ask=int(input("Enter your Height in CMs: "))
age_ask=int(input("Enter your Age: "))

#Here the first height is checked if the condition is true than it will go inside the loop else it will print line 17.

if height_ask>=120:
    print("You can enter the ride.")
    if age_ask<12:                                              #Age limit is 0-12 price is $7.
        print("Please pay $7 at the window.")
    elif age_ask<=18:                                           # Age 12-18 price is $10.
        print("Please pay $10 at the window.")
    else:
        print("Please pay $14 at the window.")                  # And age over 18 price is $14.
else:
    print("Sorry, Minimum height required is 120cm.")