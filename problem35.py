import numpy as np

i = 1
n = 0

primes = [2]

def primeTest(test, primes):
    n = len(primes)
    num_factors = 0
    for i in range(n):
        test_type = test/primes[i]
        if float.is_integer(test_type) == True:
            num_factors = num_factors+1
        else:
            continue
    if num_factors == 0:
        return(test)
    else:
        return


while n<100:
    i = i+1
    j = 2*i-1
    test = primeTest(j,primes)
    if type(test) == int:
        primes.append(test)
    n_primes = len(primes)



print(primes)

