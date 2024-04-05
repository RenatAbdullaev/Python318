# first_name = "nikolai"  # комментарий
# print("hello, " + first_name + "!")
import re
# a = 30
# b = "hello"
# c = 2.8
# print(type(a))
# print(type(b))
# print(type(c))

# a = 5
# print(a, type(a))
# b = "hello"
# print(b, type(b))
# print(str(a) + b)

# a = 5
# print(a, id(a))  # 5
# b = 4
# print(b, id(b))  # 4
# a = b  # 4
# print(a, id(a))

# a = b = c = 4
# print(a, b, c)

# a, b, c = 5, "hello", 9.2
# print(a, b, c)

# PI = 3.14
# print(PI)
# PI = 2  # нарушение соглашения
# print(PI)

# a = 21
# b = 512
# print("a:", a)
# print("b:", b)
# a, b = b, a
# # c = a  # c = 1
# # a = b  # a = 2
# # b = c  # b = 1
# print("a:", a)  # 2
# print("b:", b)  # 1

# print("строка символов строка \t\tсимволов строка \
#        символов строка символов строка символов строка \
#        символов строка символов \
#        строка символов строка символов строка символов \
#       строка символов строка символов строка символов строка символов")
# print('строка \nсимволов')

# print("документ \"file.txt\" \nнаходится по пути \rD:\\folder\\file.txt")

# s1 = "hello"
# s2 = "python"
# s3 = s1 + ", " + s2 + "!"
# print(s3)  # hello, python!
# print(s1 * 5)

# print(8748547545456786478478)
# print(4.8748547545456786478478)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 / 2)  # 3.0
# print(6 / 4)  # 1.5
#
# print(6 // 2)  # 3
# print(6 // 4)  # 1
#
# print(6 ** 2)
# print(6 % 4)
#
# number = (6 + 4) * (5 ** 2 + 7)
# print(number)  # 113
#
# num = 10
# num += 5  # num = num + 5
# print(num)  # 15
#
# num -= 3  # num = - 3
# print(num)  # 12

# num = 4321
# print(num)
# a = num % 10
# print("a:", a)
# num = num // 10
# # print(num)
# b = num % 10
# print("b:", b)
# num = num // 10
# # print(num)
# c = num % 10
# print("c;", c)
# num = num // 10
# # print(num)
# d = num % 10
# print("d", d)
# print(a * 1000 + b * 100 + c * 10 + d)


# num = 4321  # 432
# print(num)
# res = num % 10 * 1000  # 1000
# num //= 10  # num = num // 10
# res += num % 10 * 100  # 200
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print(res)

# num1 = "2.5"
# num2 = 3
# # res = num1 + str(num2)  # 23
# # print(res)
# res = float(num1) + num2  # 5
# print(res)


# print(int(2.5))
# print(round(2.51))
# print(round(2.519, 2))

# a = 2.519
# b = round(a)
# print(b, type(b))
# c = round(a, 2)
# print(c, type(c))


# name = "виктор"
# age = 28
# print("меня зовут", name, ". мне", age, "лет.")
# print("меня зовут " + name + ". мне " + str(age) + "лет.")
# print("меня зовут ", name, ". мне ", age, " лет.", end="\n\n", sep="")
# print("hello")

# name = input("введите имя: ")
# print("Hello,", name)

# num = int(input("введите число: "))  # '5'
# power = int(input("введите степень: "))  # 2
#
# # num = int(num)
# # power = int(power)
#
# res = num ** power  # 5 ** 2
# print("число", num, "в степени", power, "равно:", res)

# print("введите четыре числа: ")
# num1 = int(input("1: "))
# num2 = int(input("2: "))
# num3 = int(input("3: "))
# num4 = int(input("4: "))
# print("результат: ", round((num1 + num2) / (num3 + num4), 2))


# b1 = True
# b2 = False
# print(b1 + 5)  # 1 + 5 = 6
# print(b2 + 5)  # 0 + 5 = 5


# print(bool("python"))
# print(bool(""))  # False
# print((bool(" ")))
# print((bool(4564)))
# print((bool(-4)))
# print((bool(4.2)))
# print((bool(0)))  # False
# print((bool(0.0)))  # False
# print(bool(False))  # False
# print(bool(None))  # False
#
#
# test = None
# print(test)
# test = 5
# print(test)

# print(7 == 7)
# print(2 + 5 == 7)
# print(7 != 10 - 3)
# print(8 > 5)
# print(8 < 5)
# print(8 >= 8)
# print(8 <= 8)
# print("привет" >  "Привет")  # 1087 >  1055

# print(2 < 4 < 9)
# print(2 * 5 > 7 >= 4 + 3)  # True && True = True
# print(3 * 3 <= 7 >= 2)  # False && True => False

# a = 10
# b = 5
# c = a == b
# print(a, b, c)  # 10, 5, False

# print(5 - 3 == 2 and 1 + 3 == 4)  # True : True => True
# print(5 - 3 == 2 and 1 + 3 < 4)  # True : False => False
# print(5 - 3 == 2 and 1 + 3 == 4)  # False : True => False
# print(5 - 3 > 2 and 1 + 3 < 4)  # False : False => False

# print(5 - 3 == 2 or 1 + 3 == 4)  # True : True => True
# print(5 - 3 == 2 or 1 + 3 < 4)  # True : False => True
# print(5 - 3 == 2 or 1 + 3 == 4)  # False : True => True
# print(5 - 3 > 2 or 1 + 3 < 4)  # False : False => False


# print(not 9 - 5)  # False
# print(not 9 - 9)  # True


# cnt = 5
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
#     # pass
#     # ...
# else:
#     print("Доступ запрещен")


# a = 35
# b = 35
# if a > b:
#     print("a > b")
# if b > a:
#     print("b > a")
# if a == b:
#     print("a == b")


# a = 35
# b = 35
# if a > b:
#     print("a > b")
# elif b > a:
#     print("b > a")
# else:
#     print("a == b")

# a = input('введите первую сторону: ')
# b = input('введите вторую строну: ')
# c = input('введите третью сторону: ')
# if a == b == c:
#     print('треугольник равносторонний')
# elif a == b or a == c or b == c:
#     print('треугольник равнобедренный')
# else:
#     print('треугольник разносторонний')

# day = int(input("введите день недели (цифрой): "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5)
#     print("рабочий день -", end=" ")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("выходной день -", end=" ")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("такого дня недели не существует!")

# a = int(input("введите месяц (цифрой): "))
# if 1 <= a <= 12:
#     if 1 <= a <= 2 or a == 12:
#         print("зима")
#     if 3<= a <= 5:
#         print("весна")
#     if 6 <= a <= 8:
#         print("лето")
#     if 9 <= a <= 11:
#         print("осень")
# else:
#     print("ошибка ввода данных")
#
# a = int(input("Введите номер месяца: "))
# if 1 <= a <= 12:
#     if 3 <= a <= 5:
#         print("Весна")
#     elif 6 <= a <= 8:
#         print("Лето")
#     elif 9 <= a <= 11:
#         print("Осень")
#     else:
#         print("Зима")
# else:
#     print("Ошибка ввода данных


# n = int(input("введите кол-во ворон: "))
# if 0 <= n <= 9:
#     print("на ветке", end=" ")
#     if n == 1:
#         print(n, "ворона")
#     elif 2 <= n <= 4:  # if
#         print(n, "вороны")
#     else:  # if 5 <= n <= 9 or == 0
#         print(n, "ворон")
# else:
#     print("ошибка ввода данных")


# password = "qwerty"
#
# match password:
#     case 'admin':
#         print("администратор")
#     case 'user':
#         print("пользователь")
#     case _:
#         print("такого пользователя не существует")


# day = "четверг"
# time = 17
#
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 16:
#         print("Рабочий день")
#     case 'суббота' | 'воскресенье':
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или нерабочее время")

# a, b = 30, 20
# minim = a if a < b else b
# print(minim)

# a, b = 20, 30
# print("a == b" if a == b else "a > b" if a > b else "b > a")


# a, b = 20, 10
# print('на ноль делить нельзя' if b == 0 else a / b)


# a = 5
# b = 0
# print(a / b)

# try:
#     n = int(input("введите целое число"))
#     print(n * 2)
# except ValueError:
#     print("что то пошло не так")

# try:
#     n = int(input("введите делимое: "))
#     m = int(input("введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("нельзя делить строки")
# except ZeroDivisionError:
#     print("нельзя делить на ноль")

#
# try:
#     n = int(input("введите делимое: "))
#     m = int(input("введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("нельзя делить строки или нельзя делить на ноль")
# else:  # когда в блоке tru не возникло исключения
#     print("все нормально . вы ввели числа", n, "и", m)
# finally:  # выполнится в любом случае
#     print("конец программы")

# n = input("введите первое число: ")
# m = input("введите второе число: ")
#
# try:
#     n = int(n)  # 9
#     m = int(m)
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)


# n = input("введите первое число: ")
# m = input("введите второе число: ")
#
# try:
#     print(int(n) + int(m))
# except ValueError:
#     print(n + m)


# циклы

# i = 0
# while i < 5:
#     print("i =", i)
#     i += 1  # i = i + i

# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 2


# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print("i =", i)
#     i += 1

# n = int(input("укажите количество символов: "))  # 5
# print(n * "+-")  # +-+-+
# print(n * "+" if n % 2 == 0 else n * "-")
#
# i = 0
# while i < n:
#     print("+" if i % 2 == 0 else "-", end="")
#     # if i % 2 == 0
#     #      print("*", end="")
#     #  else:
#     #   print("_", end="")
#     i += 1
#
#     while n > 0:
#         print("*")
#         n -= 1

# a = int(input("введите начало диапазона: "))
# b = int(input("введите конец диапазона: "))

# n = int(input("введите начало диапазона: "))  # 1
# m = int(input("введите конец диапазона: "))  # 5
# sum1 = 0
# while n <= m:  # 1 <= 5
#     if n % 2:  # n % 2 != 0
#         # print(n, end=" ")
#         sum1 += n
#     n += 1
# print(sum1)

# n = input("введите целое число: ")
#
# while type(n) != int:
#     try:
#         n= int(n)
#     except ValueError:
#         print("число не целое")
#         n = input("введите целое число")
#
#
# if n % 2 == 0:
#     print("четное")
# else:
#     print("нечетное")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен!")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1


# while True:
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break

# summ = 1
# while True:
#     n = int(input("введите число: "))
#     if n == 0:
#         break
#     summ *= n
#
# print(summ)

# i = 0
# while i < 10:
#     # if i == 5:
#     #     break
#     if i == 8:
#         print(5 / 0)
#     print(i)
#     i += 1
# else:
#     print("цикл окончен, i =", i)
#
# print("код ниже")

# i = 1
# while i < 5:
#     print("внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i*j, end="\t\t")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1


# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1
# print()
# i = 0
# while i < 5:
#     print(" " * i, "*", sep="")
#     i += 1

# for element in collection:
#       print(i)

# for i in "hello!":
#     print(i)
#
# for color in "red", "blue", "green":
#     print(color)
#
# print(range(2, 9, 2))
# # range(start, stop, step), start = 0
#
# for i in range(100, 0, -10):
#     print(i, end=" ")
#
# print()
#
# i = 100
# while i > 0:
#     print(i, end=" ")
#     i -= 10

# a = int(input("введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(10, 100):  # 23
#     # if i % 11 == 0:
#     if i // 10 == i % 10:
#         print(i, end=" ")

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print("конец цикла")

# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("----")

# w = int(input("введите ширину прямоугольника: "))
# h = int(input("введите высоту прямоугольника: "))
#
# for i in range(h):  # 4
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# d = [i for i in "Hello"]
# print(d)
#
# num = [i for i in range(30) if i % 2 == 0]
# print(num)

# Список (list)

# nums = [8, 3, 9, 4, 1, "hello", True]
# print(nums)
# print(type(nums))
# print(nums[0])
# print(nums[2])
# print(nums[-1])
# print(nums[6])
# print(nums[-2])
# print(nums[-7])
# nums[1] = 256
# nums[2] += 100
# print(nums)
# # for i in nums:
# #     print(i)
# print(len(nums))

# s = [1, 3, 5]
# print(s)
# print(type(s))
#
# s1 = list("hello")
# print(s1)
# print(type(s1))
#
# s2 = s1 + s
# print(s2)
#
# s3 = s * 2
# print(s3)

# n = list(range(2, 10, 3))
# print(n)

# a = [0 for i in range(5)]
# print(a)
#
# a1 = [i ** 2 for i in range(1, 25)]
# print(a1)
#
# a2 = [i * 3 for i in "Python"]
# print(a2)

# a = [0] * int(input("введите количество элементов списка: "))
# print(a)  # [0, 0]
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)

# summ = 0
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# # for i in range(len(a)):
# #     if a[i] < 0:
# #         summ += a[i]
# for i in a:
#     if i < 0:
#         summ += i
# print(summ)

# s = list(range(10, 100, 10))
# print(s)
#
# for i in range(len(s)):
#     print(s[i], end=" ")
# print()
# for i in s:
#     print(i, end=" ")

# n = list(range(21, 41))
# print(n)
# count = s = 0
# # for i in range(len(n)):
# #     if n[i] % 2 == 0:
# #         count += 1
# #     else:
# #         s += n[i]
# for i in n:
#     if n[i] % 2 == 0:
#         count += 1
#     else:
#         s += i
# print("количество четных элементов списка", count)
# print("сумма нечетных элементов:", s)

# n = list(range(21, 41))
# print(n)
#
# a = 2
# print(n[a])
# print(n[a - 1])

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i])

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# s = count = 0
# for i in range(len(a)):
#     s += a[i]
#     if a[i] != 0:
#         count += 1
# print(s / count)


# a = [7, 9, 2, 1, 17]
# print(a)
# a[0], a[1] = a[1], a[0]
# print(a)

# срез = список[start:stop:step]
# s = [5, 9, 3, 7, 1, 8]
# print(s, id(s))
# print(s[1:3])
# print(s[::-1], id(s[::-1]))
# print(s[6:22], id(s[6:22]))

# lst = list(range(1, 8))
# print(lst[:])
# print(lst[::-1])
# print(lst[::2])
# print(lst[1::2])
# print(lst[:1])
# print(lst[6:])
# print(lst[-1:])
# print(lst[3:4])
# print(lst[4:])
# print(lst[4:1:-1])
# print(lst[2:5]

# st = "hello"
# print(st)
# print(st[::-1])
#
# a = 54, 56, 78, 99
# # print(a)
# print(a[:])
# for i in a:
#     print(i)

# методы списков dir(list)
# s = [9, 5, 6, 3, 7, 4]
# print(s)
# s.append(8)  # добавили элемент в конец списка
# # s. append("add")
# print(s)
# s.extend([20, 1, 2])  # добавили набор элементов в конец списка
# # s.extend("add")
# print(s)
# s.insert(3, 100)  # добавляет элемент (второй параметр) по заданному индексу (первый параметр)
# s.insert(20, 222)
# print(s)
# print(s[-1])

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
#
# s = []
# n = int(input("введите количество элементов списка: "))
# for num in range(n):
#     x = int(input("введите число: "))
#     if x % 2 == 0:
#         s.append(x)
#     # s.insert(0, x)
# print(s)

# s = []
# n = int(input("введите количество элементов списка: "))
# for num in range(n):
#     x = int(input("введите число: "))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x, "не делится на 3 без остатка")
# print(s)

# a = [5, 9, 2, 1, 4, 3]
# b = [4, 2, 1, 3, 7]
# c = []
#
# for i in a:  # 1
#     for j in b:  # 1
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)
#
# s = []
# for el in a:
#     if el in b and el not in s:
#         s.append(el)
# print(s)

# a = [1, 2, 3, 44, 55]
# b = [11, 22, 33]
# c = []
# if len(a) > len(b):
#     a, b = b, a
# for i in range(len(a)):  # 0 1 2
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])
# if len(b) > len(a):
#     for i in range(len(a)):  # 0 1 2
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):  # 0 1 2
#             c.append(a[i])
#             c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print(c)  # [1, 11, 2, 22, 3, 33, 44, 55]

# a = [7, 9, 2, 9, 1, 17, 9]
# print(a)
# t = a.remove(9)  # удаляет элемент по значению
# print(a)
# last = a.pop()  # удаляет последний элемент из списка и возвращает удаленный элемент
# print(last)
# second = a.pop(0)  # удаляет элемент по индексу
# print(second)
# print(a)
# a.clear()  # очищает список
# print(a)
# num = a.count(9)  # количество заданных значений в списке
# print(num)
# ind = a.index(9)  # возвращает индекс элемента по заданному значению
# print(ind)
# ind2 = a.index(9, 2, -1)
# print(ind2)

# num = 7
# if num in a:
#     print(a.index(num))


# a = [7, 9, 2, 9, 1, 17, 9]
# print(a)
# a.reverse()
# print(a)


# a = [1, 2, 3]
# b = a.copy()
# print("a =", a)
# print("b =", b)
# a.append(4)
# b.append(120)
# print("a =", a)
# print("b =", b)


# Sort - посмотреть
# a = [7, 9, 2, 9, 1, 17, 9]
# print(a)
# #  a.sort()  # сортировка элементов списка по возрастанию
# a.sort(reverse=True)  # сортировка элементов по убыванию
# print(a)

# s = ["Виталий", "Сергей", "Александр", "Анна"]
# print(s)
# s.sort(key=len, reverse=True)  # сортировка элементов по алгоритму заданной функции
# print(s)
# print(len(s))
# print(len(s[0]))

# lst = sorted(s, key=len, reverse=True)
# print(lst)
# print(s)

# генерация случайных данных

# import random

# print(random.random())
# print(random.randint(0, 9))  # 9 - включительно
# print(random.randrange(3, 9, 2))  # 9 - не включительно
# print(round(random.uniform(10.5, 25.5), 2))
# print(round(random.uniform(10.5, 25.5)))

# s = [20, 30, 40, 50, 60, 70, 80, 90, 10]
# print(s)
# # random.shuffle(s)
# print(random.choice(s))
# print(random.choices(s, k=3))

# lst = [random.randint(0, 100) for i in range(10)]
# print(lst)


# s = ['20', '30', '40', '50', '60', '70', '80', '90', '10']
# print(s)
# print(len(s))
# print(sum(s))
# print(max(s))
# print(min(s))

# s = [20, 30, 40, 50, 60, 70, 80, 90, 10]
# print(s)
# res = 0
# for i in s:
#     res = res + i
# print(res)
# print(sum(s))

#  import random
#
# lst=[random.randint(0,100) for i in range(10)]
# print(lst)
# print("Max:",max(lst))
# s=sorted(lst,reverse=True)
# print(s)

# import random
#
# lst = [random.randint(1, 100) for i in range(10)]
# print(lst)
# mux = max(lst)
# print("Max:", mux)
# lst.remove(mux)
# lst.insert(0, mux)
# print(lst)

# x = list('1a2b3c4d')
# print(x)
# print('a' not in x)
# print('e' not in x)
# s = 'c'
# if s in x:
#     print("такой элемент в списке есть")
# else:
#     print(s, "в списке отсутствует")

# lst = []
# if not lst:  # lst == []  # len(lst) == 0
#     print("список пустой")
#
# print(bool(lst))
# import random

# n1 = int(input("введите размер первого списка: "))
# n2 = int(input("введите размер второго списка: "))
# a = [random.randint(0, 10) for i in range(n1)]
# b = [random.randint(0, 10) for i in range(n2)]
# print("первый список:", a)
# print("второй список:", b)
# c = a + b
# print(c)
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print(c)

# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print(c)
# c = [min(a), min(b), max(a), max(b)]
# print(c)
# n1 = int(input("размер списка: "))
# # a = [random.randint(0, 10) for i in range(n1)]
# a = []
# while len(a) != n1:
#     n = random.randrange(n1)  # от 0 до 10
#     if n not in a:
#         a.append(n)
# print(a)

# m = [
#     [1, 2, 3, 4, 55],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12, 33, 44]
# ]
# print(m, end="\n\n")
# # # print(len(m))
# # print(m[1][2])
#
# # s = ["hello", "world"]
# # print(s[1][0])
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t\t")
#     print()
# print()
# for row in m:
#     # print(row)
#     for x in row:
#         print(x, end="\t\t")
#     print()

# m = [
#     [1, 2, 3, 4, 55],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12, 33, 44]
# ]


# for row in m:
#     for x in row:
#         print(x, end="\t\t")
#     print()
# print()
# for row in m:
#     for x in row:
#         print(x, end="\t\t")
#     print()

# w, h = 5, 3
# # matrix = [[random.randint(1, 20) for x in range(w)] for y in range(h)]
# # matrix = [[0 for x in range(w)] for y in range(h)]
# matrix = []  # [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
# for y in range(h):  # 3
#     new_row = []
#     for x in range(w):  # 5
#         new_row.append(0)  # new_row == [0,0,0,0,0]
#     matrix.append(new_row)
#
# for row in matrix:
#     for x in row:
#         print(x, end="\t\t")
#     print()

# for x, y, z in [[1, 2, 1], [3, 4, 2], [5, 6, 3], [7, 8, 4]]:
# print(z, ")", x, "+", y, "=", x + y, sep="")
# print(x[2], ") ", x[0], " + ", x[1], " = ", x[0] + x[1], sep="")

# a = int(input("Количество символов: "))
# b = str(input("Тип символа: "))
# print(" 0 - горизонтальная\n 1 - вертикальная")
# c = int(input("Ориентация линии: "))
#
# if c == 0:
#     qwe = b * a
#     print(qwe)
# elif c == 1:
#     for i in range(a):
#         print(b)
# else:
#     print("Вы задали неверную ориентацию")

# Import math

# num1 = math.sqrt(4)
# num2 = math.pi
# num3 = math.ceil(3.2)
# num4 = math.floor(3.8)
#
# print(num1)
# print(num2)
# print(num3)
# print(num4)

# import math as m
#
# num3 = m.ceil(3.2)
# num4 = m.floor(3.8)
#
# print(num3)
# print(num4)

# from math import *
#
# num3 = ceil(3.2)
# num4 = floor(3.8)
#
# print(num3)
# print(num4)


# from math import ceil, floor
#
# num3 = ceil(3.2)
# num4 = floor(3.8)
#
# print(num3)
# print(num4)

# from math import pi
#
# radius = int(input("введите радиус окружности: "))
# print("длина окружности: ", round(2 * pi * radius, 2))

# import time
# import locale
#
# locale.setlocale(locale.LC_ALL, "ru")

# second = time.time()
# print(second)
# s = 1550704510
# local_time = time.ctime()
# print(local_time)
#
# res = time.localtime()
# print(res)
# print("0" + str(res.tm_mday) if res.tm_mday < 10 else res.tm_mday, ".", res.tm_year, sep="")
#
# print(time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime(s)))
#
# print(time.strftime("Today is %B %d, %Y, %A"))

# start = time.monotonic()
# pause = 5
# print("программа запущена...")
# time.sleep(pause)
# print("пауза была", pause, "секунд")
# finish = time.monotonic()
# res = finish - start
# print(res)


# Функции
# print()
#
#
# def hello(name, age):
#     print("мне", age, "меня зовут", name)
#
#
# hello("Irina", 28)
# hello("Igor", 19)


# def get_sum(a, b):
#     print("сумма: ", end="")
#     return a + b
#
#
# n = 2
# m = 5
# # print(get_sum(n, m))
# res = get_sum(n, m)
# print(res)
# print(res + 5 - 2)
# c = 3
# d = 7
# # get_sum(c, d)

# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(maximum(9, 6))
# print(maximum(9, 16))

# def maximum(a, b):
#     if a > b:
#         return a - b
#     else:
#         return a + b
#
#
# a = int(input("введите a: "))
# b = int(input("введите b: "))
# print(maximum(a, b))

# def cub(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cub(i))


# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     end = lst.pop()  # удалили последний элемент из списка
#     start = lst.pop(0)  # удалили первый элемент
#     lst.insert(0, end)  # добавляем в начало списка
#     lst.append(start)  # добавили элемент в конец списка
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))


# def maximum(one, two):
#     if one > two:
#         return True
#     else:
#         return False
#
#
# print(maximum(9, 6))  # True
# print(maximum(9, 16))  # False
#
# if maximum(9, 6):
#     print("первое число больше второго")
# else:
#     print("второе число больше первого")

# def check_password(password):
#     has_lower = False
#     has_upper = False
#     has_num = False
#
#     for ch in password:
#         if "a" <= ch <= "z":
#             has_lower = True
#         if 'A' <= ch <= "Z":
#             has_upper = True
#         if "0" <= ch <= "9":
#             has_num = True
#
#     if len(password) >= 8 and has_lower and has_upper and has_num:
#         return True
#     return False
#
#
# p = input("введите пароль: ")
# if check_password(p):
#     print("это надежный пароль")
# else:
#     print("это ненадежный пароль")

# from random import randint
#
# w, h = 3, 4
# count = 0
# matrix = [[randint(-20, 10) for y in range(w)] for x in range(h)]
# for row in matrix:
#     for x in row:
#         print(x, end="\t\t")
#         if x < 0:
#             count += 1
#     print()
# print(count)


# def get_sum(a, b, c, d):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2))


# def set_param(c=20, s="-"):
#     print(s * c, end="")
#     print()
#
#
# set_param()
# set_param(7)
# set_param(s="#")
# set_param(15, "+")
# set_param(s="*", c=10)


# def digits_sum(n, even=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:  # even=True
#             s += cur_digit
#         if not even and cur_digit % 2:  # even=False
#             s += cur_digit
#         n //= 10  # n = // 10
#     return s
#
#
# print("сумма четных цифр: ")
# print(digits_sum(9874023))
# print(digits_sum(38271))
# print(digits_sum(123456789))
# print("сумма нечетных цифр: ")
# print(digits_sum(9874023, even=False))
# print(digits_sum(38271, even=False))
# print(digits_sum(123456789, even=False))


# def display_info(name, age):
#     print("Name:", name, "\nAge", age)
#
#
# display_info("Irina", 23)
# display_info(23, "Irina")
# display_info(age=23, name="Irina")
# display_info("Igor", age=23, name="Irina")


# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(lt1 == lt2)
# print(lt1 is lt2)
# print(id(lt1))
# print(id(lt2))
#
# a = "Hello"
# b = "Hello"
#
# a = a + "_new"
# print(a)
# print(a == b)
# print(a is b)
# print(id(lt1))
# print(id(lt2))

# lt1 = [1, 20, 3]
# print(lt1, id(lt1), id(lt1[0]), id(lt1[1]))
# lt1[1] = 50
# print(lt1, id(lt1), id(lt1[0]), id(lt1[1]))

# # неизменяемые типы данных - int, str, float, bool, tuple
# # изменяемые типы данных - list

# Кортеж (tuple) - неизменяемы список

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())  # 72 104
# print(tpl.__sizeof__())  # 48 48
# print(tpl[2])
# print(type(tpl))

# a = (5,)
# print(a, type(a))
#
# b = tuple("Hello")
# # b = tuple(["hello", "world"])
# print(b, type(b))

# a = (5, 9, 7, 3, 4)
# print(a[1:3])
# print(a[-1])
# print(a[4])

# from random import randint
#
# # tpl = tuple(i for i in range(5))
# # tpl = tuple(input("-> ") for i in range(5))
# tpl = tuple(randint(1, 100) for i in range(5))
# tpl = tuple(2 ** i for i in range(1, 13))
# print(tpl)

# t1 = tuple("hello")
# t2 = tuple("world")
# print(t1)
# print(t2)
# t3 = t1 + t2
# print(t3)
# # print(t3 * 2)
# print(t3.count("l"))
# # print(t3.index('l', 4, -2))
# sym = "l"
# # if sym in t3:
# #     print(t3.index(sym))
# # else:
# #     print("такого символа нет")
#
# try:
#     print(t3.index(sym, 4, -2))
# except ValueError:
#     print("такого символа нет в заданном диапазоне")


# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1) + 1
#             return tpl[first:second]
#             return tpl[tpl.index(el):tpl.index(el, tpl.index(el) + 1) + 1]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return tuple()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))


# t = (10, 11, [1, 2, 3], [4, 5, 6], ["hello", "world"])
# print(t, id(t))
# t[4][0] = "hi"
# t[4].append("new")
# print(t, id(t))


# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t  # распаковка картежа
# print(x, y, z)


# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# first_name, year, married = get_user()  # first_name, year
# # user = get_user()
# # first_name, year, married = user
# # print(user[0])
# # print(user[1])
# # print(user[2])
# print(first_name, year, married)


# from random import randint
#
#
# def ran(a, b):
#     return tuple(randint(a, b) for i in range(10))
#
#
# tpl1 = ran(0, 5)
# tpl2 = ran(-5, 0)
# print(tpl1)
# print(tpl2)
# tpl3 = tpl1 + tpl2
# print(tpl3)
# print("0 =", tpl3.count(0))

# name = "Igor"
#
# if name:
#     print("Name:", name)
#     name = "Marina"
# else:
#     print("ELSE")
#
#     print(name)

# name = "Igor"

# for i in range(5):
#     print(i, end=" ")
#     name = "Marina"
#
# print()
# print(name)

# name = "Igor"
#
#
# def func():
#     print("Hello")
#     name = "Marina"
#
#
# func()
# print(name)

# lst = [1, 2, 3, 4, 5]
# print(lst)
# tpl = tuple(lst)
# print(tpl)
# lst2 = list(tpl)
# print(lst2)

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6))),
# )
# print(countries, end="\n\n")
#
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана: ", country_name, ", население =", country_population, cities, sep="")
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород: ", city_name, ", население = ", city_population, sep="")


# Множество (set) - неупорядоченная коллекция, хранит только уникальные значения (изменяемый тип данных)

# s = {"red", "green", "blue", "red", "green"}
# print(type(s))
# print(s)
# print(len(s))
#
# for i in s:
#     print(i)


# a = set("hello")
# print(a, type(a))

# from random import randint
# # s = {x * x for x in range(10)}
# # s = {input("-> ") for x in range(10)}
# s = {randint(20, 50) for x in range(10)}
# print(s)


# s = {"red", "green", "blue"}
# print("green" in s)
# print("green" not in s)


# lst = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# # lt = [i for i in lst if 'a' in i]
# # lt = ['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst]
# lt = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst if i[1] == 'c'}
# print(lt)

# for i in lst:
#     if i[1] == 'c':
#         if i[0] == 'a':
#             print('A' + i[1:])
#         else:
#             print('B' + i[1:])

# s = {"red", "green", "blue"}
# print(s)
# s.add("black")  # добавление элемента
# print(s)
# s.remove("black")  # удаляет элемент (KeyError)
# print(s)
# color = "green"  # KeyError
# if color in s:
#     s.remove("color")  # удаляет элемент (KeyError)
# print(s)
# s.discard("pink")  # удаляет элемент по значению, не выбрасывает исключение, если элемента не существует
# print(s)
# color = s.pop()  # удаляет первый элемент из множества
# print(s)
# print(color)
# s.clear()  # очищает множество
# print(s)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # c = a.union(b)
# # c = a | b
# # a |= b
# # c = a & b
# # a &= b
# # c = a - b
# # a -= b
# c = a ^ b
# a ^= b
# print(c)
# print(a)

# n = 5
# m = 6
# v = n + m
# print(v)
# n += m
# print(n)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
# # s = s1.union(s2, s3, s4, s5, s6, s7)
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))

# s1 = "Hello"
# s2 = "How are you"
# a = set(s1) & set(s2)
# print(a)
# for i in a:
#     print(i, end=" ")

# drawing = {"Марина", "Женя", "Света"}
# music = {"Костя", "Женя", "Илья"}
# one_hobby = drawing ^ music
# print(one_hobby)
# both_hobbies = drawing & music
# print(both_hobbies)
# drawing = drawing - both_hobbies
# print(drawing)


# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# print(a <= b)
# print(a >= b)
# print(a < b)
# print(a > b)
# print(a != b)

# a = [9, 8, 6, 5, 8, 7, 1, 5, 5, 4, 4, 7, 8, 7, 8, 9, 5, 4]
# print(a)
# s = set(a)
# print(s)
# a1 = list(s)
# print(a1)


# s = frozenset("Hello")
# s = frozenset(["Hello", "World"])
# s = frozenset([9, 8, 5, 6, 7, 4, 2])
# print(s)

# Словари (dict)

# lst = [1, 2, 3]
# d = {"one": 1, "two": 2, "three": 3}
# print(d)
# lst[1] = 200
# d["two"] = 200
# print(lst)
# print(d)

# d = {"one": 1, "two": 2}
# print(d, type(d))
#
# d1 = dict(one=1, two=2)
# print(d1, type(d1))
#
# a = [("a", 1), ('b', 2)]
#
# d2 = dict(a)
# print(d2, type(d2))


# d = {0: "text", "one": 45, (1, 2.3): "Кортеж", "список": [2, 3, 6, 7], True: 1, False: 0, 1: "один"}
# print(d)
#
# key = "one"
# if key in d;
#     del d[key]

# try:
#     del d[key]
# except KeyError:
#     print("элемента с ключом " + str(key) + " нет в словаре")
#
# print(d)
# d["ne"] = "новое значение"
# print(d)
#
# for key in d:
#     print(key, ":", d[key])


# print("ne" in d)

# print(d["0"])
# print(d[0])
# print(d[(1, 2.3)])
# print(d[False])
# print(d[True])
# print(d[1])

# sl = {
#    'x1': 3,
#    'x2': 7,
#    "x3": 5,
#    'x4': -1
# }
# a = 1
# for key in sl:
#    a *= sl[key]
#    print(sl[key])
# print(a)

# d = dict()
# d[1] = input("-> ")
# d[2] = input("-> ")
# d[3] = input("-> ")
# d[4] = input("-> ")
# d = {i: input("-> ") for i in range(1, 5)}
# print(d)
# dislike = int(input("какой элемент исключить: "))
# del d[dislike]
# print(d)

# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core-i5-4670', 3, 8500],
#     '3': ['AMD FX-13-4330', 6, 3700],
#     '4': ['Core-13-4330', 8, 2100],
#     '5': ['Core-13-4330', 5, 6400],
# }
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], "шт. по ", goods[i][2], " руб ", sep="")
#
# while True:
#     n = input("№: ")
#     if n != "0":
#         if n in goods:
#             while True:
#                 try:
#                     count = int(input("количество: "))
#                     goods[n][1] = count
#                     break
#                 except ValueError:
#                     print("значение некорректно. введите число")
#         else:
#             print("такого ключа не существует")
#     else:
#         break
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], "шт. по ", goods[i][2], " руб ", sep="")

# d = {'a': 1, 'b': 2, 'c': 3}
# print(d)
# print(d.keys())
# print(d.values())
# print(d.items())
# for key, value in d.items():
#     print(key, "->", value)
# print(list(d.keys()))
# print(list(d.values()))
# print(list(d.items()))

# d = {'a': 1, 'b': 2, 'c': 3}
# d2 = d.copy()
#
# print("D =", d, id(d))
# print("D2 =", d2, id(d2))
#
# d['b'] = 5
# d2['e'] = 7
# print("D =", d, id(d))
# print("D2 =", d2, id(d2))

# d = {'a': 1, 'b': 2, 'c': 3}
# # print(d['b'])
# # value = d.get('b1', 'такого ключа не существует')
# # print(value)
# item = d.setdefault('c', 5)
# print(item)
# print(d)

# d = {'a': 1, 'b': 2, 'c': 3}
# item = d.pop('b', "такого ключа не существует")
# print(item)
# print(d)
# item2 = d.popitem()
# print(item2)
# print(d)
# d.clear()
# print(d)

# d = dict.fromkeys(['a', 'b'], 100)
# print(d)

# d = {'a': 1, 'b': 2, 'c': 3}
# d2 = [('r', 7), ('q', 9)]
# # d2 = {'r': 7, 'q': 9}
# # print(list(d2.items()))
# # d.update(d2)
# # d3 = d.copy()
# # d3.update(d2)
# d |= d2
# print(d)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# new_d = dict()
#
# new_d['name'] = d.pop('name')
# new_d['salary'] = d.pop('salary')
#
# print(d)
# print(new_d)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# print(d)
#
# d['location'] = d.pop('city')
#
# print(d)

# d = {'три': 3, 'один': 1, 'два': 2,  'четыре': 4}
# # new_d = {value: key for key, value in d.items()}
# new_d = {key: value for key, value in d.items() if value <= 2}
# print(new_d)

# sales = {
#     "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#     "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
#     "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#     "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451},
# }
# # print(sales)
#
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print("\t", y, ":", sales[x][y])
#
# person = input("имя: ")
# region = input("регион: ")
# print(sales[person][region])
# new_data = int(input("новое значение: "))
# sales[person][region] = new_data
# print(sales[person])

# d = {
#     'emp1': {'name': 'John', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 6500},
# }
#
# print(d['emp3'])
# print(d['emp3']['salary'])
# d['emp3']['salary'] = 8500
# #
# # for i in d:
# #     print(i)
# #     for j in d[i]:
# #         print("\t", j, ":", d[i][j])
# for i in d:
#     print(i)
#     for j, v in d[i].items():
#         print("\t", j, ":", v)


# # zip
# a = ['Dec', 'Jan', 'Feb']
# b = [12, 1, 2]
# c = (2.9, 3.7, 9.2)
# # d = dict(zip(a, b))
# d = list(zip(a, b))
# d = list(zip(b, a, c))
# print(d)
# one = {'name': "Igor", 'surname': 'Doe', 'job': 'Consultant'}
# two = {'name': "Irina", 'surname': 'Smith', 'job': 'Manager'}
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, '->', v1)
#     print(k2, '->', v2)

# lt = [('Dec', 12), ('Jan', 1), ('Feb', 2)]
# a, b = zip(*lt)
# print(a)
# print(b)

# a = [1, 2, 3]
# b = [4, *a, 5, 6]
# print(b)
# print(len(b))

# first = {'one': 1, 'two': 2}
# second = {'three': 3, 'four': 4}
# print({**first, **second})
# for k, v in {**first, **second}.items():
#     print(k, "=>", v)


# colors = ['red', 'green', 'blue']
# i = 1
# for color in colors:
#     print(i, ") ", color, sep="")
#     i += 1
# print()
# for num, val in enumerate(colors, 1):
#     print(num, ") ", val, sep="")


# studs = {}
# n = int(input("Количество студентов: "))
# s = 0
#
# for i in range(n):
#     name = input(str(i + 1) + "-й студент: ")
#     point = int(input("Балл: "))
#     studs[name] = point
#     # s += point
#
# s = sum(studs.values())
# avg = s / n
# print(studs)
# print(s)
# print("средний балл: ", avg)
#
# for i in studs:
#     if studs[i] > avg:
#         print(i)
#
# for k, v in studs.items():
#     if v > avg:
#         print(k)


# def func(*args):
#     return args
#
#
# print(func(5))
# print(func(5, 6, 7, 8, "abc"))
# print(func())

# def summa(*params):
#     print(params)
#     print(*params)
#     res = 0
#     for n in params:
#         res += n
#     return res
#
#
# print(summa(1, 2, 3))
# print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9))

# def ch(*args):
#     avg = sum(args) / len(args)
#     print(avg)
#     res = []
#     for num in args:
#         if num < avg:
#             res.append(num)
#     return res
#
#
# print(ch(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(ch(3, 6, 1, 9, 5))
# s = 1, 2, 3, 4, 5, 6, 7, 8, 9
# print(type(s))
# print(s)

# def func(a, *args):
#     return a, args
#
#
# print(func(5))
# print(func(1, 2, 3, 5, "abc"))

# def print_scores(student, *scores):
#     print("Student name:", student, end=", оценки: ")
#     for score in scores:
#         print(score, end=" ")
#     print()
#
#
# print("Jonathan", 100, 95, 88, 92, 99, 84)
# print_scores("Rick", 96, 20, 33, 66)

# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(one="один"))

# def intro(**data):
#     for k, v in data.items():
#         print(k, "is", v)
#     print()
#
#
# intro(name="Irina", surname="Sharma", age=22)
# intro(name="Igor", surname="Word", email="igor@.ru", counry="russia", age=22, phone=3333333)


# def func(a, b,*args, y=0, x=9, **kwargs):
#     return a, b, args, kwargs, y, x
#
#
# print(func(5, 1, 2, 3, 4, 6, 7, n=9, y=100, m=10))

# my_dict = {'one': 'first'}
#
#
# def db(**kwargs):
#     my_dict.update(kwargs)
#
#
# print("my_dict =", my_dict)
# db(k1=22, k2=31, k3=11, k4=91)
# print("my_dict =", my_dict)
# db(name='Bob', age=31, weight=61, eyes_color='grey')
# print("my_dict =", my_dict)

# name = "Tom"
# surname = ""
#
#
# def hi():
#     global name, surname
#     name = "Sam"
#     surname = "Johnson"
#     print("Hello", name, surname)
#
#
# def bye():
#     print("Good bye", name)
#
#
# print(name)
# hi()
# bye()
# print(name)
# print(surname)

# sum = 5
#
# lst = [9, 8, 7, 6, 5]
# print(sum(lst))

# print = "hello"
#
#
# print("Python")


# def add(a):
#     x = 2
#
#     def outer():
#         x = 3
#         print("x =", x)
#         return a + x
#
#     return outer()
#
#
# print(add(5))


# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30

# def inner():
#         nonlocal a
#         a = 35

#     inner()
#     print('a =', a)
#     t = a
#
#
# fn()
# c = x + t
# print(c)

# x = 5
#
#
# def fn1():  # 2
#     x = 25
#
#     def fn2():
#         x = 33  # 4
#
#         def fn3():
#             nonlocal x
#             x = 55  # 6
#
#         fn3()  # 5
#         print("fn2.x", x)  # 7  # 33
#     fn2()  # 3
#     print("fn1.x", x)  # 8  # 25
#
#
# fn1()  # 1
# print(x)

# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#         print(a, b)
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))


# замыкание - функция возвращает другую функцию, но не вызывает ее

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# item1 = outer(5)
# print(item1(10))
#
# item2 = outer(6)
# print(item2(10))
#
# print(outer(7)(10))
# def func(a):
#     return a * 2


# x = func(5)
# print(x)


# def func1():
#     b = 'line'
#     a = 1
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         # global a
#         c.append(4)
#         a = a + 1
#         b = b + "_new"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())


# def func(city):
#     count = 0
#
#     def inner():
#         nonlocal count
#         count += 1
#         print(city, count)
#
#     return inner
#
#
# res1 = func("Москва")
# res1()
# res1()
#
# res2 = func("Сочи")
# res2()
# res2()
# res2()
#
# res1()
# res1()
# res1()

# lambda - выражения

# print((lambda x, y: x + y)(1, 2))
# print((lambda x, y: x + y)(10, 20))
#
#
# def func(x, y):
#     return x + y
#
# # func = lambda x, y: x + y
# print(func(1, 2))


# print((lambda a, b, c: a + b + c)(10, 20, 30))
# print((lambda a, b, c=3: a + b + c)(10, 20))
# print((lambda a, b=2, c=3: a + b + c)(10))
# print((lambda a=1, b=2, c=3: a + b + c)())
#
# print((lambda *args: args)(1, 2, 3, 4, 5, 6, 7, 8))
# print((lambda *args: args)(1, 2, 3))

# c = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4,
# )
# for t in c:
#     print(t("abc_"))


# def inc1(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# func = inc1(10)
# print(func(5))
#
#
# def inc2(n):
#     return lambda x: n + x
#
#
# func2 = inc2(10)
# print(func2(5))
#
# inc3 = (lambda n: (lambda x: n + x))
#
# func3 = inc3(10)
# print(func3(5))
#
# print((lambda n: (lambda x: n + x))(10)(5))

# print((lambda n: (lambda x: (lambda z: n + x + z)))(10)(5)(1))

# def func(i):
#     return i[1]
#
#
# d = {'a': 15, 'c': 10, 'b': 5}
# # lst = sorted(d.items(), key=lambda i: i[1])
# lst = list(d.items())
# # print(lst)
# # lst.sort(key=lambda i: i[1])
# # lst.sort(key=func)
# print(lst)
# print(dict(lst))


# players = [
#     {"name": "Антон", "last_name": "Бирюков", "rating": 9},
#     {"name": "Алексей", "last_name": "Боня", "rating": 10},
#     {"name": "Федор", "last_name": "Сидоров", "rating": 4},
#     {"name": "Михаил", "last_name": "Семенов", "rating": 6},
# ]
#
# res = sorted(players, key=lambda item: item["last_name"])
# print(res)
#
# res1 = sorted(players, key=lambda item: item["rating"], reverse=True)
# print(res1)

# a = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y]
# print(a[1](8, 3))
# print(a[0](8, 3))

# d = {
#     1: lambda: print("Понедельник"),
#     2: lambda: print("Вторник"),
#     3: lambda: print("Среда"),
#     4: lambda: print("Четверг"),
#     5: lambda: print("Пятница"),
#     6: lambda: print("Суббота"),
#     7: lambda: print("Воскресенье"),
# }
#
# d[6]()
# from math import pi
#
# area = {
#     "Circle": lambda radius: pi * radius * radius,
#     "Rectangle": lambda a, b: a * b,
#     "Trapezoid": lambda a, b, h: (a + b) * h / 2
# }
#
# print("площадь окружности:", area["Circle"](2))
# print("площадь прямоугольника:", area["Rectangle"](10, 13))
# print("площадь трапеции:", area["Trapezoid"](7, 5, 3))

# print((lambda a, b: a if a > b else b)(5, 10))
# print((lambda a, b: a if a > b else b)(15, 10))


# def outer(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
#
# print(outer(2, 4, 6))
# print(outer(5, 8, 2))
# print(outer(1, 6, 8))


# s - глобальная переменная
# s = 0
#
#
# def outer(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     global s
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
#
# outer(2, 4, 6)
# print(s)
# outer(5, 8, 2)
# print(s)
# outer(1, 6, 8)
# print(s)


# нелокальная переменная
# def outer(a, b, c):
#     s = 0
#
#     def inner(i, j):
#         nonlocal s
#         s += i * j
#
#     inner(a, b)
#     inner(a, c)
#     inner(b, c)
#     return 2 * s
#
#
# print(outer(2, 4, 6))
# print(outer(5, 8, 2))
# print(outer(1, 6, 8))

# print("вносим изменения")

# print("Данные переносим на GitHub")

# map (func, iterable), filter(func, iterable)

# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
#
# # lst2 = list(map(mult, lst))
# lst2 = list(map(lambda t: t * 2, lst))
# print(lst2)

# lst2 = (list(map(lambda t: t * 2, [2, 8, 12, -5, -10])))

# t = (2.88, -1.75, 100.55)
#
# # t2 = tuple(map(lambda x: int(x), t))
# t2 = tuple(map(int, t))
# print(t2)

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# res = dict(map(lambda x, y: (x, y), num, st))
# print(res)

# st = [1, 2, 3]
# num = [1, 2, 3]
#
# res = list(map(lambda x, y: x + y, st, num))
# print(res)

# def func(s):
#     return len(s) == 3
#
#
# t = ('abcd', 'abc', 'asdfg', 'def', 'ert')
#
# # t2 = tuple(filter(lambda s: len(s) == 3, t))
# # t2 = tuple(filter(func, t))  # t2 = ('abc', 'def', 'ert'
# print(t2)

# b = [60, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)

# from random import randint
#
# lst = [randint(1, 40) for i in range(10)]
# print(lst)
#
# lst2 = list(filter(lambda t: 10 <= t <= 20, lst))
# print(lst2)


# m = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10))))
# print(m)
#
# m1 = [x ** 2 for x in range(10) if x % 2]
# print(m1)


# Декораторы

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# def super_func(func):
#     print("Hello, I am func 'super_func'")
#     print(func())
#
#
# super_func(hello)

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# test = hello
# print(test())

# def my_decorator(func):
#     def inner():
#         print("Code before")
#         func()
#         print("Code after")
#
#     return inner
#
#
# def func_test():
#     print("Hello, I am func 'func_test'")


# test = my_decorator(func_test)
# test()


# def my_decorator(func):  # декорирующая фуекция
#     def inner():
#         print("*" * 40)
#         func()
#         print("=" * 40)
#
#     return inner
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print("Hello, I am func 'func_test'")
#
#
# @my_decorator
# def hello():
#     print("Hello, I am func 'hello'")
#
#
# func_test()
# hello()

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @bold
# @italic
# def hello():
#     return "text"
#
#
# print(hello())

# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("вызов функции:", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()
# hello()
# hello()
# hello()
# hello()
# hello()
# hello()


# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print("данные:", arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(name, surname):
#     print("меня зовут", name, surname)
#
#
# print_full_name("ирина", "ветрова")


# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("args:", args)
#         print("kwargs:", kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study, "\n")
#
#
# print_full_name("Ирина", "Борис", "Светлана", study="JavaScript")
# print_full_name("Владимир", "Екатерина", "Виктор")

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# @decor("Произведение:", "*")
# def mul(a, b):
#     print(a * b)
#
#
# n = 5
# m = 2
# summa(n, m)
# sub(n, m)
# mul(n, m)

# def multiply(arg):
#     def decor(fn):
#         def wrap(*args, **kwargs):
#             return arg * fn(*args, **kwargs)
#
#         return wrap
#     return decor
#
#
# @multiply(3)
# def return_num(num):
#     return num


# print(return_num(5))

# def avg(fn):
#     def wrap(*args):
#         return fn(*args) / len(args)
#
#     return wrap
#
#
# @avg
# def summa(*args):
#     return sum(args)
#
#
# print(summa(2, 3, 3, 4))


# Строки

# print(0x10)
# print(bin(18))  # 0b10010 => 0b - двоичная система
# print(oct(18))  # 0o22 => - восьмеричная
# print(hex(18))  # 0x12 => 0x - шестнадцатеричная
#
# print(0b10010 + 0o22)
# print(0o22)
# print(0x12 + 0o22)

# q = 'Pyt'
# w = "hon"
# e = q + w
# # print(e)  Python => Pytton
# # print(e * 3)
# # print("y" in e)
# # print("l" in e)
# # print(e[1])
# # print(e[-1])
# # print(e[::-1])
# e = e[:3] + 't' + e[4:]
# print(e)

# print("Привет")
# print(u"Привет")

# print("C:\\folder\\file.txt")
# print(r"C:\folder\file.txt")
# print(r"C:\folder\\[:1]")
# print("C:\\folder" + "\\")
# print("C:\\folder\\")

# name = "Дмитрий"
# age = 25
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print(f"Меня зовут {name}. Мне {age} лет)"
# print(a)
# print(f"число: {round(12.2564, 2)}, {5 + 3}")
# print(f"число: {12.2564:.2f}")

# x = 10
# y = 5
# print(f"{x=}, {y=}")
# print(f"{x} x {y} / 2 = {x * y / 2}")

# dir_name = "folder"
# file_name = "file.txt"
# print(fr"home\{dir_name}\{file_name}")
# print("home"+ "\\" + dir_name + "\\" + file_name)

# s = """стр  ока
# символов"""
# print(s)
# s1 = '''стр ока
# символов'''
# print(s1)
# s2 = ("стро ка "
#       "символов")
# print(s2)

# def square(n):
#     """Принимаем число n, возвращает число n"""
#     print("hello")
#     return n ** 2
#
#
# print(square(5))

# from math import pi
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра
#
#     Вычисляет площадь на основании заданной высоты и радиуса основания

#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# # print(cylinder.__doc__)
# print(sum.__doc__)
# print(len.__doc__)
# print(int.__doc__)
# print(type.__doc__)

# print(ord('а'))
# print(ord('й'))

# while True:
#     n = input("->")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break

# st = "Test string for me"
# arr = [ord(x) for x in st]
# print("ASCII коды:", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое", arr)
# arr += [ord(x) for x in input("-> ")[:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)


# print(chr(97))
# print(chr(35))
# print(chr(8364))

# a = 122
# b = 97
# if a > b:
#     for i in range(b, a + 1):
#         print(chr(i), end=" ")
# else:
#     for i in range(a, b + 1):
#         print(chr(i), end=" ")
# if b > a:
#     a, b = b, a
#
# for i in range(b, a + 1):
#     print(chr(i), end=" ")


# print("apple" == "Apple")
# print("apple" > "Apple")

# from random import randint
#
# min_ascii = 33
# max_ascii = 126
# shortest = 6
# longest = 16
#
#
# def random_password():
#     res = ""
#     for i in range(randint(shortest, longest)):
#         res += chr(randint(min_ascii, max_ascii))
#     return res
#
#
# print("ваш случайный пароль:", random_password())

# Методы строк

# s = "hello, WORLD! I am learning Python."
# print(s)
# a = s.capitalize()
# print(a)  # Hello, world! i am learning python.
# print(s.lower())  # hello, world! i am learning python.
# print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON.
# print(s.count('l'))
# print(s.lower().count('l'))

# print(s.count('h', 1, -4))
# print(s.count('h'))

# print(s.find("Python"))  # поиск подстроки в строке, возвращает индекс совпадения, если совпадение нет вернет "-1"
# print(s.index("Python"))  # поиск подстроки в строке, возвращает индекс совпадения, если совпадение нет вернет
# исключение "ValueError"

# print(s.find("h", 1, -4))
# print(s.rfind("h1"))
# print(s.rindex("h1"))

# st = input("введите два слова через пробел: ")  # "один два"
# first = st[:st.find(" ")]
# second = st[st.find(" ") + 1:]
#
# print(second + " " + first)


# s = "hello, WORLD! I am learning Python."
# print(s)
#
# print(s.endswith("on."))  # заканчивается ли строка на заданную подстроку -> (True, False)
# print(s.startswith("I am", 14))  # заканчивается ли строка на заданную подстроку -> (True, False)
# print(s.find("I am"))


# a = input("введите число: ")
# try:
#     a = int(a)
#     print(a ** 2)
# except ValueError:
#     print("нужно ввести число")

# print('123'.isdigit())  # состоит ли строка только из чисел
# print('123a'.isdigit())
#
# a = input("введите число: ")
# b = 2
# if a.isdigit():
#     a = int(a)
#     print(a + b)
# else:
#     print(a + str(b))


# print("abc123".isalnum())  # состоит ли строка только из букв и цифр
# print("ABCabc".isalpha())  # состоит ли строка только из букв


# print("abc123!@#".islower())  # определяется, являются ли буквенные символы строки в нижнем регистре
# print("ACV123!@#".islower())  # определяется, являются ли буквенные символы строки в верхнем регистре

# print('py'. center(10))
# print('py'. center(10, "-"))
# print('py'. center(1))


# print("    p   y     ".lstrip())
# print("    py     ".rstrip())
# print("    py     ".strip())
#
# print("https://www.python.orgw".lstrip("/:pthsw"))
# print("https://www.python.orgw".strip("/:pthsw"))
# print("https://www.python.orgw".lstrip("/:pths").rstrip("w"))

# s = "hello, Python! I am learning Python. Python"
# print(s.replace("Python", "Java", 2))  # поиск и замена

# s = "-"
# seq = ("a", "b", "c")
# print(s.join(seq))
#
# print("..".join(['1', '2']))  # объединяет итерируемый объект в строку через символ разделитель
#
# print(":".join("Hello"))

# print("a b c".split())
# print("www.python.org".split(".", 1))
# print("www.python.org".rsplit(".", 1))

# Регулярные выражения

# import re

# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта."
# reg = r"\."
# print(re.findall(reg, s))  # возвращает список, содержащий все совпадения с шаблоном
# print(re.search(reg, s))  # возвращает первое совпадения с шаблоном
# # print(re.search(reg, s).span())
# # print(re.search(reg, s).start())
# # print(re.search(reg, s).end())
# # print(re.search(reg, s).group())
# print(re.match(reg, s))  # возвращает по шаблону в начале строки
# print(re.split(reg, s, 3))  # возвращает список, в котором строка разбита по шаблону
# print(re.sub(reg, "!", s, 1))  # поиск и замена

# s = r"Я ищу совпадения в 2024 году. И я и^х найду в 2 счё_та. [1938765]. Hel-lo"
# reg = r"[204]"
# reg = r"[0-9]"
# reg = r"[А-яЁё]"
# reg = r"[A-Za-z9.[\]-]"
# reg = r"[^0-9]"
# reg = r"[12][0-9][0-9][0-9][0-9]"  # 20[00] 19[00]
# print(re.findall(reg, s))
# print(ord("Ё"))  # 1025
# print(ord("А"))  # 1040
# print(ord("Я"))  # 1071
# print(ord("а"))  # 1072
# print(ord("я"))  # 1103
# print(ord("ё"))  # 1105
# print(chr(96))

# st = "Час в 24-часовом формате от 00 до 23. 2021-06-15T21:59. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09."
# pattern = "[0-2][0-9]:[0-5][0-9]"
# print(re.findall(pattern, st))

# s = r"Я ищу совпадения в 2024 году. И я и^х найду в 2 счё_та."
# reg = r"\d"  # [0-9]
# reg = r"\D"  # [^0-9]
# reg = r"\s"  # [ ]
# reg = r"\S"  # [^ ]
# reg = r"\w"  # [0-9A-zА-я]
# reg = r"\W"  # [^0-9A-zА-я]
# reg = r"\АИ я"
# reg = r"году.\Z"
# reg = r"\Вния"
# reg = r"\w+"
# reg = r"\d+"
# reg = r"20*"
# print(re.findall(reg, s))
# кол-во повторений
# + - от 1 до бесконечности
# * - от 0 до бесконечности
# ? - от 0 до 1

# d = "Цифры: 7, +17, --42, 0013, 0.3456"
# print(re.findall(r"[+-]?\d+[.\d]*", d))

# st = "05-06-1987 # Дата рождения"
# print("Дата рождения:", re.sub(r"\s#.*", "", st))
# # Дата рождения: 05-06-1987 => Дата рождения: 05.06.1987
# print("Дата рождения:", re.sub(r"-", ".", re.sub(r"\s#.*", "", st)))

# st = "author=Пушкин А.C.; title = Евгений Онегин; price =200; year= 1831"
# # pattern = r"\w+\s*=\s*[\w\s.]+"
# pattern = r"\w+\s*=\s*[^;]+"
# print(re.findall(pattern, st))


# s1 = "12 сентября 2024 года 4567897"
# reg1 = r"\d{2,4}"
# print(re.findall(reg1, s1))


# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счё_та."
# # reg = r"^\w+\s\w+"
# reg = r"^\w+\s\w+\.$"
# print(re.findall(reg, s))

# def valid_login(name):
#     return re.findall("^[A-Za-z0-9_-]{3,16}$", name)
#
#
# print(valid_login("Python_master"))
# print(valid_login("Python"))


# print(re.findall(r"\w+", "12 + й"))
# print(re.findall(r"\w+", "12  + й", flags=re.ASCII))

# text = "Hello World"
# print(re.findall(r"\w\+", text, re.DEBUG))


# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта."
# reg = "я"
# print(re.findall(reg, s, re.IGNORECASE))

# text = """one # Комментарий two"""
#
# # print(re.findall(r"one.\w+", text))
# # print(re.findall(r"one.\w+", text, re.DOTALL))
# print(re.findall(r"one.\w+", text, re.MULTILINE))

# print(re.findall("""
# [a-z.-]+  # part 1
# @         # @
# [a-z.-]+  # part 2
# """, "test@mail.ru", re.VERBOSE))

# import re
#
# text = """Python,
# python,
# PYTHON"""
# reg = "(?im)^python"
# print(re.findall(reg, text))


# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall("<.*?>", text))


# *?, +?, ??
# {m,n}?, {,n}?, {m,}?

# s1 = "12 сентября 2024 года 4567897"
# reg1 = r"\d{3,}?"
# reg1 = r"\d{3}"
# print(re.findall(reg1, s1))

# s = "петр и виталий отлично учатся"
# reg = r"ольга|виталий"
# print(re.findall(reg, s))


# s = "int = 4, float = 4.0f, double = 8.0, float"
# # reg = r"int\s*=\s*[.\w+]*|float\s*=\s*[.\w+]*"
# # reg = r"(?:int|float)\s*=\s*[.\w+]*"
# reg = r"((?:int|float)\s*=\s*([.\w+]*))"
# print(re.findall(reg, s))
# # print(re.search(reg, s))

# (?:...) - обозначает, что эта группирующая скобка является не сохраняющей

# s = "5 + 7*2 - 4"
# reg = r"\s*([+*-])\s*"
# print(re.split(reg, s))

# a = "28-08-2021"
# pattern = r"(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19\d\d|20[0-9][0-9])"
# print(re.findall(pattern, a))
# print(re.search(pattern, a).group(2))
# m = re.search(pattern, a)
# print(m[0])
# print(m[1])
# print(m[2])
# print(m[3])


# s = "самолет прилетает 10/23/2024. будем рады вас видеть после 10/24/2024."
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# print(re.sub(reg, r"\2.\1.\3", s))

# s = "yandex-98.ru.com and yandex.ru"
# reg = r"(([a-z0-9-]{2,}\.)+[a-z]{2,4})"
# print(re.sub(reg, r"http://\1", s))

# Рекурсия

# def elevator(n):
#     if n == 0:
#         print("вы в подвале")
#         return
#     print("=>", n)
#     elevator(n - 1)
#     print(n, end=" ")
#
#
# n1 = int(input("на каком вы этаже: "))
# elevator(n1)
# elevator(n1)


# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += 1
#     return res

# def sum_list(lst):
#     if len(lst) == 1:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0]
#     else:
#         print(lst, "=>[0]:", lst[0])
#         return lst[0] + sum_list(lst[1:])
#
#
# print(sum_list([1, 3, 5, 7, 9]))

# def to_str(n, base):
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]
#
#
# print(to_str(17, 16))

# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# names = ['Adam', ['Bob', ['Chat', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], "Ann"]
# print(names)
# print(len(names))
# # print(isinstance(names, list))
# # print(isinstance(names[0], list))
# # print(isinstance(names[1][1][0], list))
# print(count_items(names))


# def remove(text):
#     if not text:
#         return ""
#     if text[0] == "\n" or text[0] == " ":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
#
# print(remove(" Hello\nWorld "))

