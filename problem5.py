import numpy as np

n = 20

def nonMatchElements(list1, list2):
    nonMatch = []
    for i in list1:
        if i not in list2:
            nonMatch.append(i)
        else:
            pass
    return nonMatch

def matchElements(list1, list2):
    match = []
    for i in list1:
        if i in list2:
            match.append(i)
        else:
            pass
    return match

def reduceExcessElements(masterList, tempList):
    for i in tempList:
        if masterList.count(i) < tempList.count(i):
            masterList = masterList + ([i]*( tempList.count(i) - masterList.count(i)))
        else:
            pass
    return masterList

def degeneracyRemover(n):
    raw = list(range(1,n+1))
    degeneracy = []
    for i in range(n, 1, -1):
        for j in raw[0:i-1]:
            if i == j:
                pass
            if (i/j).is_integer() == True:
                degeneracy.append(j)
            else:
                pass
    degeneracyRemoved = nonMatchElements(raw, degeneracy)
    return degeneracyRemoved

def isMultipleOfAll(multiples):
    start = multiples[-1]*multiples[-2]*multiples[-3]
    i = start - 1
    while i > 1:
        print(i)
        i = i+1
        for j in multiples:
            if i % j == 0:
                if j == multiples[-1]:
                    return i
                else:
                    continue
            else:
                break

def isPrime(test):
    if test == 1:
        return False
    n = int(np.sqrt(test))
    for i in range(2,n+1):
        if test % i == 0:
            return False
    return True

def primeFactors(test):
    remaining = test
    primeFactors = []
    while remaining > 1:
        print(remaining)
        for i in range(remaining, 1, -1):
            if test % i == 0 and isPrime(i) == True:
                primeFactors.append(i)
                remaining = int(remaining/i)
                break
            else:
                pass
    return(primeFactors)


def commonPrimeFactors(n):
    raw = list(range(1,n+1))
    commonPrimes = []
    for i in raw:
        tempPrimes = primeFactors(i)
        commonPrimes = reduceExcessElements(commonPrimes, tempPrimes)
    return commonPrimes


print(
    (np.prod(np.array(commonPrimeFactors(20))))
)




