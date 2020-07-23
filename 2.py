fibs = [0, 1, ]
a = b = 1

num = int(input('Введіть вашу оцінку:'))

for _ in range(30):
    a, b = b, b + a
    fibs.append(a)

if num in fibs:
    print('Ваша оцінка є числом Фібоначчі')
else:
    print('Ваша оцінка не є числом Фібоначчі')
