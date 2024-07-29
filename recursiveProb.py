def sumN(n):
    if n==1:
        return 1
    return n+sumN(n-1)

print(sumN(10))


def sumOddN(n):
    if n == 1:
        return 2
    return 2*n-1 + sumOddN(n - 1)

def fact(n):
    if n==0:
        return 1
    return n* fact(n-1)
print(fact(5))