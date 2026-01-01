# print(' Hello','Kaniet', sep='bdfj, ')
# print('first row',end=' ')
# print('second row')
# input('Please enter something')

#////////

# name = input('Enter your name: ')
# age = input('Enter your age: ')

# print('Hello',name)
# print('Your are', age,'years old')

#/////// int str

# name = 'Kaniet'
# city = 'Karakol'
# age = input('enter age: ')
# # age = int(input('enter age: '))   #always <class 'int'> 
# year = 2025

# print(type(name))   # <class 'str'>  cтрока (текст)
# print(type(year))   # <class 'int'>  значение числа
# print(type(age))    #always <class 'str'> because input

#/////// if elif else

# age = int(input('enter your age: '))
# if age < 0:
#     print('invalid age')
# elif age < 18:
#     print('you are minor')
# elif age < 65:
#     print('you are an adult')
# else:
#     print('you are a senior')

#////// mini progect

# print(' ===mini questionnaire===')

# name = input('enter your name: ')
# age = int(input('enter your age: '))
# city = input('enter your city: ')

# print('===result===')

# print('name: ',name)
# print('age: ',age)
# print('city: ',city)

# if age < 18:
#     print('status: Minor')
# elif age < 65:
#     print('status: Adult')
# else:
#     print('status: Senior')

#///// mini progect from calculator for massa

print('===massa/molar/atom massa===')

m = float(input('enter yout massa: '))
n = float(input('enter yout molar: '))
M = float(input('enter yout atom massa: '))
C = float(input("enter your konsantrasyon: "))
V_ml = float(input("enter your volum: "))

print('===result===')

print('massa: ',m)
print('enter your molar: ',n)
print('enter your atom massa: ',M)
print('enter your atom volum: ',V_ml)
print('enter your atom konsantrasyon: ',C)


if m > 0 and M > 0 and n == 0:
    n = m / M
    print('n = ',n)
elif n > 0 and M > 0 and m == 0:
    print('m = ',n * M, 'g')

V = V_ml / 1000
if C == 0 and n > 0 and V > 0:
    print('C = ',n / V, 'mol/lt')
elif C > 0 and n > 0 and V == 0:
    print('V = ',n / C, 'lt')
elif C > 0 and V > 0 and n == 0:
    print('n = ',C * V, 'mol')

if V_ml == 0 and n > 0 and C > 0:
    print('error ziroo')
#////////   переменная

# переменная в пайтон - это контейнер,для хранения значения. Может быть числом,текстом или более сложными типами данных.

# name, age = 'Kaniet', 19
# print(name, age)

# other_name = name
# print(other_name)

# x = 3
# y = 4

# x, y = y, x
# print(x, y)

# variable = 0.5
# print(type(variable))

# snake_case - имена переменных,функций,методов модулей
# CamelCase - имена классов 
# yet-another-package - название пакетов
# CONSTANT - константы
# integer int
# + сложение, - вычитание, * умножение, / деление , ** возведение в степень , % остаток от деления , // целочисленное деление
# 9 / 4 = 2 * 4 + 1  2 - это по целочисленному делению // , 1 - это остаток от деления %


# //////трудная задачка

# number_flat = int(input('enter your apartment: '))

# print(' ===result=== ')

# number_entrance = (number_flat - 1) // 20 + 1
# number_room = (number_flat - 1) % 20 // 4 + 1
# print('Entrance: ',number_entrance)
# print('Flat: ',number_room)

# == равно , != не равно , >= больше либо равно , <= меньше либо равно , < больше , > меньше