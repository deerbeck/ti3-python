#assigning given message and code 
code1 = 'X'
message1 = 'RTFVQXSSE'

#assign numbers to each character of code1 and message1 using list comprehension (iter through each element of given list and apply a function to that element)
#using given number-char combo
code1_val = ord(code1)-65
message1_val = [ord(e)-65 for e in list(message1)]

#decipher given numbercode with listcomprehension (abs(e-code1_val) represents xor)
result_val = [abs(e ^ code1_val) for e in message1_val]

#change numbers back to chars and create the resulting string
result1 = "".join([chr(e+65) for e in result_val])