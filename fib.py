fibs = [0, 1, ]
a = b = 1

min = int(input('enter the minimum:'))
max = int(input('enter the maximum:'))

for _ in range(max):
    a, b = b, b + a
    fibs.append(a)

for x in fibs:
    if min <= x <= max:
        print(x)
