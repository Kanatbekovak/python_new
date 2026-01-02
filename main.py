# print(' Hello','Kaniet', sep='bdfj, ')
# print('first row',end=' ')
# print('second row')
# input('Please enter something')

#////////////////////////////////////////////////////////

# name = input('Enter your name: ')
# age = input('Enter your age: ')

# print('Hello',name)
# print('Your are', age,'years old')

#/////// int str  ////////////////////////////////////

# name = 'Kaniet'
# city = 'Karakol'
# age = input('enter age: ')
# # age = int(input('enter age: '))   #always <class 'int'> 
# year = 2025

# print(type(name))   # <class 'str'>  cтрока (текст)
# print(type(year))   # <class 'int'>  значение числа
# print(type(age))    #always <class 'str'> because input

#/////// if elif else  //////////////////////////////////

# age = int(input('enter your age: '))
# if age < 0:
#     print('invalid age')
# elif age < 18:
#     print('you are minor')
# elif age < 65:
#     print('you are an adult')
# else:
#     print('you are a senior')

#////// mini progect  ///////////////////////////////////

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

#///// mini progect from calculator for massa ///////////////////

# print('===massa/molar/atom massa===')

# m = float(input('enter yout massa: '))
# n = float(input('enter yout molar: '))
# M = float(input('enter yout atom massa: '))
# C = float(input("enter your konsantrasyon: "))
# V_ml = float(input("enter your volum: "))

# print('===result===')

# print('massa: ',m)
# print('enter your molar: ',n)
# print('enter your atom massa: ',M)
# print('enter your atom volum: ',V_ml)
# print('enter your atom konsantrasyon: ',C)


# if m > 0 and M > 0 and n == 0:
#     n = m / M
#     print('n = ',n)
# elif n > 0 and M > 0 and m == 0:
#     print('m = ',n * M, 'g')

# V = V_ml / 1000
# if C == 0 and n > 0 and V > 0:
#     print('C = ',n / V, 'mol/lt')
# elif C > 0 and n > 0 and V == 0:
#     print('V = ',n / C, 'lt')
# elif C > 0 and V > 0 and n == 0:
#     print('n = ',C * V, 'mol')

# if V_ml == 0 and n > 0 and C > 0:
#     print('error ziroo')


#////////   переменная  ////////////////////////////////

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

 
# //////трудная задачка  ///////////////////////////////

# number_flat = int(input('enter your apartment: '))

# print(' ===result=== ')

# number_entrance = (number_flat - 1) // 20 + 1
# number_room = (number_flat - 1) % 20 // 4 + 1
# print('Entrance: ',number_entrance)
# print('Flat: ',number_room)

# == равно , != не равно , >= больше либо равно , <= меньше либо равно , < больше , > меньше


#///// Булевой тип(bool)  //////////////////////////////

# x = 10
# y = 10
# eq = x != y
# print(eq)
# print(x > y)
# print(x < y)
# print(x >= y)
# print(x <= y)
# print(x < 11 and x > 1)   # операторы and or not
# a = True 
# print(not a)

# print(bool(-1)) # -1 True
# print(bool(0)) # 0 False
# print(bool(1)) # 1 True 
# print(bool("Hello")) # True
# print(bool("")) # False

#////// задание "Анализатор pH"  //////////////////////////////////

# water = 7.5
# tomato = 3.7
# ammonia = 11.2

# matter = input("enter your matter: ")
# number = float(input("enter your number matter: "))

# if number >= 0 and number < 3:   # 0 <= number < 3
#     print(matter, " = ", number, " - ", 'acidic')
# elif number >= 3 and number < 11:
#     print(matter, " = ", number, " - ", 'neutral')
# elif number >= 11 and number <= 14:
#     print(matter, " = ", number, " - ", 'alkaline')
# |
# |
# |
# ↓

# substances = {
#     'water': 7.5,
#     'tomato': 3.7,
#     'ammonia': 11.2
# }

# for name, ph in substances.items():
#     if 0 <= ph < 3:
#         status = "strong acidic"
#         print(f"{name}: pH {ph} - it is {status}")
#     elif 3 <= ph < 7:
#         status = "acidic/neutral"
#         print(f"{name}: pH {ph} - it is {status}")
#     elif 7 <= ph <= 8:
#         status = "neutral"
#         print(f"{name}: pH {ph} - it is {status}")
#     elif 8 < ph <= 11:
#         status = "weak alkaline"
#         print(f"{name}: pH {ph} - it is {status}")
#     elif 11 < ph <= 14:
#         status = "alkaline"
#         print(f"{name}: pH {ph} - it is {status}")
#     else: 
#         status = "invalid ph"
#         print(f"{name}: pH {ph} - it is {status}")

# print(f"{name}: pH {ph} - it is {status}") только один

#////////// високосный год ///////////////////////////

# year = 2000

# if year % 4 == 0 and year % 100 != 0:  # if not year % 4 and year % 100:
#     print("year is leap")
# elif year % 400 == 0:             #elif not year % 400:
#     print("year is leap")
# else:
#     print("year is not leap")


# встроенная функция при расчета длины
# lenght = len("8787")
# print(lenght)
# print(len(""))

# big_integer = 2 ** 1000
# print(len(str(big_integer)))

# my_string = "hello, world"
# print("hello" in my_string)

# my_string ="     alice world"
# print(my_string.upper())  # ALICE WORLD
# print(my_string.lower())  #alice world
# print(len(my_string))
# print(len(my_string.strip()))
# print(my_string.replace("world", "Python"))
# print(my_string.count("l"))

# integer = input("enter your number: ")
# if integer.isdigit():     # isdigit() метод принимает только числа true false
#     integer = int(integer)

# print(type(integer))

# name = "Kaniet"
# age = 19
# print(f"Hello, my name is {name} and I am {age} years old")

# x = 10
# y = 5
# print(f"summary is {x + y}, multiplication is {x * y}")

# my_string = input("enter your number: ")

# if my_string.isdigit():
#     my_integer = int(my_string)
#     print(my_integer)
# else:
#     print(f"{my_string} is not a number")

# ///////// format() оператор форматирования(или интерполяции) //////////////////

# print("Mr. %s, the total is %.2f." % ("Jekyll", 15.53))  # %s является заполнителем для строк , %f для чисел с плавающей запятой (числа перед f означает сколько хотим показать)

# print("The character after %c is %c." % ("B", "C"))  # %c один символ

# place = "New York"
# print("Welcome to %s" % place)

# year = 2019
# print("%i will be a perfect year." % year)  # %i or %d десятичное целое число
# # %u беззнаковое десятичное целое число
# number = 15
# print("%i in octal is %o" % (number, number))  # %o восьмеричное целое число

# number = 15
# print("%i in hex is %02x" % (number, number))  # %x шестнадцатеричное целое число с использованием строчных букв (af)

# number = 15
# print("%i in hex is %04X" % (number, number))  # %X шестнадцатеричное целое число с использованием строчных букв (af)


#///// списки(list) ////////////////////////////////////

# fruits = ["apple", "banana", "cherry"]  # инты, флаты,бул
# print(len(fruits))
# print("banana" in fruits)
# fruits.append("watermelon")
# print(fruits)

# element1 = "apple"
# element2 = "banana"
# elemnet3 = "cherry"
# fruits = [element1, element2, elemnet3]
# print(fruits)

# print(bool([]))  # false
# print(bool([0]))   # true

# word = "hello"
# my_list = list(word)
# print(my_list)

# my_string = "hello world"
# new = my_string.replace("world", "Python")
# print(new)
# print(my_string)

# fruits = ["apple", "banana", "cherry"]
# fruit = fruits.pop()
# print(fruit)
# print(fruits)

# fruits = ["apple", "banana", "cherry"]
# fruits2 = ["fig", "grape"]

# fruits.extend(fruits2)
# print(fruits)

# fruits = ["apple", "banana", "cherry"]
# fruits.reverse()
# print(fruits)

# my_list = [ 3, 5, 6, 7, 8, 10]
# my_list.sort(reverse=True)
# print(my_list)

# my_string = "my name is Kaniet"
# my_list = my_string.split(" ")
# print(my_list)

# new = " ".join(my_list)
# print(new)

# my_list = [1, 4, 7, 45, 4, 9, 34, 57, 986]
# print(min(my_list))
# print(max(my_list))
# print(sum(my_list))

# ////// индексы и слайсы //////////////////////////////

# fruits = ["apple", "banana", "cherry", "watermelon"]
# print(fruits[0]) # 0 1 2 3 
# print(fruits[-4])  # -4 -3 -2 -1 
# print(fruits[-3])

# fruits[0] = "pineapple"
# print(fruits)

# fruits[0],fruits[3] = fruits[3],fruits[0]
# print(fruits)

# слайс это всегда полуоткрытый интревал 
# numbers = [0,1, 2, 3, 4,5]
# numbers[0:3]  => [0,1,2] 

# number = [0, 1, 2, 3, 4, 5,6 ,7, 8, 9]
# new = number[0:5]  new = number[0:len(numbers)]   new = number[0:10:2] четные (::2)
# print(new)


#/////// цикл for //////////////////////////////////////

# file_names = ["txt", "jpg", "pdf"]

# for file_name in file_names:
#     print(file_name)

greeting = "Hello, world"
count_o = 0
for char in greeting:
    if char == "o":
        count_o += 1
        print(char)

print(count_o)

# caхар для питона 

# count = count + 1 
# count += 1

# count = count - 1
# count -= 1

# count = count * 2
# count *= 2

# students = ["Alice", "Kaniet", "Nurcigit"]

# for student in students:
#     print(student)
#     for char in student:
#         print(char)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for number in numbers:
    if number % 2 == 0:
        continue
    print(number)
    if number == 10:
        break
    print(number)