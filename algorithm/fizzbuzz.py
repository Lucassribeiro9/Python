# multiple 3 and 5

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

for number in numbers:
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)