# starttuple
t = (1, 1, 2, 3, 5, 8, 13, 21)
print(t)

# convert t to string
string = str(t)
print(string)

# string method testing

s = "das Ist ME1N teext"

print(s)
print(s.capitalize())
print(s.count("d"))
print(s.find("1"))
print(s.isalpha())
print("-----")
print(",".join(list(s)))
print(s.lower())
print(s.replace("d", "D"))
print(s.rsplit())
print(s.split())

#modified given string to give a proper german sentence
s = "das Ist ME1N teext"

s = s.lower()
s = s.replace("d", "D")
s = s.replace("1", "i")
s = s + "."
s = s.replace("tee", "Te")
print(s)