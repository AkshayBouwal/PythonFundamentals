import re

# print(re.fullmatch("(ab)?", ""))
# print(re.fullmatch("(ab)?", "ab"))
# print(re.fullmatch("(ab)?", "abab"))
# print(re.fullmatch("(ab)?", "aa"))
# print(re.fullmatch("(ab)?", "bb"))


print(re.fullmatch("(ab)*", ""))
print(re.fullmatch("(ab)*", "ababababab"))
print(re.fullmatch("(ab)*", "ababa1b3abab"))