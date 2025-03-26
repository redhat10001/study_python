# функции print & input
a = -6.84
b = 7
c = 25.6
print(a, b, c, sep=' | ')

print('Hello', 'World', end=' ')
print()
x = -5.76
y = 8.0
print(f'Координаты точки х = {x} ; y = {y}')
#print()
#a = input()
#print(a, type(a))

#print()
#a = int(input())
#b = abs(a)
#print(b)

#print()
#a = float(input())
#b = abs(a)
#print(b)

#print()
#a = float(input('Введите длину прямоугольника: '))
#b = float(input('Введите ширину прямоугольника: '))
#print('Периметр: ', format(2 * (a + b), '.1f'))

#print()
#a, b = map(float, input('Введите стороны прямоугольника: ').split())
#print('Периметр: ', format(2 * (a + b), '.1f'))

print()
a, b, c = map(int, input('Введите стороны треугольника: ').split())
print('Периметр: ', a + b + c)