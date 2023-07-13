import math

# task 1 calculate sum of 0 to n recursively

def sum_rec(n):
    return 0 if n == 0 else (n + sum_rec(n-1))
    
print(sum_rec(5),sum_rec(10),sum_rec(50),sum_rec(100))

# task 2 calculate gaussian sum formula

def gaus_sum(n):
    return (n*(n+1))/2

assert(sum_rec(5) == gaus_sum(5))
assert(sum_rec(10) == gaus_sum(10))
assert(sum_rec(50) == gaus_sum(50))
assert(sum_rec(100) == gaus_sum(100))

# task 3 return price
orders = [ ["34587","Learning Python, Mark Lutz", 4, 40.95],
["98762","Programming Python, Mark Lutz", 5, 56.80],
["77226","Head First Python, Paul Barry",3,32.95]]

price_calc = lambda x,y: x*y if x*y>=100 else x*y+10

for order in orders:
    print((order[0], price_calc(order[-2],order[-1])))

