# # Найти НОК двух чисел

# import random
# from random import randint

# first_number, second_number = 9, 12
# nok = min(first_number,second_number)
# while True:
#     if nok%first_number==0 and nok%second_number==0:
#         break
#     nok += 1
# print(nok)

# # Вычислить число Пи c заданной точностью d

# import math
# from unicodedata import decimal

# k = 1
# s = 0
# for i in range ( 1000000 ):
#     if i % 2 == 0 :
#         s += 4 / k
#     else :
#         s -= 4 / k
#     k += 2
# s = float(s)
# print ('%.2f' %s)

# # Дана последовательность чисел. Получить список неповторяющихся элементов исходной 
# # последовательности
# # Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

# start_list = [1, 2, 3, 5, 1, 5, 3, 10 ]
# fin_list = []
# for i in range (len(start_list)):
#     if start_list.count(start_list[i]) == 1: fin_list.append(start_list[i])
# print(fin_list)

# # Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа. 
# import random
# from random import randint

# n = 0

# with open('doc.txt', 'w') as doc:
#     while n < 10:
#         doc.write(str(randint(1,10))+' ')
#         n+=1
    
# with open('doc.txt', 'r') as doc:
#     numbers = doc.read().split()
#     new_list = []
#     new_numbers = ''
#     print(numbers)
#     for i in range (len(numbers)):
#         if (int(numbers[i]) % 2 != 0):
#            new_list.append(numbers[i])
#     print(new_list)

# with open('doc.txt', 'w') as doc:
#     for i in range (len(new_list)):
#         new_numbers = new_numbers+new_list[i]
#     print(new_numbers)
#     doc.write(new_numbers)
    

# # Римские цифры

# roman_numbers = {
# 'I': '1', 'II': '2', 'III': '3', 'IV': '4', 'V': '5', 'VL': '6', 'VII': '7', 'VIII':'8', 'IX': '9', 'X': '10',
# 'XXL': '40', 'L': '50', 'LX': '60', 'LXX': '70', 'LXXX': '80', 'XC': '90', 'C': '100', 'CC': '200', 'CCC': '300',
# 'CD': '400', 'D': '500', 'DC': '600', 'DCC': '700', 'DCCC': '800', 'DM': '900', 'M': '1000' 
# }

# def roman_to_arabian(string, dictionary):
#     string = string.upper()
#     arabian_number = 0
#     for i in range(len(string)):
#         for key in dictionary.keys():
#             if string.count(key):
#                 arabian_number+=int(dictionary.get(key))
#     return arabian_number

# a = input('Введите римскую цифру ')
# b = roman_to_arabian(a, roman_numbers)
# print(b)

# # Маркеры

# def clear_garbage(string):
#     garbage = "!'@#$%^&*()`/:;.,? <>\|'""+ -=[]}{"
#     new_string = ''
#     for char in string:
#         if char not in garbage:
#             new_string+=char
#         else:
#             break
    
#     return new_string

# user_string = input('Введите какой-нибудь текст ')
# print(clear_garbage(user_string))

# # # # pyramid = []
# # # # with open('task7.txt', 'r') as doc:
# # # #     for line in doc:
# # # #         pyramid.append([int(x) for x in line.split()])
# # # # print(pyramid) # далее ступор (( две ночи до 5 утра в поисках 
# result = 0
# with open('task7.txt', 'r') as doc:
#     line1 = doc.readline().strip().split()
#     line2 = doc.readline().strip().split()
#     line3 = doc.readline().strip().split()
#     line4 = doc.readline().strip().split()
#     line5 = doc.readline().strip().split()
#     line6 = doc.readline().strip().split()
#     line7 = doc.readline().strip().split()
#     line8 = doc.readline().strip().split()
#     line9 = doc.readline().strip().split()
#     line10 = doc.readline().strip().split()
#     line11 = doc.readline().strip().split()
#     line12 = doc.readline().strip().split()
#     line13 = doc.readline().strip().split()
#     line14 = doc.readline().strip().split()
#     line15 = doc.readline().strip().split()
# element_position = 0
# max_element = 0
# result+=(int(max(line1))+(int(max(line2))))
# print(result)

# def line_max(string, position):
#     for i in range(len(string)):
#         max_element = int(max(string[position], string[position+1]))
#         # print(max_element)
#         return max_element
# def line_element_position(string, maximum_element):
#     max_element = str(maximum_element)
#     for i in range(len(string)):
#             position = string.index(max_element)
#             print(position)
#             return position
# def pyramid_sum(result, max_element):
#     result+=(int(max_element))
#     return result
# max_element = line_max(line2, element_position)
# element_position = line_element_position(line2, max_element )
# result = pyramid_sum(result, max_element)
# max_element = line_max(line3, element_position)
# element_position = line_element_position(line3, max_element )
# result = pyramid_sum(result, max_element)
# max_element = line_max(line4, element_position)
# element_position = line_element_position(line4, max_element )
# result = pyramid_sum(result, max_element)
# max_element = line_max(line5, element_position)
# element_position = line_element_position(line5, max_element )
# result = pyramid_sum(result, max_element)
# max_element = line_max(line6, element_position)
# element_position = line_element_position(line6, max_element )
# result = pyramid_sum(result, max_element)
# max_element = line_max(line7, element_position)
# element_position = line_element_position(line7, max_element )
# result = pyramid_sum(result, max_element)
# max_element = line_max(line8, element_position)
# element_position = line_element_position(line8, max_element )
# result = pyramid_sum(result, max_element)
# max_element = line_max(line9, element_position)
# element_position = line_element_position(line9, max_element )
# result = pyramid_sum(result, max_element)
# max_element = line_max(line10, element_position)
# element_position = line_element_position(line10, max_element )
# result = pyramid_sum(result, max_element)
# max_element = line_max(line11, element_position)
# element_position = line_element_position(line11, max_element )
# result = pyramid_sum(result, max_element)
# max_element = line_max(line12, element_position)
# element_position = line_element_position(line12, max_element )
# result = pyramid_sum(result, max_element)
# max_element = line_max(line13, element_position)
# element_position = line_element_position(line13, max_element ) # тут логика ломается и я не знаю, как исправить(
# result = pyramid_sum(result, max_element)
# max_element = line_max(line14, element_position)
# element_position = line_element_position(line14, max_element )
# result = pyramid_sum(result, max_element)
# max_element = line_max(line15, element_position)
# element_position = line_element_position(line15, max_element )
# result = pyramid_sum(result, max_element)
# print(result)

