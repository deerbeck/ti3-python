#provided input for exercise 01
digits = '0123456789'

#slice string to get "2468" as output // start:stop:step
print(digits[2::2])

#slice and reverse to get "86420" as output // start at -2 and go backwards with stepwidth 2
print(digits[-2::-2])

#slice and format string to get "g02468u13579"
print(f"g{digits[::2]}u{digits[1::2]}")

#slice and format to get "Palindrom: 024686420"
print(f"Palindrom: {digits[::2]}{digits[-4::-2]}")