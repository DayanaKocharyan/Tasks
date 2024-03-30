# task 1
# print(f'My name is Dayana\nMy email adress: dayanakocaryan@gmail.com')
# --------------------------------------------
# task 2
# name = input("What is your name?")
# print(f'Hello {name}')
# --------------------------------------------
# task 3
# length = float(input("Write the length of the room: "))
# width = float(input("Write the width of the room: "))
# surface = length * width
# print(f'The surface of the room is {surface} meter')
# --------------------------------------------
# task 4
# length = float(input("Write the length of the park in feet: "))
# width = float(input("Write the width of the park in feet: "))
# surface = length * width / 43560
# print(f'The surface of the room is {surface} acres')
# --------------------------------------------
# task 5
# less = int(input("Hello!\nHow many bottles less than one liter would you like to give? "))
# more = int(input("Okay, and how many bottles more than one liter would you like to give? "))
# money = float((less * 0.1) + (more * 0.25))
# print("%.2f" %money,'$')
# --------------------------------------------
# task 6
# order = float(input('Write the amount of the order: '))
# tips = order * 18 / 100
# taxes = order * 7 / 100
# sum = order + tips + taxes
# print(f'order->{order}\ntips->{tips}\ntaxes->{taxes}\nThe sum of order is {"%.2f" %sum}$')
# --------------------------------------------
# task 7
# n = int(input('Write the number: '))
# sum = (n * (n + 1)) / 2
# print(f'The sum of natural positive numbers from 1 to {n} is {sum}')
# --------------------------------------------
# task 8
# souvenirs = int(input("Hello, how many souvenirs do you have? "))
# trinkets = int(input("Okay, and how many trinkets do you have? "))
# weight = int((souvenirs * 75) + (trinkets * 112))
# print(f'Total wight is {weight}g')
# --------------------------------------------
# task 9
# money = float(input("Write the sum of money you want give: "))
# first =round((money + money * 0.04),2)
# second = round((first + first * 0.04),2)
# third = round((second + second * 0.04),2)
# print(f'first year->{"%.2f"%first}\nsecond year->{"%.2f"%second}\nthird year->{"%.2f"%third}')
# --------------------------------------------
# task 10
# a = int(input('Write first whole number: '))
# b = int(input('Write second whole number: '))
# import math
# print(f'Gumar->{a + b}\nTarberutyun->{a - b}\nArtadryal->{a * b}\
#       \nAmboxj masov bajanum->{a // b}\nBajanumic stacvac mnacord->{a % b}\
#       \n{a} tvi 10 himqov logaritm->{math.log10(a)}\n{a} tvi {b} astichan->{a ** b}')
# --------------------------------------------
# task 11
# mpg = float(input('Write how many miles-per-gallon you have: '))
# kml = mpg * 0.425144
# print(f'{mpg}mpg->{kml}km/l')
# --------------------------------------------
# task 12
# import math
# x = float(input('enter 1st degree: '))
# y = float(input('now enter 2nd degree: '))
# a = float(input('enter 3rd degree: '))
# b = float(input('now enter 4rd degree: '))
# t1 = math.radians(x)
# t2 = math.radians(y)
# g1 = math.radians(a)
# g2 = math.radians(b)
# distance = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1-g2))
# print(distance)
# --------------------------------------------
# task 13
# n = int(input('How much change should I give you: '))
# cent_25 = n // 25
# n = n - cent_25 * 25
# cent_10 = n // 10
# n = n - cent_10 * 10
# cent_5 = n // 5
# n = n - cent_5 * 5
# cent_1 = n
# print(f'25->{cent_25}\n10->{cent_10}\n5->{cent_5}\n1->{cent_1}')
# --------------------------------------------
# task 14
# feet = int(input('Enter the number of feet in your height: '))
# inch = int(input('Enter the number of inches in your height: '))
# inch += feet * 12
# print(f'{inch * 2.54}cm')
# --------------------------------------------
# task 15
# feet = float(input('Enter the distance in feet: '))
# inch = feet * 12
# yard = feet * 3
# mile = feet * 5280
# print(f'inch->{inch}\nyard->{yard}\nmile->{mile}')
# --------------------------------------------
# task 16
# import math
# r = float(input('enter the radius of circle: '))
# s = 2 * math.pi * r
# S = 3/4 * math.pi * (r ** 3)
# print(f'The area of circle is {s}\nThe area of circle sphere is {S}')
# --------------------------------------------
# task 17
# m = float(input('Write the weight of water in grams: '))
# T = float(input('Write the temperature difference: '))
# q = m * T * 4.186
# c = round(8.9 * (q/3600000),2)
# print(f'The total amount -> {q}\ncost -> {c}')
# --------------------------------------------
# task 18
# import math
# r = float(input('Enter the radius of the cylinder: '))
# h = float(input('Enter the height of the cylinder: '))
# v = math.pi * (r ** 2) * h
# print(f'The volume of cylinder is {round(v,1)}')
# --------------------------------------------
# task 19
# import math
# h = float(input('Enter the height in meters: '))
# v = math.sqrt(2 * 9.8 * h)
# print(f'The speed of an object is {v}')
# --------------------------------------------
# task 20
# P = float(input('Enter the pressure in pascals: '))
# V = float(input('Enter the volume in liters: '))
# T = float(input('Enter the temperature on the Kelvin scale: '))
# T += 273.15
# P1 = 20000000
# V1 = 12
# T1 = 20 + 273.15
# R = 8.314
# n = (P * V) / (R * T)
# n1 = (P1 * V1) / (R * T1)
# print(f'{n}\n{n1}')
# --------------------------------------------
# task 21
# b = float(input('Enter the length of the base of the triangle: '))
# h = float(input('Enter the height the triangle: '))
# print(f'the area of a triangle is {(b * h) / 2}')
# --------------------------------------------
# task 22
# import math
# a = float(input('Enter 1st side of the triangle: '))
# b = float(input('Enter 2nd side of the triangle: '))
# c = float(input('Enter 3rd side of the triangle: '))
# s = (a + b+ c) / 2
# area = math.sqrt(s * (s - a) * (s - b) * (s - c))
# print(f'the area of a triangle is {area}')
# --------------------------------------------
# # task 23
# import math
# s = float(input('Enter the length of the side: '))
# n = float(input('Enter the number of sides: '))
# area = (n * (s ** 2)) / 4 * math.tan(math.pi / n)
# print(f'area -> {area}')
# --------------------------------------------
# task 24
# day = int(input('Enter days: '))
# hour = int(input('Enter hours: '))
# minute = int(input('Enter minute: '))
# sec = int(input('Enter seconds: '))
# sec += day * 24 * 60 * 60 + hour * 60 * 60 + minute * 60
# print(f'The number of seconds of the entered segment is {sec}')
# --------------------------------------------
# task 25
# sec = int(input('Enter seconds: '))
# day = sec // (24 * 60 * 60)
# sec -= day * 24 * 60 * 60
# hour = sec // (60 * 60)
# sec -= hour * 60 * 60
# minute = sec // 60
# sec -= minute * 60

# print(f'{day}:{"%02d" %hour}:{"%02d" %minute}:{"%02d" %sec}')
# --------------------------------------------
# task 26
# import time
# print(time.asctime())
# --------------------------------------------
# task 28
# height = float(input('Enter your height in centimeters: '))
# weight = float(input('Enter your weight in kilograms: '))
# print(f'Your body mass index is {weight/(height ** 2)}')
# --------------------------------------------
# task 29
# t = float(input(' Enter the air temperature in degrees Celsius (<10): '))
# v = float(input('Enter the wind speed in kilometers per hour (>4.8km/h): '))
# WCI = 13.12 + 0.6215 * t - 11.37 * (v ** 0.16) + 0.3965 * t * (v ** 0.16)
# print(f'WCI={round(WCI)}')
# --------------------------------------------
# task 30
# celsius = float(input('Enter the celsius: '))
# kelvin = celsius + 273.15
# fahrenheit = (celsius * 9/5) + 32
# print(f"{celsius} -> {fahrenheit} Fahrenheit and {kelvin} Kelvin: ")
# --------------------------------------------
# task 31
# kpa = float(input('Enter the pressure in kilopascals: '))
# psi = kpa * 0.145038
# mmhg = kpa * 7.50062
# atm = kpa / 101.325
# print(f'{kpa} equal to {psi} pounds per square inch , {mmhg} millimeters of mercury and {atm} atmosphere')
# --------------------------------------------
# task 32
# num = int(input('Enter four-digit integer: '))
# a = num % 10
# b = num // 10 % 10
# c = num // 100 % 10
# d = num // 1000 % 10
# sum = a + b + c + d
# print(f'The counting sum of its constituent digits will be {sum}')
# --------------------------------------------
# task 34
# bread = int(input("Enter how much bread you want to buy: "))
# discounted_price = bread * 3.49 - bread * 3.49 * 60 / 100
# print(f'Price of bread is {3.49 * bread}$\nDiscount price of bread is {round(discounted_price,3)}$')
# --------------------------------------------
# task 35
# n = int(input('Enter the number: '))
# if n%2 == 0:
#     print('Your number is even')
# else: 
#     print('Your number is odd')
# ------------------------------------
# task 36
# dog = int(input('Enter dog age: '))
# if 0< dog <= 2:
#     print(f'Humanage is {dog * 10.5}')
# else:
#     print(f'Human age = {21 + (4 * (dog - 2))}')
# ------------------------------------
# task 37
# word = input('Enter the word: ').lower()
# if word == ('a' or 'o' or 'y' or 'i' or 'e' or 'u'):
#     print('Your word is vowel')
# else:
#     print('Your word is consonant')
# ------------------------------------
# task 38
# n = int(input('Enter the number of sides: '))
# if (n < 3 or n > 10):
#     print('There is no such figure in geometry')
# elif n == 3:
#     print('It\'s a triangle')
# elif n == 4:
#     print('It\'s a rectangle or quadrilateral')
# elif n == 5:
#     print('It\'s a pentagon')
# elif n == 6:
#     print('It\'s a hexagon')
# elif n == 7:
#     print('It\'s a heptagon')
# elif n == 8:
#     print('It\'s a octagon')
# elif n == 9:
#     print('It\'s a nonagon')
# elif n == 10:
#     print('It\'s a decagon')
# ------------------------------------
# task 46
# a1 = input('Enter the color of a1: ').lower()
# square = input('Enter the position which color you want to know: ').lower()
# letter = square[0]
# number = int(square[1])
# aceg = 'a','c','e','g'
# bdfh = 'b','d','f','h'
# if a1 == 'black':
#     if (letter in aceg) and (number % 2 == 1):
#         print('Black')
#     elif (letter in bdfh) and (number % 2 == 0):
#         print('Black') 
#     else:
#         print('White ')
# elif (a1 == 'white'):
#     if (letter in aceg) and (number % 2 == 1):
#         print('White')
#     elif (letter in bdfh) and (number % 2 == 0):
#         print('White')
#     else:
#         print('Black')
# else:
#     print('There is no such color on chessboards')
# ------------------------------------
# task 47
# month = input('Enter the month: ').lower()
# day = int(input('Enter the day of month: '))
# if (month == 'december' and 21 < day <= 31) or (month == 'january' and 0 < day <= 31) or (month == 'february' and 0 < day <= 29) or (month == 'march' and 0 < day < 20):
#     print('It\'s winter')
# elif (month == 'march' and 20 <= day <= 31) or (month == 'april' and 0 < day < 31) or (month == 'may' and 0 < day <= 31) or (month == 'june' and 0 < day <= 21):
#     print('It\'s Spring')
# elif (month == 'june' and 21 < day <= 30) or (month == 'july' and 21 < day <= 31) or (month == 'august' and 0 < day <= 31) or (month == 'september' and 0 < day < 21):
#     print('It\'s Summer')
# elif (month == 'september' and 21 <= day <= 31) or (month == 'october' and 0 < day <= 31) or (month == 'november' and 0 < day <= 30) or (month == 'december' and 0 < day <= 21):
#     print('It\'s Autumn')
# else:
#     print('Error')
# ------------------------------------
# task 51
# import math
# a = float(input('Enter a: '))
# b = float(input('Enter b: '))
# c = float(input('Enter c: '))
# D = b ** 2 - 4 * a * c
# if D < 0:
#     print('There is no roots')
# elif D > 0:
#     x1 = (- b + math.sqrt(D)) / (2 * a)
#     x2 = (- b - math.sqrt(D)) / (2 * a)
#     print(f'First root is {x1} and second is {x2}')
# else:
#     x = - b / 2 * a
    # print(f'There is one root -> {x}')
# ------------------------------------
# task 57
# minutes = int(input('Enter the number of minutes spent per month: '))
# sms = int(input('Enter the number of SMS spent per month: '))
# money_min = 0
# money_sms = 0
# if minutes > 50:
#     money_min = (minutes - 50) * 0.25
# if sms > 50:
#     money_sms = (sms - 50) * 0.15
# taxes = round((15 + 0.44 + money_min + money_sms) * 0.05, 2)
# print(f'The base billing amount is 15.00$\
#       \nThe amount for additional minutes and messages is {money_min + money_sms}$\
#       \nThe amount of deductions to call centers 911 is 0.44$\
#       \nThe total amount is {taxes + 15 + 0.44 + money_min + money_sms}$')
# ------------------------------------
# task 58
# year = int(input('Enter the year: '))
# if year % 400 == 0:
#     print(f'{year} is leap year')
# elif year % 100 == 0:
#     print(f'{year} is\'nt leap year')
# elif year % 4 == 0:
#     print(f'{year} is leap year')
# ------------------------------------
# task 61
# car = input('Enter your car number: ')
# if car[0:2].isalpha() and car[0:2].isupper() and car[3:5].isdigit() and len(car) == 6:
#     print('Your car number type is old')
# elif car[0:2].isalpha() and car[0:2].isupper() and car[3:6].isdigit() and len(car) == 7:
#     print('Your car number type is new')
# else:
#     print('There is no such car number')
# ------------------------------------
# task 62
# red = 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36
# black = 2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35
# import random
# num = random.randint(0,36) or '00'

# if num == '00':
#     sort = 'Not even or odd'
# elif num % 2 == 0:
#     sort = 'Even'
# else:
#     sort = 'Odd'

# if num in red:
#     color = 'Red'
# elif num in black:
#     color = 'Black'
# else:
#     color = 'Green'
# if num == '00' or num == 0 :
#     position = '0 or 00'
# elif 0 < num <= 18:
#     position = '1 to 18'
# elif 18 <= num <= 36:
#     position = '19 to 36'

# print(f'Dropped number:{num}\nWinning bet:{num}\nWinning bet:{color}\nWinning bet:{sort}\nWinning bet:{position}')
# # ------------------------------------
# task 73
# alphabet = 'xyzabcdefghijklmnopqrstuvwxyz'
# text = input('Enter the text: ')
# n = int(input('Enter the number: '))
# for i in text:
#     print(alphabet[alphabet.index(i) + n], end='')
# ----------------------------------------
# task 74
# x = int(input('Enter x: '))
# guess = x / 2
# while guess * guess - x > 10 ** -12:
#     guess = (guess + x / guess) / 2
# print(guess)
# ----------------------------------------
# task 75 solution without loop
# text = input('Enter the text: ')
# if text == text[::-1]:
#     print('The text is a palindrome')
# else:
#     print('The text is\'nt a palindrome')
# ----------------------------------------
# task 75 solution with loop
# text = input('Enter the text: ')
# last = len(text) - 1
# count = 0

# for i in range(len(text)):
#     if text[i] != text[last]:
#         print('The text is\'nt a palindrome')
#         break
#     else:
#         last -= 1
#         count += 1
#     if count == len(text) // 2:
#         print('The text is a palindrome') 
# ----------------------------------------
# task 76 solution 1
# text = input('Enter the text: ').lower()
# line = ''

# for i in text:
#     if i.isalpha():
#         line += i
# if line == line[::-1]:
#     print('The line is a palindrome')
# else:
#     print('The text is\'nt a palindrome')
# ----------------------------------------
# task 76 solution 2
# text = input('Enter the text: ').lower()
# count = 0
# line = ''

# for i in text:
#     if i.isalpha():
#         line += i

# last = len(line) - 1

# for i in range(len(line)):
#     if line[i] != line[last]:
#         print('The text is\'nt a palindrome')
#         break
#     else:
#         last -= 1
#         count += 1
#     if count == len(line) // 2:
#         print('The text is a palindrome') 
# ----------------------------------------
# task 77
# print('    ',end='')
# for i in range (0,11):
#     for j in range(0,11):
#         if i != 0 and j != 0:
#             print(f'{j*i:>3}', end=' ')
#         elif i == 0 and j != 0:
#             print(f'{j:>3}', end=' ')
#         elif i != 0 and j == 0:
#             print(f'{i:>3}', end=' ')
#     print()
# ----------------------------------------
# task 78
# line = ''
# while True:
#     n = int(input("Enter positive numbers: "))
#     if n <= 0:
#         print('The number is negative or 0')
#         break
#     else:
#         line += str(n) + ","
#         while n != 1:
#             if n % 2 == 0:
#                 n = n // 2
#                 line += str(n) + ","
#             else:
#                 n = (n * 3) + 1
#                 line += str(n) + ","
#         print(line)
# ----------------------------------------
# task 79
# n = int(input("Enter first number: "))
# m = int(input("Enter second number: "))
# d = max(n, m)
# while True:
#     if n % d == 0 and m % d == 0:
#         print(d)
#         break
#     else:
#         d -= 1
# ----------------------------------------
# task 80
# n = int(input('Enter the number: '))
# factor = 2
# while factor <= n:
#     if n % factor == 0:
#         print(factor)
#         n = round(n/factor)
#     else:
        # factor += 1
# ----------------------------------------
# task 81
# num1 = input('Enter the binary number: ')
# l = len(num1) - 1
# num2 = 0
# for i in num1:
#     if l != 0:
#         num2 += int(i) * (2 ** l)
#         l -= 1
#     else:
#         break
# print(num2)
# ----------------------------------------
# task 82
# num1 = int(input('Enter the decimal number: '))
# num2 = ''
# while num1 > 0:
#     if num1 % 2 == 0:
#         num2 += '0'
#     else:
#         num2 += '1'
#     num1 //= 2
# print(num2[::-1])
# ----------------------------------------
# task 84
# import random
# summ = 0
# for i in range(10):
#     line = ''
#     count = 0
#     while 'PPP' not in line and 'OOO' not in line:
#         line += random.choice('OP')
#         count += 1
#     summ += count
#     print(f'{line}  -> count {count}')
# print(summ / 10)
#  ----------------------------------------
# task 85
# import math
# def right_triangle(a, b):
#     return math.sqrt(a ** 2 + b ** 2)

# a = float(input('Enter a = '))
# b = float(input('Enter b = '))
# print(f'c = {right_triangle(a, b)}')
# --------------------------------------------------
# task 86
# def Fare(kilometers):
#     metr = kilometers * 1000
#     return 4.25 * (metr // 140)

# distance = float(input('Enter travel distance in kilometers: '))
# print(f'Total taxi fare --> {Fare(distance)}$')
# --------------------------------------------------
# task 87
# def Delivery_Amount(count):
#     if count < 1:
#         return 'Error'
#     elif count == 1:
#         return 10.95
#     else:
#         return round(10.95 + (count - 1) * 2.95, 2)

# order_count = int(input('Enter the count of goods in order: '))
# print(Delivery_Amount(order_count))
# --------------------------------------------------
# task 88
# def Median(a,b,c):
#     if (a < b and a > c ) or (a < c and a > b):
#         return a
#     elif (b < a and b > c ) or (b < c and b > a):
#         return b
#     elif (c < a and c > b ) or (c < b and c > a):
#         return c
#     else:
#         return 'There is no median'

# first = float(input('Enter first number: '))
# second = float(input('Enter second number: '))
# third = float(input('Enter third number: '))
# print(f'{Median(first,second,third)}')
# --------------------------------------------------
# task 89
# def Num(n):
#     numbers = {
#         'one':1,
#         'two':2,
#         'three':3,
#         'four':4,
#         'five':5,
#         'six':6,
#         'seven':7,
#         'eight':8,
#         'nine':9,
#         'ten':10,
#         'eleven':11,
#         'twelve':12
#         }
#     for i in numbers:
#         if n == numbers[i]:
#             return i
#         else:
#             continue
        
# number = int(input('Enter number from 1 to 12: '))
# if 0 < number < 13:
#     print(Num(number))
# else:
#     print('Entered number not from 1 to 12')
# --------------------------------------------------
# task 90
# def Song(count):
#     lyrics1 = {
#         1:'On the first day of Christmas',
#         2:'On the second day of Christmas',
#         3:'On the third day of Christmas',
#         4:'On the fourth day of Christmas',
#         5:'On the fifth day of Christmas',
#         6:'On the sixth day of Christmas',
#         7:'On the seventh day of Christmas',
#         8:'On the eighth day of Christmas',
#         9:'On the ninth day of Christmas',
#         10:'On the tenth day of Christmas',
#         11:'On the eleventh day of Christmas',
#         12:'On the twelfth day of Christmas'
#     }
#     lyric2 = {
#         1:'A partridge in a pear tree',
#         2:'Two turtle doves, and',
#         3:'Three french hens',
#         4:'Four calling birds',
#         5:'Five golden rings',
#         6:'Six geese a-laying',
#         7:'Seven swans a-swimming',
#         8:'Eight maids a-milking',
#         9:'Nine ladies dancing',
#         10:'Ten lords a-leaping',
#         11:'Eleven pipers piping',
#         12:'Twelve drummers drumming' 
#     }
#     print(lyrics1[count])
#     print('my true love sent to me')
#     for i in range (count, 0, -1):
#         print(lyric2[i])
#     print(f'----------------[Verse {count}]----------------')

# count = 1
# for _ in range(0,12):    
#     Song(count)
#     count += 1
# --------------------------------------------------
# task 91
# def ordinalDate(day, month, year):
#     bool_ = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
#     if bool_ == 'False': 
#         month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     else:
#         month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if month == 1:
#         day_num = day
#     else:
#         day_num = day + sum(month_days[:month - 1])
#     return day_num

# day = int(input('Enter the day: '))
# month = int(input('Enter the month: '))
# year = int(input('Enter the year: '))
# if 0 < day < 31 and 0 < year and 0 < month < 13: 
#     print(ordinalDate(day, month, year))
# else:
#     print('Not correct date')
# --------------------------------------------------
# task 92 --half--
# def Month(year, day):
#     bool_ = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
#     if bool_ == 'False': 
#         month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#         if day > 364:
#             day -= 365 * (day//365)
#     else:
#         month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#         if day > 365:
#             day -= 366 * (day//366)
#     month = 0
#     while day > 0:
#         day = day - month_days[month]
#         month += 1
#     return month

# day = int(input('Enter the day: '))
# year = int(input('Enter the year: '))
# print(f'----------------- {Month(year, day)} -----------------')
# --------------------------------------------------
# task 93
# def Line(s,w):
#     if len(s) >= w:
#         return s
#     else:
#         count = (w - len(s)) // 2
#         return count * ' ' + s

# s = 'Albert'
# w = 10
# print(Line(s,w))
# --------------------------------------------------
# task 94
# def triangle(a, b, c):
#     summ = a + b + c
#     if max(a, b, c) < summ - max(a, b, c):
#         return 'True'
#     else:
#         return 'False'
    
# a = float(input('Enter first side: '))
# b = float(input('Enter second side: '))
# c = float(input('Enter third side: '))
# print(triangle(a, b, c))
# --------------------------------------------------
# task 95
# def Capital(text):
#     end = ['!', '.', '?']
#     s = [' ', '\'', '!', '.', '?']
#     text = list(text)
#     text[0] = text[0].upper()
#     for i in range(1, len(text)):
#         if text[i] in end:
#             for i in range(i + 1, len(text)):
#                 if text[i] == ' ':
#                     continue
#                 else:
#                     text[i] = text[i].upper()
#                     break
#         elif text[i] == 'i':
#             if text[i - 1] == ' ' and text[i + 1] in s:
#                 text[i] = text[i].upper()
#     text = ''.join(text)
#     return text

# line = 'what time do i have to be there? what\'s the address? this time i\'ll try to be on time!'
# print(Capital(line))
# --------------------------------------------------
# task 96
# def isInteger(string):
#     string.replace(' ','')
#     if string[0].isdigit() or string[0] == '+' or str[0] == '-':
#         bool_ = True
#     else:
#         bool_ = False
#     for i in range(1, len(string)):
#         if string[i].isdigit():
#             pass
#         else:
#             bool_ = False
#     if bool_ == False:
#         print('Not integer')

#     else:
#         print('Is integer')

# text = input('Enter the string: ')
# isInteger(text)    
# --------------------------------------------------
# task 98
# def Prime_number(num):
#     count = 0
#     for i in range(2, num):
#         if num % i == 0:
#             count += 1
#     if count != 0:
#         return 'False'
#     else:
#         return 'True'
    
# n = int(input('Enter the number: '))
# print(Prime_number(n))
# --------------------------------------------------
# task 99
# def Prime_number(num):
#     count = 0
#     for i in range(2, num):
#         if num % i == 0:
#             count += 1
#     if count != 0:
#         return 'False'
#     else:
#         return 'True'

# def nextPrime(n):
#     while True:
#         n += 1
#         if Prime_number(n) == 'True':
#             return n
#             break

# n = int(input('Enter the number: '))
# print(nextPrime(n))
# --------------------------------------------------
# task 110
# numlist = []
# while True:
#     num = int(input('Enter the number (enter 0 to finish): '))
#     if num == 0:
#         break
#     else:
#         numlist.append(num)
# print(sorted(numlist))
# ---------------------------------------------
# task 111
# numlist = []
# while True:
#     num = int(input('Enter the number (enter 0 to finish): '))
#     if num == 0:
#         break
#     else:
#         numlist.append(num)
# print(sorted(numlist)[::-1])
# ---------------------------------------------
# task 112
# mylist = []
# newlist = []
# while True:
#     num = int(input('Enter the number (enter 0 to finish): '))
#     if num == 0:
#         break
#     else:
#         mylist.append(num)
# mylist.sort()
# for i in range(1,len(mylist) - 1):
#     if mylist[i] != mylist[0] and mylist[i] != mylist[-1]:
#         newlist.append(mylist[i])
# print(f'your list --> {newlist}\nremoved numbers --> {mylist[0]}, {mylist[-1]}')
# ---------------------------------------------
# task 113
# mylist = []
# newlist = []
# while True:
#     text = input('Enter the text: ')
#     if text == '':
#         break
#     else:
#         mylist.append(text)
# for i in mylist:
#     if i not in newlist:
#         newlist.append(i)
# print(newlist)
# ---------------------------------------------
# task 114
# mylist = []
# newlist = []
# while True:
#     num = input('Enter the number: ')
#     if num == '':
#         break
#     else:
#         num = int(num)
#         mylist.append(num)
# for i in mylist:
#     if i < 0:
#         newlist.append(i)
# for i in mylist:
#     if i == 0:
#         newlist.append(i)
# for i in mylist:
#     if i > 0:
#         newlist.append(i)
# print(newlist)
# ---------------------------------------------
# task 115
# def baj(n, List):
#     for i in range(1, n // 2 + 1):
#         if n % i == 0:
#             List.append(i)
#     print(List)

# mylist = []
# numlist = []
# while True:
#     num = int(input('Enter the number: '))
#     if num < 2:
#         print('Break')
#         break
#     elif num not in numlist:
#         baj(num,mylist)
#         mylist = []
#     elif num in numlist:
#         print('Repetition!')
#     numlist.append(num)
# ---------------------------------------------
# task 116
# def kataryal(n):
#     count = 0
#     summ = 0
#     for i in range(1, n // 2 + 1):
#         if n % i == 0:
#             count += 1
#             summ += i
#     if n == summ:
#         print('True')
#     else:
#         print('False')
# num = int(input('Enter the number: '))
# kataryal(num)
# ---------------------------------------------
# task 117
# text = 'Hello!+ը@նկե*ր+Ալբերտ+:),գնացինք?'
# text2 = "Contractions include: don't, isn't, and wouldn't."
# symbols = '!@#$%^&*?;:.,<()>'

# for i in text:
#     if i in symbols:
#         text = text.replace(i,'')
# text = text.split('+')
# print(text)

# for i in text2:
#     if i in symbols:
#         text2 = text2.replace(i,'')
# text2 = text2.split(' ')
# print(text2)
# ---------------------------------------------
# task 118
# text = input('Enter the text: ').lower()
# text = text.split(' ')
# line = []
# count = 0
# for i in text:
#     if i.isalpha():
#         line.append(i)
# for i in range(0, len(line) // 2):
#     if line[i] != line[-i-1]:
#         print('The line is\'nt a palindrome')
#         break
#     else:
#         count += 1
# if count > len(line) // 2 - 1:
#     print('The line is a palindrome')
# ---------------------------------------------
# task 119
# mylist = []
# summ = 0
# while True:
#     num = input('Enter the number: ')
#     if num == '':
#         break
#     else:
#         num = int(num)
#         mylist.append(num)
#         summ += num
# average = summ // len(mylist)
# print(average)

# for i in mylist:
#     if i > average:
#         print(i, end=' ')
# for i in mylist:
#     if i == average:
#         print(i, end=' ')
# for i in mylist:
#     if i < average:
#         print(i, end=' ')
# ---------------------------------------------
# task 120
# line = []
# while True:
#     text = input('Enter the text: ')
#     if text == '':
#         break
#     else:
#         line.append(text)
# if len(line) > 1:
#     line.insert(-1, 'and')
# print(line)
# ---------------------------------------------
# task 121
# import random
# numlist = []
# line = []
# for i in range(1,50):
#     numlist.append(str(i))
# for _ in range(0,6):
#     n = random.choice(numlist)
#     line.append(n)
#     numlist.remove(n)
# print(line)
# ---------------------------------------------
# task 122
# ալարեցի գրեմ
# ---------------------------------------------
# task 123
# 122-ը որ ալարեցի գրեմ, էս էլ պետքա ալարեմ
# ---------------------------------------------
# task 124
# koord = []
# xsum, ysum, xy, x2 = (0,0,0,0)
# while True:
#     x = input('Enter x: ')
#     if x == '':
#         break
#     else:
#         y = input('Enter y: ')
#         x = float(x)
#         y = float(y)
#         koord.append(x)
#         koord.append(y)
#         xsum += x
#         ysum += y

# n = (len(koord) // 2)
# x_ = xsum // n
# y_ = ysum // n

# for i in range(0, len(koord), 2):
#     xy += koord[i] * koord[i+1]
#     x2 += koord[i] ** 2

# m = (xy - (xsum * ysum / n)) / (x2 - (xsum ** 2 / n))
# b = y_ - m * x_
# print(f'y = {m}x + {b}')
# ---------------------------------------------
# task 125 with import random
# def createDeck():
#     mast = ['s', 'h', 'd', 'c']
#     tiv = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
#     karter = []
#     for i in mast:
#         for j in tiv:
#             karter.append(j + i)
#     return karter

# def shuffle(List):
#     import random
#     newlist = List.copy()
#     random.shuffle(newlist)
#     print(newlist)

# print(createDeck())
# shuffle(createDeck())
# ---------------------------------------------
# task 126
# def createDeck():
#     mast = ['s', 'h', 'd', 'c']
#     tiv = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
#     karter = []
#     for i in mast:
#         for j in tiv:
#             karter.append(j + i)
#     return karter

# def deal(n, card):
#     import random
#     a,b,c,d = ([],[],[],[])
#     deck = createDeck().copy()
#     if n * card <= 52:
#         for _ in range(0,n):
#             for _ in range(0,card):
#                 n = random.choice(deck)
#                 a.append(n)
#                 deck.remove(n)
#             print(a)
#             a.clear()
# n = int(input('Enter the number of players: '))
# c = int(input('Enter the number of cards for one person: '))
# deal(n, c)
# ---------------------------------------------
# task 127
# def sorted(List):
#     newlist = List.copy()
#     newlist.sort()
#     for i in range(0, len(List)):
#         if newlist[i] != List[i]:
#             return 'False'
#         return 'True'
# mylist = []
# while True:
#     x = int(input('Enter x: '))
#     if x == 0:
#         break
#     else:
#         mylist.append(x)
# print(sorted(mylist))
# ---------------------------------------------
# task 128
# def countRange(List,Min, Max):
#     count = 0
#     for i in List:
#         if i > Min and i < Max:
#             count += 1
#     return count
# mylist = [1, 6, 8, 3, 9, 17]
# a, b = (0, 10)
# print(countRange(mylist, a, b))
# ---------------------------------------------
# 173 Сумма значений
# def SumOfNumbers():
#     num = int(input('Enter numbers you want sum (enter  0 for finish): '))
#     if num == 0:
#         return 0
#     else:
#         return num + SumOfNumbers()
    
# print(SumOfNumbers())
# -------------------------------------------------
# 174 Наибольший общий делитель
# def MaxDivider(a, b):
#     if b == 0:
#         return a
#     else:
#         return MaxDivider(b, a % b)

# num1 = int(input('Enter first number: '))
# num2 = int(input('Enter second number: '))
# print(MaxDivider(num1, num2))
# -------------------------------------------------
# 175 Рекурсивный перевод числа из десятичного в двоичное
# def Binary(n):
#     if n == 1:
#         return '1'
#     else:
#         return Binary(n // 2) + str(n % 2)

# num = int(input('Enter the decimal number: '))
# print(Binary(num))
# -------------------------------------------------
# 176 Фонетический алфавит НАТО
# def NATO(sms):
    # alphabet = {
    #     "A": "Alpha", "J": "Juliet", "S": "Sierra",
    #     "B": "Bravo", "K": "Kilo", "T": "Tango",
    #     "C": "Charlie", "L": "Lima", "U": "Uniform",
    #     "D": "Delta", "M": "Mike", "V": "Victor",
    #     "E": "Echo", "N": "November", "W": "Whiskey",
    #     "F": "Foxtrot", "O": "Oscar", "X": "Xray",
    #     "G": "Golf", "P": "Papa", "Y": "Yankee",
    #     "H": "Hotel", "Q": "Quebec", "Z": "Zulu",
    #     "I": "India", "R": "Romeo"
    # }
    # if len(sms) == 0:
    #     return ''
    # if sms[0] not in alphabet:
    #     return ''
    # else:
    #     return alphabet[sms[0]] + ' ' + NATO(sms[1:]) 

# print(NATO('HELLO'))
# -------------------------------------------------
# 177 Римские цифры
# def RomanToNum(hromeakan):
#     num_dict = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
#     if len(hromeakan) == 0:
#         return 
#     elif len(hromeakan) == 1 :
#         return num_dict[hromeakan]
#     else:
#         if num_dict[hromeakan[0]] >= num_dict[hromeakan[1]]:
#             return num_dict[hromeakan[0]] + RomanToNum(hromeakan[1:])
#         else:
#             if len(hromeakan) > 2:
#                 return num_dict[hromeakan[1]] - num_dict[hromeakan[0]] + RomanToNum(hromeakan[2:])
#             else:
#                 return num_dict[hromeakan[1]] - num_dict[hromeakan[0]]
# print(RomanToNum('MXIV')) # 1014
# print(RomanToNum('MIX')) # 1009
# -------------------------------------------------
# 178 Рекурсивные палиндромы
# def Palindrom(text):
#     if len(text) < 2:
#         print('The text is a palindrome')
#     else:
#         if text[0] == text[-1]:
#             Palindrom(text[1:-1])
#         else:
#             print('The text is\'nt palindrome')

# text = input('Enter the text: ')
# line = text.replace(' ','')
# Palindrom(line)
# -------------------------------------------------
# 179 Рекурсивный квадратный корень
# def SQRT(n,guess=1):
#     if guess ** 2 - n <= 10 ** (-12) and guess != 1:
#         return guess
#     else:
#         return SQRT(n, (guess + n / guess) / 2)
# print(SQRT(49))
# -------------------------------------------------
# 182 Слова через химические элементы
# def func(text):
#     periodic_table = [
#         "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl",
#         "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Ni", "Co", "Cu", "Zn", "Ga", "Ge", "As",
#         "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In",
#         "Sn", "Sb", "I", "Te", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb",
#         "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl",
#         "Pb", "Bi", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr",
#         "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"
#     ]
#     text = text.title()
#     if len(text) >= 2 and text[0] + text[1] in periodic_table:
#         return text[0] + text[1] + func(text[1:])
#     elif text[0] in periodic_table:
#         return text[0] + func(text[1:])
#     else:
#         return '-'

# text = input('Enter the text:')    
# print(f'{text} может быть представлен как {func(text)}')
# -------------------------------------------------
# 184 Выравниваем список
# def Pakagcer(list_):
#     if list_ == []:
#         return []
#     if type(list_[0]) == int:
#         return [list_[0]] + Pakagcer(list_[1:])
#     else:
#         return Pakagcer(list_[0]) + Pakagcer(list_[1:])

# mylist = [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]
# print(Pakagcer(mylist))
# -------------------------------------------------
# 185 Декодирование на основе длин серий
# def PrintList(mylist):
#     if mylist == []:
#         return []
#     else:
#         return [mylist[0]] * mylist[1] + PrintList(mylist[2:])

# mylist = ["A", 12, "B", 4, "A", 6, "B", 1]
# print(PrintList(mylist))
# -------------------------------------------------
# 186 Кодирование на основе длин серий
# def Hakarak(mylist, count=1):
#     if len(mylist) == mylist.count(mylist[0]):
#         return [mylist[0], mylist.count(mylist[0])]
#     if mylist[0] == mylist[1]:
#         return Hakarak(mylist[1:], count + 1)
#     else:
#         return [mylist[0], count] + Hakarak(mylist[1:], count=1)

# a = ['A', 12, 'B', 4, 'A', 6, 'B', 1]
# mylist = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B']
# print(Hakarak(mylist))
# ------------------------------------------------