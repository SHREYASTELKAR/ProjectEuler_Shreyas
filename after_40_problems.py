import itertools
from ProjectEuler import is_prime

def digit_cancelling_fractions():
    numerator, denominator = 10 , 11
    
    results = set()
    while numerator < 100:
        denominator = numerator + 1
        while denominator < 100:
            if len(results) == 4:
                from fractions import Fraction
                current_prod = Fraction(1, 1)
                for numerator, denominator in results:
                    current_prod *= Fraction(numerator, denominator)
                return current_prod.denominator
            
            # tens digits of denominator and ones digit of numerator is the same
            if (denominator // 10 == numerator % ((numerator// 10) * 10) and (denominator % ((denominator// 10) * 10)) != 0):
                if ((numerator / denominator) == (numerator // 10) / (denominator % ((denominator// 10) * 10))):
                    results.add((numerator, denominator))
            denominator += 1
        numerator += 1

def nth_power():
    """ Returns the number of
    values in which the length
    of the result equals the
    power of the number
    """
    
    result = 0
    THRESHOLD = 100000
    power = 1
    while power < 50:
        num_found = False
        for num in range(1, THRESHOLD):
            if len(str(num ** power)) == power:
                   result += 1
                   num_found = True
        if not num_found:
            break
        power += 1

    return result

def get_primes_to_limit(limit):
    """ Get all primes up till
    the limit
    """

    result = [num for num in range(2, limit + 1) if is_prime(num)]

    return result
    
def retrieve_concatenated_pair_primes(primes):
    """Takes in a combination of 5
    primes and checks if the concatenation
    of each permutation is prime.
    
    Returns the sum of the 5 primes
    which all have this behavior.
    """
    
    prime_combinations = itertools.combinations(list(primes), 2)
    #print(list((prime_combinations)))
    
    for prime_combination in list(prime_combinations):
        #print(prime_combination)
        first_prime, second_prime = prime_combination
        if not (is_prime(int(str(first_prime) + str(second_prime))) and is_prime(int(str(second_prime) + str(first_prime)))):
            return None

    return sum(primes)


def find_prime_pair_sets():

    LIMIT = 10000
    primes = get_primes_to_limit(LIMIT)

    primes_set = list(itertools.combinations(primes, 5))

    for five_primes in primes_set:
        if sum_primes := retrieve_concatenated_pair_primes(five_primes):
            return sum_primes
    return None

def goldbachs_conjecture():
    # TODO: Fix and debug
    
    LIMIT = 1001
    for odd_number in range(7, LIMIT, 2): 
        result_found = False
        for num in range(2, odd_number):
            if is_prime(num):
                diff = odd_number - num
                power_num = 0
                while 2 * power_num**2 <= diff:
                    if 2 * power_num**2 == diff:
                        result_found = True
                        break
                    power_num += 1
            if result_found:
                break
        if not result_found:
            return odd_number
    return None
            
if __name__ == "__main__":
    #print(digit_cancelling_fractions())
    #print(nth_power())

    # Too Slow
    #print(find_prime_pair_sets())
    print(goldbachs_conjecture())
