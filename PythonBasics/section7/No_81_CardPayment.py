cardNumber = input("Enter Card Number: ")

#print(len(cardNumber))

encryptedNum = "XXXX " * 3
#encryptedNum = "XXXX XXXX XXXX "

# for i in range(15,len(cardNumber)):
#     #print(i)
#     encryptedNum = encryptedNum + cardNumber[i]

encryptedNum = encryptedNum + cardNumber[15:]

print(encryptedNum)
