
# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
            print(number)
        if number % 3 == 0:
            print("Fizz")
            print(number)
        if number % 5 == 0:
            print("Buzz")
            print(number)
        else:
            print(number)


fizz_buzz(100)