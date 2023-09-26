n = int(input('Введите число:'))
x = 0
if n > 0:
        for i in str(n):
            if int(i) % 2 == 0:
                x += int(i)
        print(x)
else:
        print('error')