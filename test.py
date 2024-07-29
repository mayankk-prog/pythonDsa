def f(n):
    s = 0
    for i in range(1, n + 1):
        if n // i == i and n % i == 0:
            s = 1
    print( s % 2 == 1)
