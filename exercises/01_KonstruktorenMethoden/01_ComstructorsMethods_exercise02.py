#startlist
l = ['München', 'Regensburg', 'Augsburg', 'Nürnberg', 'Scheinfurt', 'Bayreuth', 'Ulm']

#use list methods to learn

#add element to list on the last place
l.append("append")
print(l)
#insert element to list on given index
l.insert(4,"insert")
print(l)
#remove given element from list
l.remove("Scheinfurt")
print(l)
#remove last item of the list and return it
print(l.pop())
print(l)
#return number of occurrences of given value
print(l.count("Augsburg"))
#sort list in ascending order
l.sort()
print(l)