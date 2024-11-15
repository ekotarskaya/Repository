money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months = 0  # Счетчик месяцев
current_capital = money_capital  # Текущая финансовая подушка

# Цикл расчета количества месяцев
while current_capital + salary >= spend:
    months += 1
    # Обновляем текущий капитал: добавляем зарплату, вычитаем расходы
    current_capital += salary - spend
    # Увеличиваем расходы на 5% (рост цен)
    spend *= 1 + increase

print("Количество месяцев, которое можно протянуть без долгов:", months)
