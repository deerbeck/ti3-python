#months in correct order
months = ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September',
          'Oktober', 'November', 'Dezember']
#create months dict to later assign month to key and the number to value
months_dict = dict()

#loop through months and assign each month to the correct number
for i in range(len(months)):
    months_dict[months[i]] = i

#print out resulting dict
print(months_dict)
