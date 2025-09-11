dayNum = int(input("Enter the day number (Number must be between 0 and 6 with limits included): "))

# similar to switch case in java

match dayNum:
    case 0:
        print("Monday")
    case 1:
        print("Tuesday")
    case 2:
        print("Wednesday")
    case 3:
        print("Thursday")
    case 4:
        print("Friday")
    case 5:
        print("Saturday")
    case _: #similar to default case in java
        print("Sunday")



# if dayNum == 0:
#     print("Monday")
# elif dayNum == 1:
#     print("Tuesday")
# elif dayNum == 2:
#     print("Wednesday")
# elif dayNum == 3:
#     print("Thursday")
# elif dayNum == 4:
#     print("Friday")
# elif dayNum == 5:
#     print("Saturday")
# else:
#     print("Sunday")




