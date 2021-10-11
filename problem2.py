import numpy as np

n = 4000000

def nextFib(cap):
    fib=[1,1]
    i=1
    while fib[-1]+fib[-2] < cap:
        fib.append(fib[-1]+fib[-2])
    return fib 

def evenSum(array):
    n = len(array)
    total = 0
    for i in array:
        if i%2 == 0:
            total = total + i
        else:
            pass
    return total

print(
    evenSum(
        nextFib(n)))


