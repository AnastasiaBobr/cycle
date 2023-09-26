n = int(input('Введите число:'))
i = []

if n < 0:
    print('ошибка')
else:
    while n != 0:
        i.append(n % 10)
        n = n // 10

i.reverse()
print(i)