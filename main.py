import math
import numpy as np

# Задачи на циклы и оператор условия------
# ----------------------------------------
gl_run = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # массив для блокировки выполнения некоторых заданий
"""
Задача 1

Вывести на экран циклом пять строк из нулей длиной 4, причем каждая строка должна быть пронумерована.

Пример:
    0 0000
    1 0000
    2 0000
    3 0000
....
"""

if 1 in gl_run:
    print('Задание 1-------------------------------------------------------------------------------')
    i = 1
    while i < 6:
        print(str(i) + ' ', end='')
        for ii in range(6):
            print(0, end='')
        print('')
        i += 1
    print('Окончание выполнения Задания 1----------------------------------------------------------\n\n')
'''
Задача 2

Пользователь в цикле вводит 10 производных цифр. Выведите количество введенных пользователем цифр 5.
'''
if 2 in gl_run:
    print('Задание 2-------------------------------------------------------------------------------')
    inp = []
    for i in range(10):
        inp.append(int(input('Введите цифру ' + str(i + 1) + ":")))
    five_count = 0
    five_words = ['ноль', 'одну', 'две', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
    five_word_ends = ['пятёрок', 'пятёрку', 'пятёрки', 'пятёрки', 'пятёрки', 'пятёрок', 'пятёрок', 'пятёрок', 'пятёрок',
                      'пятёрок', 'пятёрок']
    for i in range(10):
        if inp[i] == 5:
            five_count += 1
    print(f'Вы ввели {five_words[five_count]} {five_word_ends[five_count]}.')
    print('Окончание выполнения Задания 2----------------------------------------------------------\n\n')
'''
Задача 3

Вывести сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
if 3 in gl_run:
    print('Задание 3-------------------------------------------------------------------------------')
    nums = []
    nums = np.array(nums)
    for i in range(100):
        nums = np.append(nums, int(i + 1))
    print(nums)
    print(np.sum(nums))  # Решение с применением numpy
    sum = 0
    for i in range(100):
        sum += nums[i]
    print(sum)  # Решение с применением поэлементного обхода массива
    print('Окончание выполнения Задания 3----------------------------------------------------------\n\n')
'''
Задача 4

Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран(можно поискать в интернете алгоритм
факториала в python).
'''
if 4 in gl_run:
    print('Задание 4-------------------------------------------------------------------------------')
    nums = []
    nums = np.array(nums, dtype=int)
    for i in range(100):
        nums = np.append(nums, int(i + 1))
    print(nums)
    # fact=np.longdouble(1)
    fact = 1
    # fact=np.astype('int64')
    for i in range(100):
        fact *= int(nums[i])
    print(fact)  # Решение через цикл

    fact1 = math.factorial(nums[99])
    print(fact1)  # Решение через функцию factorial

    print('Окончание выполнения Задания 4----------------------------------------------------------\n\n')

'''
(!!!Подсказка на следующую задачу - превратите число в строку, а потом работайте с строкой)
Задача 5

Вывести цифры числа на каждой новой строке.

Пример:
     123567

     1
     2
     3
     4
     5
     6
     7

'''


def get_val_size(val):
    sizen = 1;
    vall = val
    cont = True
    while cont:
        vall = vall // 10
        if vall == 0:
            cont = False
        else:
            sizen += 1
    return sizen


def get_digit(val, n):
    size = get_val_size(val)
    # print(f'size: {size}')
    # print('val: ' + str(val))
    # print(f'n:{10 ** n}')
    ret = (val // (10 ** ((size - n)))) % 10
    return (ret)


if 5 in gl_run:
    print('Задание 5-------------------------------------------------------------------------------')
    var_num = 123567
    var_str = str(var_num)
    print(var_num)
    print('Вариант со строкой')
    for i in range(len(var_str)):
        print(var_str[i])
    print('Вариант с разбором разрядов цифр')
    for i in range(get_val_size(var_num)):
        print(get_digit(var_num, i + 1))

    print('Окончание выполнения Задания 5----------------------------------------------------------\n\n')

'''
(!!!Подсказка на следующие 5 задач - превратите число в строку, а потом работайте с строкой)
Задача 6

Найти сумму цифр числа.

    Пример:

    254314

    Сумма цифр числа - 19(2+5+4+3+1+4)

'''
if 6 in gl_run:
    print('Задание 6-------------------------------------------------------------------------------')
    var_num = 254314
    var_str = str(var_num)
    print(var_num)
    print('Вариант со строкой')
    res_val = 0
    res_str = ''
    init = True
    for i in range(len(var_str)):
        res_val += int(var_str[i])
        if init == False:
            res_str = res_str + '+'
        else:
            res_str = '('
            init = False
        res_str += var_str[i]
    res_str = str(res_val) + res_str + ')'
    print(res_str)

    print('Вариант с разбором разрядов цифр')
    res_val = 0
    res_str = ''
    init = True
    for i in range(get_val_size(var_num)):
        res_val += get_digit(var_num, i + 1)
        if init == False:
            res_str = res_str + '+'
        else:
            res_str = '('
            init = False
        res_str += str(get_digit(var_num, i + 1))
    res_str = str(res_val) + res_str + ')'
    print(res_str)

    print('Окончание выполнения Задания 6----------------------------------------------------------\n\n')

'''
Задача 7

Найти произведение цифр числа.

    Пример:

    254314

    Произведение цифр числа - 480(2*5*4*3*1*4)
'''

if 7 in gl_run:
    print('Задание 7-------------------------------------------------------------------------------')
    var_num = 254314
    var_str = str(var_num)
    print(var_num)
    print('Вариант со строкой')
    res_val = 1
    res_str = ''
    init = True
    for i in range(len(var_str)):
        res_val *= int(var_str[i])
        if init == False:
            res_str = res_str + '*'
        else:
            res_str = '('
            init = False
        res_str += var_str[i]
    res_str = str(res_val) + res_str + ')'
    print(res_str)

    print('Вариант с разбором разрядов цифр')
    res_val = 1
    res_str = ''
    init = True
    for i in range(get_val_size(var_num)):
        res_val *= get_digit(var_num, i + 1)
        if init == False:
            res_str = res_str + '*'
        else:
            res_str = '('
            init = False
        res_str += str(get_digit(var_num, i + 1))
    res_str = str(res_val) + res_str + ')'
    print(res_str)

    print('Окончание выполнения Задания 7----------------------------------------------------------\n\n')

'''
Задача 8

Пользователь должен ввести число. Ваш код должен дать ответ на вопрос: есть ли среди цифр числа 5?
Если есть, код должен вывексти "Цифра 5 есть в числе", в противном случае вывести: "Цифры 5 нет в числе".
'''
if 8 in gl_run:
    print('Задание 8-------------------------------------------------------------------------------')
    val = input('Введите число:')
    val_str = str(val)
    we_have_five = False
    for i in range(len(val_str)):
        if val_str[i] == '5':
            we_have_five = True
    if we_have_five == True:
        res = 'а 5 есть'
    else:
        res = 'ы 5 нет'
    print(f'Цифр{res} в числе')
    print('Окончание выполнения Задания 8----------------------------------------------------------\n\n')
'''
Задача 9

Найти максимальную цифру в числе

Пример:

    354359688

    'Цифра - 9 максимальная в числе 354359688'
'''
if 9 in gl_run:
    print('Задание 9-------------------------------------------------------------------------------')
    val = 123123
    val_str = str(val)
    max_digit = -1
    try:
        for i in range(len(val_str)):
            if int(val_str[i]) > max_digit:
                max_digit = int(val_str[i])
        print(f'Цифра - {max_digit} максимальная в числе {val_str}')
        err = False
    except:
        err = True

    if (max_digit == -1 or err == True):
        print('Что-то пошло не так... Проверьте входное число')
    print('Окончание выполнения Задания 9----------------------------------------------------------\n\n')

'''
Задача 10

Найти количество цифр 5 в числе

    Пример:

        543231235643

        'В числе 2 5-ки.'
'''
if 10 in gl_run:
    print('Задание 10-------------------------------------------------------------------------------')
    # inp = []
    # for i in range(10):
    #    inp.append(int(input('Введите цифру ' + str(i + 1) + ":")))
    val = 43554553433335554
    five_count = 0
    five_1 = 'ка'
    five_234 = 'ки'
    five_many = 'ок'
    for i in range(len(str(val))):
        if str(val)[i] == '5':
            five_count += 1
    word_end = five_many
    if five_count == 1:
        word_end = five_1
    if five_count in (2, 3, 4):
        word_end = five_234

    print(f'В числе {five_count} 5-{word_end}.')
    print('Окончание выполнения Задания 2----------------------------------------------------------\n\n')
