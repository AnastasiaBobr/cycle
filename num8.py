n =input('Введите число:')
 
Sum = 0
Umn = 1
 
for i in n:
    Sum += int(i)
    Umn *= int(i)
 
print (f'Сумма:{Sum}')
print (f'Произведение:{Umn}')