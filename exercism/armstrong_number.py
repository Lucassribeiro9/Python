"""
Instructions
An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.

For example:

9 is an Armstrong number, because 9 = 9^1 = 9
10 is not an Armstrong number, because 10 != 1^2 + 0^2 = 1
153 is an Armstrong number, because: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
154 is not an Armstrong number, because: 154 != 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190
Write some code to determine whether a number is an Armstrong number.
"""

def is_armstrong_number(number):
    """
    Check if the given number is an Armstrong number.

    :param number: int, the number to be checked
    :return: bool, True if the number is an Armstrong number, False otherwise
    """
    if number == sum(int(digit) ** len(str(number)) for digit in str(number)):
        print("Is Armstrong number")
        return True
    else:
        print("Not Armstrong number")
        return False

print(is_armstrong_number(50))