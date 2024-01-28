"""Perfect numbers
Perfect numbers are positive integers that equal the sum of its proper positive divisors.
Example: 6 = 1 + 2 + 3
"""

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    sum_of_divisors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_of_divisors += i
    if sum_of_divisors == number:
        return "perfect"
    if sum_of_divisors > number:
        return "abundant"
    return "deficient"
    
print(classify(6))
print(classify(35))