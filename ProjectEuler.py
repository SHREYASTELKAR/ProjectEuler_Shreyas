from math import sqrt

def mult_3and5():
    cur_sum = 0
    for num in range(1000):
        if (num % 3 == 0) or (num % 5 == 0):
            cur_sum += num
    
def fibonacci():
    sum = 0
    term1 = 1
    term2 = 2
    
    while term1 < 4_000_000:
        if (term1) % 2 == 0:
            sum += term1
            
        temp1 = term1
        term1 = term2
        term2 = temp1 + term2 
    return sum
            
def three_digit_palindrome():
    cur = 0
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            i = str(i)
            j = str(j)
            if i[2] != 0 or j[2] != 0 or (i[2] != 5 and j[2] != 2) or (i[2] != 2 and j[2] != 5):
                if (str(int(i) * int(j)))[::-1] == str(int(i) * int(j)):
                    cur = max(cur, int(i) * int(j))
                    
    return cur

def smallest_multiple():
    start_num = 20
    while True:
        for i in range(1, 21):
            if start_num % i != 0:
                break
            if i == 20:
                return start_num
            
        start_num += 20

def sum_square():
    c = 0
    s = range(1, 101) #list
    su = sum(s)**2
    for n in s:
        c+=n**2
    return su - c

def power_sum():
    s = 0
    for i in str(2**1000):
        s += int(i)
    return s

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def nthprime(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num
        

# 3^2 + 4^2 = 5^2, 9 + 16 = 25, 3 + 4 + 5 = 12
# Find pythagorean triple where a + b + c = z

def pythagorean():
    
    for a in range(1, 1000):
        for b in range(a, 1000):
            c_squared = a**2 + b**2
            c = sqrt(c_squared)
            if a + b + c == 1000:
                return int(a * b * c)


def str_to_matrix(inp):
    matrix = []
    start = 0
    for row_i in range(20):
        new_l = []
        for col_i in range(start, start + 50):
            new_l.append(int(inp[col_i]))
        matrix.append(new_l)
        start += 50
    return matrix


# need to check for last row where it should not go to the next line. 

def adj_prod(inp, n):
    matrix = str_to_matrix(inp)
    cur_prod = 0
    new_prod = 1
    row_i = 0
    i_step = 0
    
    while row_i < (len(matrix) - 1):
        for col_i in range(0, len(matrix[row_i])): #0-49
            
            #with overlap
            i_step = col_i
            num = i_step + n
            
            while i_step < num:
                
                if (i_step//(len(matrix[row_i]))) > 0:
                    r_i = row_i + 1
                else:
                    r_i = row_i
                
                print(i_step % (len(matrix[row_i])),r_i)
                
                new_prod *= matrix[r_i][i_step % (len(matrix[row_i]))]
                i_step += 1

            cur_prod = max(cur_prod, new_prod)
            new_prod = 1
            
        row_i += 1
        
    return cur_prod

def sum_primes(num):
    #sum of primes up to n
    res = 0
    for n in range(num):
        if is_prime(n):
            res += n
    return res

def str_to_matrix1(inp):
    
    count = 0
    matrix = []
    for row in range(20):
        new_l = []
        for col in range(0, 59, 3):
            if inp[count] == '0':
                st = inp[count + 1]
            else:
                st = inp[count] + inp[count + 1]
                
            new_l.append(int(st))
            
            if col != 57:
                count += 3
            else:
                count+=2
            
        matrix.append(new_l)
    return matrix

# Check right, down and diagonal right, if at right side end of matrix, only check down. Check at last 3 rows only do right 

def right(matrix, r, c):
     return matrix[r][c] * matrix[r][c + 1] * matrix[r][c + 2] * matrix[r][c + 3]
 
def down(matrix, r, c):
    return matrix[r][c] * matrix[r + 1][c] * matrix[r + 2][c] * matrix[r + 3][c]

def diag_right(matrix, r, c):
    return matrix[r][c] * matrix[r + 1][c + 1] * matrix[r + 2][c + 2] * matrix[r + 3][c + 3]

def diag_left(matrix, r, c):
    return matrix[r][c] * matrix[r + 1][c - 1] * matrix[r + 2][c - 2] * matrix[r + 3][c - 3]

def grid_product(inp):
    
    cur_prod = 0
    matrix = str_to_matrix1(inp)
    
    for row_i in range(len(matrix)):
        for col_i in range(len(matrix[row_i])):
            if col_i <= len(matrix[row_i]) - 4:
                cur_prod = max(cur_prod, right(matrix, row_i, col_i))
            if row_i <= len(matrix) - 4:
                cur_prod = max(cur_prod, down(matrix, row_i, col_i))
            if row_i <= len(matrix) - 4 and col_i <= len(matrix[row_i]) - 4:
                cur_prod = max(cur_prod, diag_right(matrix, row_i, col_i))
            if row_i <= len(matrix) - 4 and col_i >= 3:
                cur_prod = max(cur_prod, diag_left(matrix, row_i, col_i))
    return cur_prod

# loop through 1 mil, try collatz seq, keep count 
def longest_collatz(nums):
    chain = {}
    for num in range(1, nums):
        count = 0
        n = num
        while n != 1:
            if n % 2 == 0:
                n /= 2
            else:
                n = (3 * n) + 1
            count += 1
            
        chain[count] = num
    
    largest = 0
    for count in chain:
        largest = max(largest, count)
    
    return chain[largest] 

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def sum_factorial(num):
    
    fac = factorial(num)
    return sum(int(digit) for digit in str(fac))

def fibonacci_rec(num):
    
    if num == 1 or num == 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

def fibonacci_iter():
    first, second = 1, 1
    count = 1
    while len(str(first)) < 1000:
        first, second = second, first + second
        count += 1
    return count

    
def fib_digits():
    num = 12
    while True:
        if len(str(fibonacci(num))) == 1000:
            return num  
        num += 1

def digit_fact():
    l = []
    num = 11
    while num < 50000:
        s = s = sum(factorial(int(digit)) for digit in str(num))
        if s == num:
            l.append(num)
        num += 1
    return sum(l)

def large_sum(inp2):
    #Save nums in arrays
    nums = []
    k = 0
    new_l = []
    total_sum = 0
    
    while k < (50 * 100):
        if (k % 50 == 0 and k != 0):
            nums.append(new_l)
            new_l = []
        new_l.append(int(inp2[k]))
        k += 1
    nums.append(new_l)
    
    for lst in nums:

        number_str = ''.join(str(digit) for digit in lst)

        number = int(number_str)

        total_sum += number

    return str(total_sum)[:10]

def name_scores():
    with open('names.txt', 'r') as file:
        file_contents = file.read()
    names = [name.strip('"') for name in file_contents.split(',')]
    names = sorted(names)
    
    total_score = 0
    
    for i, name in enumerate(names, start=1):
        name_score = 0
        for char in name:
            name_score += (ord(char) - ord('A') + 1)
        total_score += (name_score * i)
    
    return total_score

import math

def factors(n):
    fac = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            fac.add(i)
            fac.add(n // i)
    return list(fac)

def triangle_factors():
    i = 1
    n = 1
    while len(factors(n)) <= 500:
        i += 1
        n = n + i  
    return n

def dbase_palindrome():
    res = 0
    for num in range(1000000):
        if bin(num)[2:] == bin(num)[2:][::-1] and str(num) == str(num)[::-1]:
            res += num
    return res

def truncatable_primes():
    count = 0
    num = 11
    res = 0
    not_trunc = False
    while count < 11:
        for i in range(0, len(str(num))):
            if not is_prime(int(str(num)[i:])) or not is_prime(int(str(num)[:(i + 1)])):
                not_trunc = True
                break
        if not_trunc == False:  
            res += num
            count += 1
        else:
            not_trunc = False
        num += 1
    return res

def self_powers():
    res = 0
    for i in range(1, 1001):
        res += i ** i 
    return str(res)[-10:]

from itertools import permutations

def number_permutations(number: str):
    # Convert the number to a list of its digits
    digits = [digit for digit in number]
    
    # Generate permutations of digits
    digit_perms = permutations(digits)
    perms = [int(''.join(perm)) for perm in digit_perms]
    return perms[999999]

def dig_fifth_powers():
    res = 0
    for num in range(2, 1000000):
        cur_sum = 0
        for dig in str(num):
            cur_sum += (int(dig) ** 5)
        if cur_sum == num:
            res += num
    return res

def distinct_powers():
    s = set()
    for a in range(2, 101):
        for b in range(2, 101):
            s.add(a ** b)
    return len(s)

def sub_str_div():
    num = '0123456789'
    divisor_l = [2, 3, 5, 7, 11, 13, 17]
    res = 0
    
    
    l_digits = [dig for dig in num]
    l_perm = permutations(l_digits)
    l = [int(''.join(perm)) for perm in l_perm if perm[0] != '0']
    
    for num in l:
        not_sub = True
        ind = 0
        n = str(num)
        for i in range(1, 8):
            if (int(n[i] + n[i + 1] + n[i + 2]) % divisor_l[ind] == 0):
                ind += 1
            else:
                not_sub = False
                break
        if not_sub:
            res += num
    return res

def champ_constant():
    res_str = ""
    for nums in range(1, 10000000):
        res_str += str(nums)
    
    return int(res_str[0]) * int(res_str[9]) * int(res_str[99]) * int(res_str[999]) * int(res_str[9999]) * int(res_str[99999]) * int(res_str[999999])

from enum import Enum
def counting_sundays():
    #Simulate days from (1 Jan 1900) to (31 Dec 2000) and count Sundays that fell on the first of the month, only count from 1901 to 2000
    #reset day after hitting days_month
    res = 0
    cur_year = 1900
    day_type = 0
    day_types = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    days_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    
    #itterate through the years
    while cur_year != 2001:
        for month, d in enumerate(days_month):
            if month == 1:
                if (cur_year % 4 == 0 and cur_year % 100 != 0) or (cur_year % 400 == 0):
                    #check century
                    days = 29
                else:
                    days = 28
            else:
                days = d 
            
            for day in range(1, days + 1):
                #check sunday
                if day == 1:
                    if day_types[(day_type % len(day_types))] == 'Sunday' and cur_year >= 1901:
                        res += 1
                day_type += 1
        cur_year += 1
    return res

def permuted_multiples():
    
    for num in range(10, 1000000):
        found_num = True
        for i in range(2, 7):
            if sorted(str(num)) != sorted(str(num*i)):
                found_num = False
                break
        if found_num == True:
            return num
    return False

    """
    p = 120
    a,b,c = 20 48 52, Law of cosines? 
    """
def integ_right():
    d = {}
    for a in range(1, 10000):
        for b in range(a, 10000):
            c_squared = a**2 + b**2
            c = sqrt(c_squared)
            if c.is_integer():  
                p = a + b + c
                
                if p >= 1000:
                    break
                if p not in d:
                    d[p] = 1
                else:
                    d[p] += 1
                                        
    return max(d, key=d.get)

def comb_selectors():
    count = 0
    for n in range(1, 101):
        for r in range(1, n):
            res = factorial(n) / (factorial(r) * factorial(n - r))
            if res >= 1000000:
                count += 1
    return count

def triangle_word(num):
    for n in range(10000):
        if num == (0.5 * n * (n + 1)):
            return True
    return False

def triangle_nums():
    with open('words.txt', 'r') as file:
        f = file.read()
    names = [name.strip('"') for name in f.split(',')]
    
    count = 0
    for name in names:
        word_res = 0
        for char in name:
            val = ord(char) - ord('A') + 1
            word_res += val
        if triangle_word(word_res):
            count += 1
    return count


def prime_fac(num):
    # Example 20, 20 /2 = 10, 10 / 2 = 5, 
    # 5 / 3, 
    # 5 / 5 = 1, 
    startOdd = 3
    #last_num = 1
    facs = set()
    
    while (num % 2 == 0):
        facs.add(2)
        num //= 2
    
    while num != 1:
        while (num % startOdd == 0):
            facs.add(startOdd)
            num //= startOdd
        startOdd += 2
        
    return facs

def get_prime_factors():
    l_4 = []
    count = 0
    for num in range(647, 1000000):
        if len(prime_fac(num)) == 4:
            l_4.append(num)
            count += 1
            if count == 4:
                return l_4[0]
        else:
            count = 0
            l_4 = []
    return l_4

def check_pandig(num):
    for n in range(1, len(str(num)) + 1):
        if str(n) in str(num) and len(set(str(num))) == len(str(num)):
            continue
        else:
            return False
    return True

#takes a while
def pandig_prime():
    val = 0
    for num in range(4213, 10000000):
        if is_prime(num) and check_pandig(num):
            val = max(val, num)
    return val

def consec_primes():
    max_chain = 0
    for num in range(2, 1000000):
        chain = 0
        total = 0
        if is_prime(num):
            sub_num = 2
            while total < num:
                if is_prime(sub_num):
                    total += sub_num
                    chain += 1
                sub_num += 1
            if total == num:
                max_chain = max(chain, max_chain)
    return max_chain
  
def pand_multiples():
    max_prod = 0
    
    for num in range(1, 10000):  # Upper limit is arbitrary but should be sufficient
        pand_str = ""
        mult = 1
        while len(pand_str) < 9:
            prod = num * mult
            pand_str += str(prod)
            if check_pandig(int(pand_str)):
                max_prod = max(max_prod, int(pand_str))
            mult += 1
    
    return max_prod


        # if prod > 918273645:
        #     print(prod)
        #     max_prod = max(prod, max_prod)
        
        # prod = num * mult #9 * 2 = 18, 9 * 3 = 27 6
        
        # if mult == 3 and prod > 987654321:
        #     break
        
        # if pand_str != "":
            
        #     for c in str(prod): 
        #         if c not in pand_str:
        #             pand_str += str(c)
        #         else:
        #             not_found = True
        #             break
                
        #     if not_found == True:
        #         pand_str = ""
        #         mult = 2
        #         num += 1
        #     else:
        #         mult+=1
        #         not_found == False
        # else:      
        #     pand_str += str(prod)            #1827
        #     mult += 1
            
    #return max_prod

def find_repeating_cycle(s):
    n = len(s)
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            cycle = s[:i]
            if cycle * (n // i) == s:
                return cycle
    return None

def recip_cycles():
    max_repeat = 0
    max_d = 0
    
    for d in range(1, 1000):
        decimal_part = format(1 / d, '.10000f')
        print(decimal_part)
        #find repeating chars
        cycle = find_repeating_cycle(decimal_part)
        if cycle:
            if len(cycle) > max_repeat:
                max_d = d
                max_repeat = len(cycle)
    return max_d

def factors1(n):
    """Return the list of proper divisors of n (excluding n itself)."""
    return [i for i in range(1, n //2 + 1) if n % i == 0]

def amicable_numbers():
    total = 0
    seen = set()
    #check if sum is over limit
    for n in range(2, 10000): 
        l  = factors1(n)
        sum_fac = sum(l)
        
        if sum_fac != n and sum_fac < 10000:  # Check if it's not the same number and less than 10000
            if sum(factors1(sum_fac)) == n and n not in seen:
                seen.add(n)
                seen.add(sum_fac)
                total += n + sum_fac
    return total

def is_palindrome(s):
    if s == s[::-1]:
        return True
    return False

def lychrel_nums():
    count = 0
    found_pal = False
    for nums in range(1, 10000):
        cur_val = nums
        for i in range(50):
            cur_val = cur_val + int(str(cur_val)[::-1])
            if is_palindrome(str(cur_val)):
                found_pal = True
        
        if found_pal != True:
            count += 1
        found_pal = False    
    return count  

def pow_digit_sum():
    total = 0
    for a in range(1, 100):
        for b in range(1, 100):
            cur_sum = 0
            for dig in str(a ** b):
                cur_sum += int(dig)
                
            total = max(cur_sum, total)
            
    return total

from fractions import Fraction

def sqrt_conv(n): # 1 index 
    fraction = Fraction(1, 2) 
    for i in range(1, n):
        fraction = 1 / (2 + fraction)
    return 1 + fraction  
    

def frac_sqrt_conv():
    count = 0
    for i in range(1, 1000):
        frac = sqrt_conv(i)
        numerator, denominator = frac.numerator, frac.denominator
        if len(str(numerator)) > len(str(denominator)):
            count += 1
    return count

def shapes_nums():
    for t in range(286, 1000):
        t_n = t * (t + 1) / 2
        for p in range(1000):
            p_n = p * ((3 * p) - 1) / 2
            for h in range(1000):
                h_n = h * ((2 * h) - 1)
                
                if t_n == p_n == h_n:
                    return t
                
def is_abundant(n):
    return sum(factors1(n)) > n

def abundant_sums():
    total = 0
    for a in range(5000, 7000):
        for b in range(5000, 7000):
            sum_abund = 0
            if is_abundant(a) and is_abundant(b):
                sum_abund = a + b
                if sum_abund > 28123:
                    return total
                total += a + b

def non_abundant_sums():
    LIMIT = 28123
    result = 0

    abundant_numbers = [x for x in range(12, LIMIT + 1) if is_abundant(x)]
    abundant_sums = set()
    
    for i in range(len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            abundant_sum = abundant_numbers[i] + abundant_numbers[j]
            if abundant_sum <= LIMIT:
                abundant_sums.add(abundant_sum)
    
    non_abundant_sum = sum(x for x in range(1, LIMIT + 1) if x not in abundant_sums)
    
    return non_abundant_sum
        

def is_pentagonal(num):
    for p_i in range(1, num):
        if num == p_i * ((3 * p_i) - 1) / 2:
            return True
    return False

def pent_sum():
    for p1 in range(1, 1000):
        for p2 in range(1, 1000): 
            if is_pentagonal(p1) and is_pentagonal(p2):
                if is_pentagonal(p1 + p2) and is_pentagonal(abs(p2 - p1)):
                    return abs(p2 - p1)

def num_letter():
    single = [3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8] # 1-19
    tens = [3, 6, 6, 5, 5, 5, 7, 6, 6] # 20-90
    HUNDRED = 7
    THOUSAND = 11
    AND = 3
    total = 0

    for cur_num in range(1, 1001):
        count_num = 0
      
        if cur_num == 1000:
            count_num += THOUSAND
            
        if cur_num < 1000 and cur_num >= 100:
            count_num += single[(cur_num // 100) - 1] + HUNDRED
            cur_num = cur_num % 100
            
            if cur_num != 0:  
                count_num += AND
            
                
        if cur_num < 100 and cur_num != 0:
            if cur_num // 10 != 0:
                if cur_num > 10 and cur_num < 20:
                    count_num += single[cur_num - 1]
                else:
                    count_num += tens[(cur_num//10) - 1]
            
            if cur_num % 10 != 0 and not (cur_num > 10 and cur_num < 20):
                count_num += single[(cur_num % 10) - 1]


        total += count_num
    return total
                
if __name__=="__main__":

    print(non_abundant_sums())
    #print(mult_3and5())
    # print(fibonacci())
    #print(prime_fac())
    #print(three_digit_palindrome())
    #print(smallest_multiple())
   # print(sum_square())
    #print(power_sum())
    #print(nthprime(10001))
    #print(pythagorean())
    
    inp = "73167176531330624919225119674426574742355349194934"\
    "96983520312774506326239578318016984801869478851843"\
    "85861560789112949495459501737958331952853208805511"\
    "12540698747158523863050715693290963295227443043557"\
    "66896648950445244523161731856403098711121722383113"\
    "62229893423380308135336276614282806444486645238749"\
    "30358907296290491560440772390713810515859307960866"\
    "70172427121883998797908792274921901699720888093776"\
    "65727333001053367881220235421809751254540594752243"\
    "52584907711670556013604839586446706324415722155397"\
    "53697817977846174064955149290862569321978468622482"\
    "83972241375657056057490261407972968652414535100474"\
    "82166370484403199890008895243450658541227588666881"\
    "16427171479924442928230863465674813919123162824586"\
    "17866458359124566529476545682848912883142607690042"\
    "24219022671055626321111109370544217506941658960408"\
    "07198403850962455444362981230987879927244284909188"\
    "84580156166097919133875499200524063689912560717606"\
    "05886116467109405077541002256983155200055935729725"\
    "71636269561882670428252483600823257530420752963450"
    
    #print(adj_prod(inp, 13))
    #print(sum_primes(2000000))
    
    inp1 = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08"\
            "49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00"\
            "81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65"\
            "52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91"\
            "22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80"\
            "24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50"\
            "32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70"\
            "67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21"\
            "24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72"\
            "21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95"\
            "78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92"\
            "16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57"\
            "86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58"\
            "19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40"\
            "04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66"\
            "88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69"\
            "04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36"\
            "20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16"\
            "20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54"\
            "01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"
            
    #print(grid_product(inp1))
    #print(longest_collatz(1000000))
    #print(sum_factorial(100))
    #print(fibonacci_iter())
    #print(digit_fact())
    
    inp2 = "37107287533902102798797998220837590246510135740250"\
"46376937677490009712648124896970078050417018260538"\
"74324986199524741059474233309513058123726617309629"\
"91942213363574161572522430563301811072406154908250"\
"23067588207539346171171980310421047513778063246676"\
"89261670696623633820136378418383684178734361726757"\
"28112879812849979408065481931592621691275889832738"\
"44274228917432520321923589422876796487670272189318"\
"47451445736001306439091167216856844588711603153276"\
"70386486105843025439939619828917593665686757934951"\
"62176457141856560629502157223196586755079324193331"\
"64906352462741904929101432445813822663347944758178"\
"92575867718337217661963751590579239728245598838407"\
"58203565325359399008402633568948830189458628227828"\
"80181199384826282014278194139940567587151170094390"\
"35398664372827112653829987240784473053190104293586"\
"86515506006295864861532075273371959191420517255829"\
"71693888707715466499115593487603532921714970056938"\
"54370070576826684624621495650076471787294438377604"\
"53282654108756828443191190634694037855217779295145"\
"36123272525000296071075082563815656710885258350721"\
"45876576172410976447339110607218265236877223636045"\
"17423706905851860660448207621209813287860733969412"\
"81142660418086830619328460811191061556940512689692"\
"51934325451728388641918047049293215058642563049483"\
"62467221648435076201727918039944693004732956340691"\
"15732444386908125794514089057706229429197107928209"\
"55037687525678773091862540744969844508330393682126"\
"18336384825330154686196124348767681297534375946515"\
"80386287592878490201521685554828717201219257766954"\
"78182833757993103614740356856449095527097864797581"\
"16726320100436897842553539920931837441497806860984"\
"48403098129077791799088218795327364475675590848030"\
"87086987551392711854517078544161852424320693150332"\
"59959406895756536782107074926966537676326235447210"\
"69793950679652694742597709739166693763042633987085"\
"41052684708299085211399427365734116182760315001271"\
"65378607361501080857009149939512557028198746004375"\
"35829035317434717326932123578154982629742552737307"\
"94953759765105305946966067683156574377167401875275"\
"88902802571733229619176668713819931811048770190271"\
"25267680276078003013678680992525463401061632866526"\
"36270218540497705585629946580636237993140746255962"\
"24074486908231174977792365466257246923322810917141"\
"91430288197103288597806669760892938638285025333403"\
"34413065578016127815921815005561868836468420090470"\
"23053081172816430487623791969842487255036638784583"\
"11487696932154902810424020138335124462181441773470"\
"63783299490636259666498587618221225225512486764533"\
"67720186971698544312419572409913959008952310058822"\
"95548255300263520781532296796249481641953868218774"\
"76085327132285723110424803456124867697064507995236"\
"37774242535411291684276865538926205024910326572967"\
"23701913275725675285653248258265463092207058596522"\
"29798860272258331913126375147341994889534765745501"\
"18495701454879288984856827726077713721403798879715"\
"38298203783031473527721580348144513491373226651381"\
"34829543829199918180278916522431027392251122869539"\
"40957953066405232632538044100059654939159879593635"\
"29746152185502371307642255121183693803580388584903"\
"41698116222072977186158236678424689157993532961922"\
"62467957194401269043877107275048102390895523597457"\
"23189706772547915061505504953922979530901129967519"\
"86188088225875314529584099251203829009407770775672"\
"11306739708304724483816533873502340845647058077308"\
"82959174767140363198008187129011875491310547126581"\
"97623331044818386269515456334926366572897563400500"\
"42846280183517070527831839425882145521227251250327"\
"55121603546981200581762165212827652751691296897789"\
"32238195734329339946437501907836945765883352399886"\
"75506164965184775180738168837861091527357929701337"\
"62177842752192623401942399639168044983993173312731"\
"32924185707147349566916674687634660915035914677504"\
"99518671430235219628894890102423325116913619626622"\
"73267460800591547471830798392868535206946944540724"\
"76841822524674417161514036427982273348055556214818"\
"97142617910342598647204516893989422179826088076852"\
"87783646182799346313767754307809363333018982642090"\
"10848802521674670883215120185883543223812876952786"\
"71329612474782464538636993009049310363619763878039"\
"62184073572399794223406235393808339651327408011116"\
"66627891981488087797941876876144230030984490851411"\
"60661826293682836764744779239180335110989069790714"\
"85786944089552990653640447425576083659976645795096"\
"66024396409905389607120198219976047599490197230297"\
"64913982680032973156037120041377903785566085089252"\
"16730939319872750275468906903707539413042652315011"\
"94809377245048795150954100921645863754710598436791"\
"78639167021187492431995700641917969777599028300699"\
"15368713711936614952811305876380278410754449733078"\
"40789923115535562561142322423255033685442488917353"\
"44889911501440648020369068063960672322193204149535"\
"41503128880339536053299340368006977710650566631954"\
"81234880673210146739058568557934581403627822703280"\
"82616570773948327592232845941706525094512325230608"\
"22918802058777319719839450180888072429661980811197"\
"77158542502016545090413245809786882778948721859617"\
"72107838435069186155435662884062257473692284509516"\
"20849603980134001723930671666823555245252804609722"\
"53503534226472524250874054075591789781264330331690"

#print(large_sum(inp2))
#print(name_scores())
#print(triangle_factors())
#print(dbase_palindrome())
#print(truncatable_primes())
#print(self_powers())
#print(number_permutations('0123456789'))
#print(dig_fifth_powers())
#print(distinct_powers())
#print(sub_str_div())
#print(champ_constant())
#print(counting_sundays())
#print(permuted_multiples())
#print(integ_right())
#print(comb_selectors())
#print(triangle_nums())
#print(get_prime_factors())
#print((pandig_prime()))
#print(consec_primes())
#print(pand_multiples())
#print(recip_cycles())
#print(amicable_numbers())
#print(lychrel_nums())
#print(pow_digit_sum())
#print(frac_sqrt_conv())
#print(shapes_nums())
#print(abundant_sums())
#print(pent_sum())
#print(num_letter())
