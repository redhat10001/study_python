import math

#from icecream import ic
#ic.configureOutput(prefix='Debug | ')

a, b = 1, 2
print(a, b)

a, b = b, a
print(a, b)

# определоение типа данных type & id
x = 6.8
y = 'Hello'
print(id(x), id(y))
print('---------------')
print(type(x), type(y))

type = 7
# ic(type)

# действия над числами
a = 5 + 1/2
b = 3 + 2.0
c = 3 + 2
d = 4 + 8/2
print(a, b, c, d)

# деление с округлением к найменьшему целому
a = 7 // 2
b = 7 // -2
print(a, b, c)
# остаток
c = 10 % 3
d = 10 % -4
e = -9 % 5
e2 = 9 % -5
e3 = -9 % -5
print('остаток', c, d, e, e2, e3)

# возведение в степень
a = 2 ** 2
b = 2 ** 3
c = 36 ** 0.5
d = 2 ** 3 ** 2
e = 27 ** 1/3
e2 = 27 ** (1/3)
print(a, b, c, d, e, e2)

# математические функции
d = abs(-5)
print('модуль числа abs(-5): ', d)
print('минимальное число min(1, 2, 3, 4, 5): ', min(1, 2, 3, 4, 5))
print('максимальное число max(1, 2, 3, 4, 5): ', max(1, 2, 3, 4, 5))
print('возведение в степень pow(6, 2) : ', pow(6, 2))
print('округление к ближайшему целому round(1.3) : ', round(1.3))
print('округление с указанной точностью round(7.83695, 2) : ', round(7.83695, 2))
print('округление с указанной точностью round(7.83695, -1) : ', round(7.83695, -1))
print('округление с указанной точностью round(783.695, -2) : ', round(783.695, -2))
print('округление с указанной точностью round(783.695, -1) : ', round(783.695, -1))

# вызов математической функции из фуекции
print('максимальное число max(1, 2, abs(-10), 4, 5): ', max(1, 2, abs(-10), 4, 5))
print('максимальное число max(1, 2, abs(min(11, 12, -13)), 4, 5): ', max(1, 2, abs(min(11, 12, -13)), 4, 5))

print('округление до большего целого math.ceil(4.2): ', math.ceil(4.2))
print('округление до большего целого math.ceil(-4.2): ', math.ceil(-4.2))

print('округление до наименеьшего целого math.floor(4.2): ', math.floor(4.2))
print('округление до наименьшего целого math.floor(-4.2): ', math.floor(-4.2))

print('факториал числа math.factorial(6) - 1*2*3*4*5*6: ', math.factorial(6))

print('отбрасывание дробной части math.trunc(-4.256): ', math.trunc(-4.256))

print('вычисление логарифма math.log2(4): ', math.log2(4))
print('вычисление логарифма math.log10(1000): ', math.log10(1000))
print('вычисление логарифма math.log(2.7): ', math.log(2.7))
print('вычисление логарифма math.log(27, 3): ', math.log(27, 3))

print('вычисление корня math.sqrt(49): ', math.sqrt(49))

print('константа пи math.pi): ', math.pi)
print('константа е math.e: ', math.e)

