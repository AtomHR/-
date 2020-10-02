seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']  # времена года
seasons_dict = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август',
                9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}  # месяца
month = int(input("Введите номер месяца которого вы хотите узнать: "))  # месяц который хотят узнать
if month == 1 or month == 2 or month == 12:  # зима
    print(seasons_dict.get(month))
    print(seasons_list[0])
elif month == 3 or month == 4 or month == 5:  # весна
    print(seasons_dict.get(month))
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:  # лето
    print(seasons_dict.get(month))
    print(seasons_list[2])

elif month == 9 or month == 10 or month == 11:  # осень
    print(seasons_dict.get(month))
    print(seasons_list[3])
else:
    print("Такого месяца не существует")  # если челове ввел слишком большую/маленькую цыфру
