# Create Phone Number
# "(123) 456-7890"
# n = [1,2,3,4,5,6,7,8,9,0]
# phone_number = '('
# for i in range(0,3):
#     phone_number += str(n[i])
# phone_number += ') '
# for i in range(3,6):
#     phone_number += str(n[i])
# phone_number += '-'
# for i in range(6,len(n)):
#     phone_number += str(n[i])
# print(phone_number)
# --------------------------------------------
# Who likes it?
# def likes(names):
#     if not names:
#         return 'no one likes this'
#     elif len(names) == 1:
#         return f'{names[0]} likes this'
#     elif len(names) == 2:
#         return f'{names[0]} and {names[1]} like this'
#     elif len(names) == 3:
#         return f'{names[0]}, {names[1]} and {names[2]} like this'
#     else:
#         return f'{names[0]}, {names[1]} and {len(names)-2} others like this'
# --------------------------------------------
# Array.diff
# def array_diff(a, b):
    # return [x for x in a if x not in b]
# --------------------------------------------
# Sum of Digits / Digital Root
# def digital_root(n):
#     list_ = []
#     if n < 10:
#         return n
#     else:
#         while n >= 10:
#             m = len(str(n))
#             for _ in range(0, m):
#                 list_.append(n % 10)
#                 n = n // 10
#             if sum(list_) > 9:
#                 n = sum(list_)
#                 list_.clear()
#         return sum(list_)
# --------------------------------------------
# def count_duplicates(text):
#     text = text.lower()
#     count = 0
#     seen = set()
#     duplicates = set()

    # for char in text:
    #     if char.isalnum():
    #         if char in seen:
    #             duplicates.add(char)
    #         else:
    #             seen.add(char)

    # return len(duplicates)
# --------------------------------------------
# Vowel Count
# def get_count(sentence):
#     vowels = ['a', 'e', 'i','o', 'u']
#     count = 0
#     for i in sentence:
#         if i in vowels:
#             count += 1
#     return count
# --------------------------------------------
# Sum of Intervals 4kyu --> 32 points
# def sum_of_intervals(intervals):
#     list_ = []
#     for i in intervals:
#         for j in range(i[0]+1, i[1]+1):
#             if j not in list_:
#                 list_.append(j)
#     return len(list_)
# --------------------------------------------
# Human Readable Time 5 kyu --> 38 points
# --------------------------------------------
# Stop gninnipS My sdroW!  6 kyu --> 8 points
# def spin_words(sentence):
#     list_ = []
#     for i in sentence.split():
#         if len(i) > 4:
#             list_.append(i[::-1])
#         else:
#             list_.append(i)
#     return ' '.join(list_)
# print(spin_words('Hey fellow warriors'))
#                 Hey wollef sroirraw
# --------------------------------------------
# "Stringing"+"Me"+"Along" --> 6kyu
# def create_message(s):
#     list.append(s)
#     def word(list_)
#         new = ''
#         for i in list_:
#             new += i
#         return ' '.join(new)
#     return list_

# print(create_message(("Hello")("World!")("how")("are")("you?")))
# --------------------------------------------
# Beginner Series #3 Sum of Numbers 7 kyu --> 2 or 8 points
# def get_sum(a,b):
#     if a == b:
#         return a 
#     else:
#         num_list= []
#         while a <= b:
#             num_list.append(a)
#             a += 1
#         return sum(num_list)
# print(get_sum(-5,4))
# --------------------------------------------
# def count_bits(n):
#     if n == 0:
#         return 0
#     binary = ''
#     while n > 0:
#         if n % 2 == 0:
#             binary += '0'
#         else:
#             binary += '1'
#         n //= 2
#         erkuakan = binary[::-1]
#     count = str(erkuakan).count('1')
#     return count

# print(count_bits(9))
# --------------------------------------------
# Highest and Lowest 7kyu --> 2 points
# def high_and_low(numbers):
#     numbers = numbers.split(' ')
#     high = int(numbers[0])
#     low = int(numbers[1])
#     for i in numbers:
#         high = max(int(i), high)
#         low = min(int(i), low)
#     return  f'{high} {low}'

# print(high_and_low('1 2 3 4 5 6 7'))
# --------------------------------------------
# Find The Parity Outlier 6kyu --> 8 points
# def find_outlier(integers):
#     count = 0
#     odd = []
#     even = []
#     for i in integers:
#         if i % 2 == 0:
#             count += 1
#             even.append(i)
#         elif i % 2 == 1:
#             count -= 1
#             odd.append(i)
#     if count > 0:
#         return odd
#     else:
#         return even
    
# print(find_outlier([1,2,3,5,7,9]))
# --------------------------------------------
# Which are in? 6kyu --> 8 points
# def in_array(array1, array2):
#     text2 = ''
#     new_array = []
#     for i in array2:
#         text2 += i + ' '
#     for i in array1:
#         if i in text2:
#             new_array.append(i)
#     return new_array
# --------------------------------------------
# Moving Zeros To The End 5 kyu --> 8 points
# def move_zeros(lst):
#     new_list = []
#     count = 0
#     for i in lst:
#         if i != 0:
#             new_list.append(i)
#         else:
#             count += 1
#     for i in range(0, count):
#         new_list.append(0)
#     return new_list
# --------------------------------------------
# The Hashtag Generator 5kyu --> 8 points
# def generate_hashtag(s):
#     text = s.split(' ')
#     hashtag = '#'
#     for i in text:
#         if i != ' ':
#             hashtag += i.title()
#     if len(hashtag) < 2 or len(hashtag) > 140:
#         return False
#     else:
#         return hashtag
# --------------------------------------------
# Snail 4kyu --> 0 points
# def snail(snail_map): 
    
# array = [[1,2,3],
#          [8,9,4],         
#          [7,6,5]]
# snail(array) # => [1,2,3,4,5,6,7,8,9]
# --------------------------------------------
# Mexican wave 7kyu --> 8 points
# def wave(people):
#     list_ = []
#     list_.append(people.title())
#     for i in range(1, len(people)):
#         text = ''
#         text += people[:i] + people[i].upper() + people[i+1:]
#         list_.append(text)
#     return list_
# print(wave('hello'))
