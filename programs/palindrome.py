n = 141
t = n
rev = 0

while t > 0:
    r = t % 10
    rev = rev * 10 + r
    print(rev)
    t = t//10

if rev == n:
    print("Palindrome")
else:
    print("Not Palindrome")
