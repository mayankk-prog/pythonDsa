def printN(n):
    if n>0:
        printN(n-1)
        print(n, end= " ")
printN(10)

def printRev(n):
    if n>0:
        print(n, end= " ")
        printRev(n-1)
printRev(10)

def printOdd(n):
    if n>0:
        printOdd(n-1)
        print(2*n-1, end= " ")
printOdd(10)