digits = '0123456789'

print(digits[2::2])

print(digits[-2::-2])

print(f"g{digits[::2]}u{digits[1::2]}")

print(f"Palindrom:{digits[::2]+digits[-4::-2]}")