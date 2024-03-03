num = int(input("Введите пятизначное число :"))
a = num % 10
num = num // 10
b = num % 10
num = num // 10
c = num % 10
num = num // 10
d = num % 10
num = num // 10
e = num % 10
num = num // 10
res = a * b * c * d * e
print("Произведение цифр числа: ", res)
sum1 = a + b + c + d + e
f = sum1 / 5
print("Среднее арифметическое: ", f)
