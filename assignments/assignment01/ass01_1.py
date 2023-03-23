import os


# open text file, read all lines and store each line as element of a list in text
text = open(".\\assignments\\assignment01\\text_assignment01.txt",'r').readlines()

# extract needed codewordsnipplets out of text, join them and safe it in 'temp_code'
temp_code = text[5][2] + text[2][26:29] + text[1][:3] + text[-1][:3]

# modify 'temp_code' to fit requirements
codeword = (temp_code[::-1] * 5)[:-2][8::8]
print(codeword)