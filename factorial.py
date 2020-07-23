mass = []

try:
    minimum = int(input('Мінінмум:'))
    maximum = int(input('Максимум:'))
    step = int(input('Крок:'))
    if minimum <= maximum:
        for i in range(minimum, maximum + 1, step):
            mass.append(i)
    else:
        mass = None
        print('Мінімум більший за максимум')
except ValueError:
    maximum = None
    print('Введено некоректні дані')


def factorial(l):
    if l:
        k = l[0]
        for x in l:
            k *= x
        return int(k/l[0])


if __name__ == '__main__':
    if mass:
        fact = factorial(mass)
        print(f'Факторіал діапазону з {minimum} по {maximum} з кроком {step} = {fact}')

print(mass)