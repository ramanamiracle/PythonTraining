# WITHOUT A GENERATOR....
# To generate first 1,000,000 fib numbers, it has to store all of them in a list

def fib_list(max1):
    nums = []
    a, b = 0, 1
    while len(nums) < max1:
        nums.append(b)
        a, b = b, a+b
    return nums

# fib_list(1000000)


# USING A GENERATOR...
# To generate first 1,000,000 fib numbers,no list needed!
def fib_gen(max1):
    x = 0
    y = 1
    count = 0
    while count < max1:
        x, y = y, x + y
        yield x
        count += 1


for n in fib_gen(100):
    print(n, end=" ")
