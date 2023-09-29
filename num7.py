n = int(input('Введите число:'))
x = 0
while n>0:
    
    if n % 2 == 0:
        x += n % 10
    n //= 10
    

print(n)
