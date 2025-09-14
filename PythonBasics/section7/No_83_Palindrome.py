# s1 = "Madam"
# s1 = "Race car"
#s1 = "race carac ecar"
s1 = "Python"

s1 = s1.lower()

s2 = s1[::-1]
# print(s2)

if s1 == s2:
    print('"' + s1 + '"' + " is palindrome")
else:
    s1 = s1 + s2[1::]
    print(s1)
