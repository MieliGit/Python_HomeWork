# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

n = int(input("Введите номер билета шестизначный "))
sum1 = 0
sum2 = 0
n1 = n//1000
n2 = n%1000

while n1 > 0:
    a = n1 % 10
    sum1 = sum1 + a
    n1 = n1 // 10


while n2 > 0:
    a = n2 % 10
    sum2 = sum2 + a
    n2 = n2 // 10

if sum1 == sum2:
    print(f"{n} -> yes")
else:
    print(f"{n} -> no")

