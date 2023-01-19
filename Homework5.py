# 1. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит заданное количество конфет.
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.

# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

# 2021 % 29 = 69 * 29 + 20
# Бота с интеллектом делать бесполезно, т.к. он в любом случае проиграет первому игроку со стратегией %29.
# По сути бот с возможностью первого хода со стратегией %29 и есть этот самый бот с интеллектом

# import random
# numSweets = 202
# numSweetsForTime = 28

# secondMove = 0
# i = 1
# while numSweets > numSweetsForTime:
#     firstMove = numSweets % (numSweetsForTime + 1)
#     print(f'{i}-ый ход первого игрока - {firstMove} конфет')
#     secondMove = random.randint(1, 28)
#     print(f'{i}-ый ход второго игрока - {secondMove} конфет')
#     numSweets -= secondMove + firstMove
#     i += 1
# print(f'Последний ход первого игрокa - {numSweets} конфет')

# 2. Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом

# Вариант 1 - комп играет сам с собой, оба игрока выбирают случайные числа
# from random import randint
# def pr(a, b, c, d, e, f, g, h, o):
#     print()
#     print(a, '\t', b, '\t', c)
#     print()
#     print(d, '\t', e, '\t', f)
#     print()
#     print(g, '\t', h, '\t', o)
#     print()

# x = []
# for _ in range(1, 10):
#     x.append('*')

# pr(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8])

# step = 1
# my_set = {0, 0}
# i = 0
# j = 0
# while step < 5:
#     print(f'step={step}')
#     while i in my_set:
#         i = randint(1, 9)
#     my_set.add(i)
#     x[i - 1] = 'X'
#     if step > 2 and (x[0] == x[4] == x[8] == 'X' or x[2] == x[4] == x[6] == 'X' \
#         or x[0] == x[1] == x[2] == 'X' or x[3] == x[4] == x[5] == 'X' \
#             or x[6] == x[7] == x[8] == 'X' or x[0] == x[3] == x[6] == 'X' \
#                 or x[1] == x[4] == x[7] == 'X' or x[2] == x[5] == x[8] == 'X'):
#         pr(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8])        
#         print('Выиграли крестики!')
#         break    
#     while j in my_set:
#         j = randint(1, 9)
#     my_set.add(j)
#     x[j - 1] = 'O'
#     pr(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8])
#     if step > 2 and (x[0] == x[4] == x[8] == 'O' or x[2] == x[4] == x[6] == 'O' \
#         or x[0] == x[1] == x[2] == 'O' or x[3] == x[4] == x[5] == 'O' \
#             or x[6] == x[7] == x[8] == 'O' or x[0] == x[3] == x[6] == 'O' \
#                 or x[1] == x[4] == x[7] == 'O' or x[2] == x[5] == x[8] == 'O'):
#         print('Выиграли нолики!')
#         break
#     step +=1
# else:
#     print('Ничья!')

# Вариант 2 - человек играет крестиками и задает ход через панель, комп выбирает случайные числа
# from random import randint
# def pr(a, b, c, d, e, f, g, h, o):
#     print()
#     print(a, '\t', b, '\t', c)
#     print()
#     print(d, '\t', e, '\t', f)
#     print()
#     print(g, '\t', h, '\t', o)
#     print()

# x = []
# for i in range(1, 10):
#     x.append(i)

# pr(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8])

# step = 1
# my_set = {0, 0}
# i = 0
# j = 0
# while step < 5:
#     print(f'step={step}')
#     print('Ваш ход, введите номер позиции: ')
#     i = int(input())
#     my_set.add(i)
#     x[i - 1] = 'X'
#     if step > 2 and (x[0] == x[4] == x[8] == 'X' or x[2] == x[4] == x[6] == 'X' \
#         or x[0] == x[1] == x[2] == 'X' or x[3] == x[4] == x[5] == 'X' \
#             or x[6] == x[7] == x[8] == 'X' or x[0] == x[3] == x[6] == 'X' \
#                 or x[1] == x[4] == x[7] == 'X' or x[2] == x[5] == x[8] == 'X'):
#         pr(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8])        
#         print('Выиграли крестики!')
#         break    
#     while j in my_set:
#         j = randint(1, 9)
#     my_set.add(j)
#     x[j - 1] = 'O'
#     pr(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8])
#     if step > 2 and (x[0] == x[4] == x[8] == 'O' or x[2] == x[4] == x[6] == 'O' \
#         or x[0] == x[1] == x[2] == 'O' or x[3] == x[4] == x[5] == 'O' \
#             or x[6] == x[7] == x[8] == 'O' or x[0] == x[3] == x[6] == 'O' \
#                 or x[1] == x[4] == x[7] == 'O' or x[2] == x[5] == x[8] == 'O'):
#         print('Выиграл Мурзик!')
#         break
#     step +=1
# else:
#     print('Ничья!')

# Вариант 3 - человек играет крестиками и задает ход через панель, комп - "немного" интеллектуал
# from random import randint
# def pr(a, b, c, d, e, f, g, h, o):
#     print()
#     print(a, '\t', b, '\t', c)
#     print()
#     print(d, '\t', e, '\t', f)
#     print()
#     print(g, '\t', h, '\t', o)
#     print()

# x = []
# for i in range(1, 10):
#     x.append(i)

# pr(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8])

# step = 1
# my_set = {0, 0}
# i = 0
# j = 0
# while step < 5:
#     print(f'step={step}')
#     print('Ваш ход, введите номер позиции: ')
#     i = int(input())
#     my_set.add(i)
#     x[i - 1] = 'X'
#     # print(my_set)
#     if step > 2 and (x[0] == x[4] == x[8] == 'X' or x[2] == x[4] == x[6] == 'X' \
#         or x[0] == x[1] == x[2] == 'X' or x[3] == x[4] == x[5] == 'X' \
#             or x[6] == x[7] == x[8] == 'X' or x[0] == x[3] == x[6] == 'X' \
#                 or x[1] == x[4] == x[7] == 'X' or x[2] == x[5] == x[8] == 'X'):
#         pr(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8])        
#         print('Выиграли крестики!')
#         break 
#     if step == 1:   
#         j = 5
#         if 5 in my_set:
#             j = 1
#     else:    
#         for k in [0, 3, 6]:
#             if x[k] == x[k + 2]:
#                 j = k + 2
#             if x[k] == x[k + 1]:
#                 j = k + 3
#             if x[k + 1] == x[k + 2]:
#                 j = k + 1
#         for k in [0, 1, 2]:
#             if x[k] == x[k + 6]:
#                 j = k + 4
#             if x[k] == x[k + 3]:
#                 j = k + 7
#             if x[k + 3] == x[k + 6]:
#                 j = k + 1
#         if x[0] == x[8] or x[2] == x[6]:
#             j = 5
#         if x[0] == x[4]:
#             j = 9
#         if x[4] == x[8]:
#             j = 1
#         if x[2] == x[4]:
#             j = 7
#         if x[4] == x[6]:
#             j = 3
#     while j in my_set:
#         j = randint(1, 9)
#     my_set.add(j)
#     x[j - 1] = 'O'
#     pr(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8])
#     if step > 2 and (x[0] == x[4] == x[8] == 'O' or x[2] == x[4] == x[6] == 'O' \
#         or x[0] == x[1] == x[2] == 'O' or x[3] == x[4] == x[5] == 'O' \
#             or x[6] == x[7] == x[8] == 'O' or x[0] == x[3] == x[6] == 'O' \
#                 or x[1] == x[4] == x[7] == 'O' or x[2] == x[5] == x[8] == 'O'):
#         print('Выиграл Мурзик!')
#         break
#     step +=1
# else:
#     print('Ничья!')

# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

# path = "Lesson5_Homework\TextInput5.txt"
# with open (path, 'r', encoding='utf-8') as file:
#     my_text = file.readline()

# new_text = ''
# i = 0
# while i < len(my_text):
#     simbol = my_text[i]
#     count = 0
#     for j in range(i + 1, len(my_text)):
#         if simbol == my_text[j]:
#             if my_text[j] == my_text[j - 1]:
#                 count += 1
#         else:
#             break
#     new_text += str(count + 1) + simbol
#     i = i + count + 1

# fig = 0
# for item in new_text:
#     if item.isdigit():
#         fig += 1

# my_text = ''
# i = 0
# while i < len(new_text):
#     if new_text[i].isdigit() and not new_text[i + 1].isdigit():
#         my_text += new_text[i + 1] * int(new_text[i])
#         i += 2
#     else:
#         flag = 2
#         for j in range(i + 2, i + fig):
#             if new_text[j].isdigit():
#                 flag += 1
#             else:
#                 flag1 = ''
#                 for k in range(i, i + flag):
#                     flag1 += new_text[k]
#                 my_text += new_text[i + flag] * int(flag1)
#                 break
#         i += flag + 1

# with open ('Lesson5_Homework\TextOutput.txt', 'w', encoding='utf-8') as file:
#     file.write(new_text + '\n' + my_text)
    