billAmount = int(input("Please your bill amount: "))

if billAmount < 1000:
    finalAmount = billAmount - (billAmount * (10/100))
    print("Your final bill amount: $" + str(finalAmount))
elif 1000 <= billAmount < 5000:
    finalAmount = billAmount - (billAmount * (15/100))
    print("Your final bill amount: $" + str(finalAmount))
elif 5000 <= billAmount < 10000:
    finalAmount = billAmount - (billAmount * (20/100))
    print("Your final bill amount: $" + str(finalAmount))
else:
    finalAmount = billAmount - (billAmount * (25/100))
    print("Your final bill amount: $" + str(finalAmount))