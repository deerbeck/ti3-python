import math

# task 1 calculate sum of 0 to n recursively


def sum_n(n):
    return 0 if n == 0 else n + sum_n(n-1)


# task 2 calcutlate sum of 0 to n via gaussian sumformula
def sum_gauss(n):
    return int(n*(n+1)/2)


# asserting sum functions
test_values = [5, 10, 50, 110]
for element in test_values:
    assert sum_n(element) == sum_gauss(element), "Solution is not the same"

# task 3 lambdafunctions
# input data
orders = [["34587", "Learning Python, Mark Lutz", 4, 40.95],
          ["98762", "Programming Python, Mark Lutz", 5, 56.80],
          ["77226", "Head First Python, Paul Barry", 3, 32.95]]


result = list(map(lambda order: (order[0], (order[2] * order[3] + 10) if (order[2] * order[3]) <= 100.00 else (order[2] * order[3])), orders))

print(result)