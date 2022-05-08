
def fib():
    current, nxt = 1, 1
    while True:
        current, nxt = nxt, current + nxt
        yield current


result = fib()
print(result)

for _ in range(10):
    print(next(result))
