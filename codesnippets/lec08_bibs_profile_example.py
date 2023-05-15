from memory_profiler import profile

@profile
def generate_numbers(n):
    return (i**2 for i in range(n))

@profile
def list_numbers(n):
    return [i**2 for i in range(n)]

# Generate 1000000 numbers using a generator
gen_nums = generate_numbers(1000000)

# Generate 1000000 numbers using a list comprehension
list_nums = list_numbers(1000000)