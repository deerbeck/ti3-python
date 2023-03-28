import random

#function to determin min max and mean of integers
def stat(l : list):
    # sort list to get easy acces to min and max value
    l.sort()

    #get min and max values of dataset
    min = l[0]
    max = l[-1]

    #calculate mean value using for loop and buffervariable
    mean_buf = 0
    for e in l:
        mean_buf += e
    mean = mean_buf/(len(l))

    #print out calculated values
    print(f"Min: {min}, Max: {max}, Mean: {mean}")


#generate workdataset
my_list = random.sample(range(10000), 1000)

#call function with given dataset as parameter
stat(my_list)