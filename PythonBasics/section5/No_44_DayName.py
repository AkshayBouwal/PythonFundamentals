dayNum = int(input("Enter the day number (Number must be between 0 and 6 with limits included): "))

if dayNum == 0:
    print("Monday")
elif dayNum == 1:
    print("Tuesday")
elif dayNum == 2:
    print("Wednesday")
elif dayNum == 3:
    print("Thursday")
elif dayNum == 4:
    print("Friday")
elif dayNum == 5:
    print("Saturday")
else:
    print("Sunday")