import numpy as np

multiples = []

n = 1000

def checkMult(test, mult):
    if test % mult == 0:
        return True
    else:
        return False

for i in range(n):
    if checkMult(i, 3) or checkMult(i, 5) == True:
        multiples.append(i)
    
print(sum(multiples))