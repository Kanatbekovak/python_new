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

# number_entrance = (number_flat - 1) // 20
# number_room = (number_flat) % 20 // 4 
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

# greeting = "Hello, world"
# count_o = 0
# for char in greeting:
#     if char == "o":
#         count_o += 1
#         print(char)

# print(count_o)

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

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# for number in numbers:
#     if number % 2 == 0:
#         continue
#     print(number)
#     if number == 10:
#         break
#     print(number)

#//////////////////////////////////////////////////////////////

# matter = ["ammonia", "benzen", "tolen", "alkan", "sulfurik asit"]
# matter2 = ["sodyum hidroksit"]
# matter.extend(matter2) # добавить
# print(matter)
# old_stuff = ["ammonia", "benzen","tolen", "alkan", "sulfurik asit"]
# for item in old_stuff:
#     if item in matter:
#         matter.remove(item)
# print(matter)


# def add_unique_items(main_list, new_items):
#     for item in new_items:
#         if item not in main_list: # Проверка на уникальность
#             main_list.append(item)
#     return main_list


# # Применяем для ХИМИИ
# matter = ["ammonia", "benzen"]
# new_chem = ["benzen", "tolen", "alkan"] # Benzen уже есть!
# matter = add_unique_items(matter, new_chem)

# print(matter) 
# # Результат: ['ammonia', 'benzen', 'tolen', 'alkan'] 
# # (Второй benzen не добавился, и это правильно!)


# # Создаем инструмент
# def clean_my_list(main_list, items_to_remove):
#     for item in items_to_remove:
#         if item in main_list:
#             main_list.remove(item)
#     return main_list


# # Теперь используем его для ХИМИИ
# matter = ["ammonia", "benzen", "tolen", "alkan", "sulfurik asit", "sodyum hidroksit"]
# old_chem = ["ammonia", "benzen"]
# matter = clean_my_list(matter, old_chem)
# print(f"Химия после чистки: {matter}")

# # Теперь этот же код для НЕДВИЖИМОСТИ (ID квартир)
# apartments_ids = [1, 2, 3, 4, 5]
# sold_ids = [1, 3]
# apartments_ids = clean_my_list(apartments_ids, sold_ids)
# print(f"Доступные квартиры: {apartments_ids}")


# def add_list(list,new_list):
#     for item in new_list:
#         if item not in list:
#             list.append(item)
#     return list

# matter = ["ammonia", "benzen", "tolen", "alkan", "sulfurik asit"]
# matter2 = ["sodyum hidroksit", "hidrojen"]

# matter = add_list(matter, matter2)
# print(matter)

# def delete_list(list_del,old_list):
#     for item in list_del[:]:
#         if item not in old_list:
#             list_del.remove(item)
#     return list_del

# matter = delete_list(matter, matter2)
# print(matter)

# def find_list(list):
#     asit_list = []
#     for item in list:
#         if "asit" in item:
#             asit_list.append(item)
#     if len(asit_list) > 0:
#         return asit_list
#     else:
#         return "not asit"


# matter = find_list(matter)
# print(f"Найденные кислоты: {matter}")

# print(my_string.upper())  # ALICE WORLD
# print(my_string.lower())  #alice world

# account = "kanatbekova kaniet"
# print(account.title())  # upper(),capitalize(),upper(),title()
# print(account.count("a"))
# print(account.find("i"))

# //////////////////////////////////////////////////////////////////////

# age = 20
# name = 'Swaroop'

# print('{0} was {1} years old when he wrote this book'.format(name, age))
# print('Why is {0} playing with that python?'.format(name))

# print("I am {0} and I am {1} years old".format(name, age))

# # print('{name} was {age} years old when he wrote this book'.format(name=name, age=age))
# # print('Why is {name} playing with that python?'.format(name=name))

# print('{0:.3f}'.format(25.5/5))


# ///////////////////////////  функции  ///////////////////////////////////////////

# def count_vowels(string):
#     VOWELS = "aeiouAEIOU"
#     count = 0
#     for char in string:
#         if char in VOWELS:
#             count += 1
            
#     return count

# print(count_vowels("Hello World"))
# enter_text = input("enter your text:")
# word = count_vowels(enter_text)
# print(word)


# def info():
#     pass #заглушки для функции чтобы они временно не работали

# info()


# def format_date(day: int, month: str):
#     return f"The date is {day} of {month}"

# print(format_date(15, "May"))
# print(format_date("May", 12))
# print(format_date(day=15,month="June"))
# print(format_date(month="June",day=15))


# def custom_greeting(*, name: str, greeting: str = "Hello") -> str:
#     return f'{greeting}, {name}'

# print(custom_greeting(name="Kaniet", greeting="Good morning"))
# print(custom_greeting(name="Kaniet"))


# comfortable_temperature = 25

# def get_diff_from_comfortable_tem(*,temperature: int) -> int:
#     return comfortable_temperature - temperature

# print(get_diff_from_comfortable_tem(temperature=20))


# defaul_level_experience = 200

# def is_level_up(*, current: int, gained: int) -> int:
#     total = current + gained
#     level_up = False

#     if total >= defaul_level_experience:
#         level_up = True
    
#     return level_up

# print(is_level_up(current=150,gained=60))  #True
# print(is_level_up(current=10,gained=60))  #False


# ///////////////////////////  цикл while  ///////////////////////////////////////////

# цикл for повторяется определенное количество раз (чащу всего количество его итерации равно количество коллекции которые мы перебираем)

# цикл while может повторятся неопределенное количество раз (это цикл который используется по условию)

# counter = 1

# while counter <= 5:
#     print(f"Counter is {counter}")
#     counter += 1


# my_list = [0, 1, 2]

# while my_list:
#     element = my_list.pop()
#     print(f"element: {element}")

# print(my_list)


# while True:
#     print("hi")  #бусконечный цикл

# while True:
#     answer = input("enter a number:")
#     if answer == "quit":
#         break
#     print("you entered: {answer}")


import random 

HEADS = "heads"
TAILS = "tails"

COIN_VALUES = [HEADS,TAILS]

def flip_coin():
    return random.choice(COIN_VALUES)

print(flip_coin())

def play_martingale(*, start: int, min_ber: int,max_bet: int) ->int:
    steps_to_loose = 0
    current_funds = start
    current_bet = min_ber

    while current_funds > 0:
        # print("============")
        steps_to_loose += 1
        current_funds -=current_bet
        # print(f"{current_funds=}, {current_bet=}")
        flipped_coin_value = flip_coin()
        if flipped_coin_value == HEADS:
            win = current_bet * 2
            # print(f"{win=}")
            current_funds += win
            current_bet = min_ber
        else:
            # print("loose")
            current_bet *= 2
            if current_bet > max_bet:
                current_bet = min_ber
            if current_bet > current_funds:
                current_bet = current_funds

    return steps_to_loose

# print(play_martingale(start=100,min_ber=1,max_bet=100))
def simulate_martingale_for_n_players(*,start:int,min_ber:int,max_bet:int,n_games) -> float:
    total_steps_to_loose = 0
    for i in range(n_games):
        steps_to_loose =play_martingale(start=start,min_ber=min_ber,max_bet=max_bet)
        total_steps_to_loose += steps_to_loose


    return total_steps_to_loose / n_games

print(simulate_martingale_for_n_players(
    n_games=10,
    start=1000,
    min_ber=1,
    max_bet=100
))