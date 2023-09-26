x=int(input('Введите число:'))
y=int(input('Введите степень:'))
n=1

if y>0:
  for i in range(y+1):
    if i==0:
      continue
     
    n*=x
  print(n)