def isPrime(x):
    if x == 2:
        return 1
    for i in range(2,x):
        if x % i == 0:
            return 0
    if i == x-1:
        return 1

print(isPrime(2))
print(isPrime(3))
print(isPrime(4))
