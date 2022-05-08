
def febon(n):
    a, b = 1, 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


def febon_rec(n):
    if n <= 1:
        return 1

    n_1 = febon_rec(n-1)
    n_2 = febon_rec(n-2)
    nn = n_1 + n_2
    return nn


print(febon(20))
print(febon_rec(20))

