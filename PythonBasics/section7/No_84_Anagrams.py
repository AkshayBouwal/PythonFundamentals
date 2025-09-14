s1 = "snooze alarms"
s2 = "alas, no more Z's"
s2 = s2.lower()

# s1 = "taste"
# s2 = "state"

#print(s1.count("l"))

for char in s1:

    if char.isalpha():

        if s1.count(char) != s2.count(char):
            print("Strings are not anagrams")
            break

else:
    print("Strings are anagrams")


