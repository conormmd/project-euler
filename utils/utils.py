import numpy as np

def check_if_multiple(number, factor):
    if number % factor == 0:
        return True
    else:
        return False

def check_if_even(number):
    return check_if_multiple(number, 2)

def check_if_prime(number):
    check_limit = int(np.sqrt(number))
    if number == 1:
        return False
    elif number == 2:
        return True
    elif check_if_even(number):
        return False
    # Check all odds from 3
    for factor in range(3, check_limit+1, 2):
        if number % factor == 0:
            return False
    return True

def check_if_square(number):
    return np.sqrt(number) == int(np.sqrt(number))

def get_factors(number, lims=None, get_first_factor=False):
    if lims is None:
        lim_low = 2
        lim_high = int(np.sqrt(number)) + 1
    else:
        lim_low = lims[0]
        lim_high = lims[1]

    factors = []

    for factor in range(lim_low, lim_high):
        if number % factor == 0:
            factor_1 = factor
            factor_2 = int(number/factor)

            if get_first_factor:
                return [factor_1, factor_2]

            factors.append((factor_1, factor_2))

    return factors


def get_factors_which_are_prime(number):
    check_limit = int(np.sqrt(number))
    prime_factors = []

    for factor in range(2, check_limit+1):
        if number % factor == 0:
            factor_1 = factor
            factor_2 = number/factor

            if check_if_prime(factor_1):
                prime_factors.append(factor_1)
            if check_if_prime(factor_2):
                prime_factors.append(factor_2)

    # for case when square number
    return list(set(prime_factors))

def check_if_palindrome(candidate):
    candidate = str(candidate)
    if candidate == candidate[::-1]:
        return True
    else:
        return False

def get_prime_factors(number):
    prime_factors = []

    if check_if_prime(number):
        prime_factors.append(number)
        return prime_factors

    factors = get_factors(number, get_first_factor=True)
    # factors = [factor for factor_tuple in factors for factor in factor_tuple]

    for factor in factors:
        if check_if_prime(factor):
            prime_factors.append(factor)
        else:
            prime_factors += get_prime_factors(factor)

    return prime_factors

def combine_prime_factors(factors_master, factors_to_add):
    for factor in set(factors_to_add):
        count_master = factors_master.count(factor)
        count_add = factors_to_add.count(factor)

        if count_add > count_master:
            factors_master += [factor]*(count_add-count_master)
        else:
            pass

    return factors_master

def sieve_of_eratosthenes(limit):
    check_limit = int(np.sqrt(limit))
    prime_number_line = np.ones(limit+1, dtype=np.bool)
    prime_number_line[0] = False
    prime_number_line[1] = False

    for number in range(2, check_limit+1):
        if prime_number_line[number]:
            prime_number_line[2*number::number] = False

    number_line = np.arange(0,limit+1, dtype='int64')
    primes = number_line[prime_number_line]

    return primes