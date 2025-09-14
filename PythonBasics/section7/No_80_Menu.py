menu = ["Hot Dogs", "Donuts" , "Burger" , "Pizza"]
prices = ["3", "40" , "135", "6457"]
#prices = ["30", "40" , "13", "64"]

# for i in range (len(menu)):
#     print(menu[i] +  " " +"-" * (30 - len(menu[i]) - len(prices[i]) - 2) + " " + prices[i])

for i in range (len(menu)):
    print(menu[i] + " " + "-" * (30 - len(menu[i]) - 5) + " $: " + prices[i])

