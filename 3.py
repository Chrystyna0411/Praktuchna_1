import random

value = random.randint(1, 10)


try:
    while True:
        num = int(input('enter your number'))
        if num == value:
            print('Good job, you guessed the number')
            break
        elif num < value:
            print('number is too small, try again')
        else:
            print('number is too big, try again')

except ValueError:
    num = None
    print('incorrect input, try again')
