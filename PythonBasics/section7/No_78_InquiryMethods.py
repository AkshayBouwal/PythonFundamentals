s = "Hello"
print(s.isalpha())

s = "Hello"
print(s.islower())

s = "hello12"
print(s.islower())

s = "hello#%$#%"
print(s.islower())

s = "UPPER"
print(s.isupper())

s = "UPPER1234"
print(s.isupper())

s = "This String Is In Title Case"
print(s.istitle())

s = "   "
print(s.isspace())

s = ""
print("ispace() with empty string: ",s.isspace())

s = "\n\t"
print(s.isspace())

s = "Hello World"
print(s.isprintable())

s = "Hello World \t"
print(s.isprintable())

num = "Hello"
print("isidentifier(): " , num.isidentifier())

num2 = "Hello \t"
print("isidentifier(): " , num2.isidentifier())