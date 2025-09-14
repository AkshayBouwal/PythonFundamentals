s = "python is very easy"

# print(s.startswith("python"))
# print(s.startswith("python1"))
# print(s.startswith("is",7))
# print(s.endswith("sy"))
# print(s.removeprefix("py"))
# #if prefix is not matching - return same string
# print(s.removeprefix("py2323"))
# print(s.removesuffix("sy"))



# s2 = s.partition("is")
# print(s2)
# print(type(s2))
#
# s2 = s.split("is")
# print(s2)
# print(type(s2))


s = "python is very easy"
s2 = s.rpartition("s")
print(s2)