a = float(input('Введите первое число: ').replace(',', '.'))
b = float(input('Введите второе число: ').replace(',', '.'))

s = a + b
avg = (a + b) / 2

print('sum=', round(s, 2), '; avg=', round(avg, 2))