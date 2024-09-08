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
    LIMIT = 10000
    for odd_number in range(7, LIMIT, 2):
        if not is_prime(odd_number):
            result_found = False
            for num in range(2, odd_number):
                if is_prime(num):
                    diff = odd_number - num
                    power_num = 1
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

# TODO
def lattice_paths():
    """
    While x and y are less than (dimension)
    scenario:
    x = 1, y = 0
    x = 2, y = 0
    """
    # dimension = 2
    # x, y = 0
    # while x < dimension and y < dimension:
    pass

def triangle_num(num):
    result = (num * (num + 1))/2
    return int(result) if int(result) == result else None

def is_pentagonal(num):
    result = (1 + (1 + 24 * num) ** 0.5) / 6
    return int(result) if int(result) == result else None

def is_hexagonal(num):
    result = (1 + (1 + 8 * num) ** 0.5) / 4
    return int(result) if int(result) == result else None

def traingle_pentagonal_hexagonal():
    for index in range(286, 100000):
        if result := triangle_num(index):
            if is_pentagonal(result) and is_hexagonal(result):
                return result
    return None

def quad_primes():
    """
    Find max primes for a quadratic formula
    and find the product of a and b for
    a <= 1000, b <= 1000 and
    n2 + an + b

    Brute force:
    For every a and b, get the number of consecutive primes.
    store the max consecutive primes and the product of that. 
    """

    def quad_formula(n, a, b) -> int:
        return n**2 + a*n + b
    
    def get_consecutive_primes(a, b) -> int:
        n = 0
        result = 0
        while True:
            cur_value = quad_formula(n, a, b)
            if not is_prime(cur_value):
                break
            result += 1
            n += 1

        return result
    
    max_consecutive_primes = 0
    product_a_b_max_primes = 0
    for a in range(-1001, 1001):
        for b in range(-1001, 1001):
            num_consecutive = get_consecutive_primes(a, b)
            if num_consecutive > max_consecutive_primes:
                product_a_b_max_primes = a * b
                max_consecutive_primes = num_consecutive
                
    return product_a_b_max_primes

def num_spiral_diagonals():
    # cur_sum = 0
    # spacing = 1
    # dimension = 1
    # spacing = 0 
    # while dimension != 1001:
    #     spacing += 2
    #     for num in range(1, 10000))
    #     cur_sum += 

    pass

def generate_pentagon_numbers(num_range: int):
    pentagonal_numbers = [pentagon_num for pentagon_num in range(num_range) if is_pentagonal(pentagon_num)]

    return pentagonal_numbers
            
def pentagon_numbers():
    """
    For two pentagon numbers that is a pentagon number
    when summed up or subtracted. Store the minimum for
    a large number of pentagon numbers.

    TODO: optimize due to large range.
    
    Solution: 5482660
    """
    RANGE = 10000000
    pentagon_numbers = generate_pentagon_numbers(RANGE)
    result = 0

    for num1 in pentagon_numbers:
        for num2 in pentagon_numbers:
            if num1 + num2 in pentagon_numbers and abs(num1 - num2) in pentagon_numbers:
                diff = abs(num1 - num2)
                result = min(result, diff) if result != 0 else diff
                
    return result


def three_arithmetic_seq(nums: list) -> bool:
    """
    Checks if any three numbers in the list are in an
    arithmetic sequence.
    """
    from itertools import combinations
    
    res = None
    
    if len(nums) >= 3:
        # print(nums)
        for a, b, c in combinations(nums, 3):
            # Sort the numbers to simplify the arithmetic sequence check
            a, b, c = sorted([a, b, c])
            # Check if they form an arithmetic sequence
            if b - a == c - b:
                res = [a, b, c]

    return res

def prime_permutations():
    """
    For each 4 digit number, check if
    permutations increase by a certain number and
    are prime.
    """

    from itertools import permutations

    result = []

    for num in range(1000, 10000):
        digits = list(str(num))
    
        # Generate permutations
        digit_perms = set(permutations(digits, 4))
    
        # Convert permutations to integers and filter out those starting with '0'
        str_perms = [''.join(perm) for perm in digit_perms if perm[0] != '0']
        perms = sorted([int(perm) for perm in str_perms])
            
        # Filter only primes
        perms = list(filter(is_prime, perms))
        
        # Check if any nums are in an arithmetic sequence
        seq = three_arithmetic_seq(perms)

        if seq:
            # arithmetic seq found, concatenate values
            value = ''.join(map(str, seq))
            result.append(value)

    for res in result:
        if res != "148748178147":
            # return the value that is not `148748178147`
            return res

def pandigital_products():
    """
    Find all multiplicant, multiplier, and product
    that have all of the pandigital products. 
    """
    pass

def circular_primes():
    """
    Rotations of a number:
    
    """
    
    from itertools import permutations
    
    RANGE = 1000000
    prime_rotations = set()
    
    for num in range(2, RANGE):
        if num in prime_rotations:
            continue

        # Get all rotations of a number
        str_num = str(num)
        perms  = [int(str_num[i:] + str_num[:i]) for i in range(len(str_num))]

        non_prime_found = False
        for perm in perms:
            if not is_prime(perm):
                non_prime_found = True
                break

        if not non_prime_found:
            for permutation in perms:
                prime_rotations.add(permutation)

    return len(prime_rotations)

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)  # Step 1: Initialize all entries as True
    p = 2
    
    # Step 2: Start with the first prime number
    while p * p <= n:
        # If primes[p] is still True, it is a prime
        if primes[p] == True:
            # Mark all multiples of p from p*p to n as False
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    # Step 3: Collect all prime numbers
    prime_numbers = [p for p in range(2, n + 1) if primes[p]]
    return prime_numbers

def consecutive_primes():
    """
    consecutive prime sum under 1 million that
    results in the larges prime number.

    Starting point can be anywhere.

    sliding window
    """
    RANGE = 1000000
    primes = sieve_of_eratosthenes(RANGE)
    prime_set = set(primes)  # Use a set for O(1) prime lookup
    max_length = 0
    max_prime = 0

    # Use two pointers (start, end) to find the longest sum of consecutive primes
    for start in range(len(primes)):
        current_sum = 0
        for end in range(start, len(primes)):
            current_sum += primes[end]
            if current_sum > RANGE:
                break
            current_length = end - start + 1
            if current_sum in prime_set and current_length > max_length:
                # Calculate max for new max
                max_length = current_length
                max_prime = current_sum

    return max_prime

if __name__ == "__main__":
    #print(digit_cancelling_fractions())
    #print(nth_power())
    # print(quad_primes())
    # print(pentagon_numbers())
    # print(prime_permutations())
    # print(circular_primes())
    # print(consecutive_primes())
    # print(consecutive_primes())

    # Too Slow
    #print(find_prime_pair_sets())
    #print(goldbachs_conjecture())
    #print(traingle_pentagonal_hexagonal())
    
    pass
