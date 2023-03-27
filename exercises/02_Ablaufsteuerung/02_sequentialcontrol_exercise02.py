import random

#initialize list of random_values
random_values = [0]*100

#get a list of 1000 random values between 0 and 99

rand_raw = [(random.randint(0,99)) for e in range(1000)]
print(rand_raw)

#loop through each index of random_value and place a random value between 0 and 99