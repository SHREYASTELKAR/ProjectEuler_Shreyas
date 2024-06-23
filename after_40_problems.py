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

if __name__ == "__main__":
    #print(digit_cancelling_fractions())
    #print(nth_power())
    pass
