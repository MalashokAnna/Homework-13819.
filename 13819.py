tickets_amount = int(input("Введите количество билетов:"))
age_list = [int(input("Введите возраст посетителя :")) for i in range(1, tickets_amount + 1)]
summa_money = 0
for every_age in age_list:
    if every_age < 18:
        summa_money = summa_money
    elif 18 <= every_age < 25:
        summa_money = summa_money+990
    else:
        summa_money = summa_money + 1390
print("Полная стоимость билетов:", summa_money)
if tickets_amount > 3:
    summa_money = int(summa_money*0.9)
    print("Стоимость билетов со скидкой:", summa_money)






















