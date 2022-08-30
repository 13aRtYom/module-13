tickets = int(input("Cколько билетов покупаете? "))
a = int(input("Сколько посетителей в возрасте до 18 лет? "))
b = int(input("Сколько посетителей в возрасте от 18 до 25 лет? "))
c = int(input("Сколько посетителей в возрасте старше 25 лет? "))
sum = (a * 0) + (b * 990)+(c * 1390)
if int(a + b + c) == int(tickets):
    print("Сейчас посчитаем сумму. ")
if int(tickets) <= 3:
    print(sum)
elif int(tickets) > 3:
    print(int(sum / 100 * 90))
else:
    print("Что то пошло не так , давайте начнём сначала. ")










