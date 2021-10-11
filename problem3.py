import numpy as np

n = 600851475143

def isPrime(test):
    n = int(np.sqrt(test))
    for i in range(2,n+1):
        if test % i == 0:
            return False
    return True

def primeFactorCandidates(n):
    primes = []
    checkTo = int(np.sqrt(n))+1
    for i in range(2,checkTo+1):
        if isPrime(i) == True:
            primes.append(i)
        else:
            pass
    return primes

def primeFactors(n, primes):
    factors = []
    for i in primes:
        if n % i ==0:
            factors.append(i)
        else:
            pass
    return factors

primes = primeFactorCandidates(n)

factors = primeFactors(n, primes)

print(factors[-1])