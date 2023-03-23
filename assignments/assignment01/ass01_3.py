# code from task1
import os

# open text file, read all lines and store each line as element of a list in text
text = open("text_assignment01.txt", 'r').readlines()

# extract needed codewordsnipplets out of text, join them and safe it in 'temp_code'
temp_code = text[5][2] + text[2][26:29] + text[1][:3] + text[-1][:3]

# modify 'temp_code' to fit requirements
codeword = (temp_code[::-1] * 5)[:-2][8::8]


# code from task 3
# decipher message
message = 'SLCVZCILAG'

# adapt codelength to messagelength create code_long from given codeword. iter through the length of
# given message and use modulo to repeatedly add each char from codeword
code_long = [codeword[(i % len(codeword))] for i in range(len(message))]

# translate each char to corresponding value
code_val = [ord(e)-65 for e in code_long]
message_val = [ord(e)-65 for e in message]

# get result values by using given decipher algorithm
result_val = [abs(message_val[i] ^ code_val[i]) for i in range(len(message))]

# convert values back to chars and return as a given string
result = "".join([chr(e+65) for e in result_val])
