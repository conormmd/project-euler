import numpy as np

i = 1
n = 0

circ_primes = []


def isPrime(test):
    n = int(np.sqrt(test))
    for i in range(2,n+1):
        if test % i == 0:
            return False
    return True

def circTest(test):
    str_test = str(test)
    n = len(str_test)
    i=0
    while i<n:
        i = i+1
        str_test = str_test[-1] + str_test[0:-1]
        if isPrime(int(str_test)) == False:
            return False
    return True

print(isPrime(13))
print(circTest(3001))

"""for i in range(2,1000000):
    if circTest(i) == True:
        circ_primes.append(i)

print(len(circ_primes))"""




