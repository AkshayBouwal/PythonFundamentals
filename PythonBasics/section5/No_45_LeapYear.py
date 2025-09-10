# userInput = int(input("Enter a Year: "))
#
# if (userInput % 4 == 0 and userInput % 100 != 0) or userInput % 400 == 0:
#     print("Leap Year")
# else:
#     print("Not a Leap Year")

#To comment multiple line Ctrl + /

year = int(input("Enter a year: "))

if year % 100 == 0:
    if year % 400 == 0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
elif year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


