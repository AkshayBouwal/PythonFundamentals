s = "These+notes#reveal9Newton seeking-out an(!underlying structure to/the\\pyramid:the units of measurements?used>by its builders."

for char in s:

    if not char.isalpha() and not char.isspace() and char != ".":
        s = s.replace(char, " ")

print(s)