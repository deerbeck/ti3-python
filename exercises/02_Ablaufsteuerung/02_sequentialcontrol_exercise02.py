import random

#initialize list of random_values
random_values = [0]*100

#get a list of 1000 random values between 0 and 99
random_raw = [(random.randint(0,99)) for e in range(1000)]

#loop through possible number 0-99 an return frequency of that number in 1000
for i in range(100):
    random_values[i] = random_raw.count(i)
    #print out all random values generated less than 5 times using string format.
    if (random_values[i] < 5): print(f"Wert {i} wurde {random_values[i]} ermittelt.")

