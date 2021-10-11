import numpy as np

n = 1000**2
digits = 3

def isPalindrome(test):
    string = str(test)
    n = len(string)
    for i in range(int(n/2)):
        if string[i] == string[-i-1]:
            continue
        else:
            return False
    return True


def findPalindromes(n):
    palindromes = []
    for i in range(0, n):
        if isPalindrome(i) == True:
            palindromes.append(i)
        else:
            pass
    return palindromes

def largestFactors(n):
    smallFactors = []
    bigFactors = []
    checkFrom = int(np.sqrt(n))
    for i in range(checkFrom, 0, -1):
        if n % i ==0:
            smallFactors.append(i)
            bigFactors.append(int(n/i))
        else:
            pass
    return smallFactors, bigFactors 

def largestPalindromeProduct(n, digits):
    palindromes = findPalindromes(n)
    palindromes.reverse()
    for i in palindromes:
        smallFactors, bigFactors = largestFactors(i)
        small = smallFactors[0]
        big = bigFactors[0]
        if len(str(small)) and len(str(big)) == digits:
            return i
        else:
            pass


print(
    largestPalindromeProduct(n,digits)
)