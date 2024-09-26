# Можно обратить вспять обычный список:
seasons = ['зима', 'весна', 'лето', 'осень']

for season in reversed(seasons):
    # Переменную цикла, в которую будут передаваться элементы «перевёрнутого» списка seasons,
    # назовём season
    print(season)


for i in reversed(range(1, 13)):
    print(i, 'бомм!')

print('C новым годом!')

print('Это первый этаж.')
# Первый этаж построен, начинайте строить со второго
for i in range(2, 11):
    j = i - 1

    # Здесь вместо многоточий
    # вставьте номер текущего этажа,
    # вычислите и вставьте номер предыдущего этажа.
    print('А это', i, 'этаж, он на один выше, чем этаж', j)



bunny_counter = ''  # Создали переменную bunny_counter, её значение - пустая строка.

for i in range(1, 6):
    # На каждой итерации цикла
    # к переменной bunny_counter будет дописываться
    # очередная цифра, запятая и пробел (чтобы числа в строке не слиплись).
    # Получившееся значение будет присвоено той же переменной bunny_counter
    bunny_counter = bunny_counter + str(i) + ', '

print(bunny_counter + 'вышел зайчик погулять!')




countdown_str = ''

for i in reversed(range(0, 11)):
    countdown_str = countdown_str + str(i) + ', '

countdown_str = countdown_str + 'поехали!'

print(countdown_str)






check = (2*2 > 6)
print(check)



check = (2*2 == 4)
print(check)


for current_hour in range(24):
    if current_hour < 12:  # напишите условие здесь
        print('Доброе утро!')




for messages_count in range(0, 21):
    if messages_count == 0:
        print('У вас нет новых сообщений')
    elif messages_count == 1:
        print('У вас 1 новое сообщение')
    elif messages_count > 1 and messages_count < 5:
        print('У вас', messages_count, 'новых сообщения')
    else:
        print('У вас', messages_count, 'новых сообщений')




for current_hour in range(0, 24):
    print("На часах " + str(current_hour) + ":00.")
    # Вместо многоточий напишите код
    if current_hour < 6 :
        print('Доброй ночи!')
    elif current_hour >= 6 and current_hour < 12:
        print('Доброе утро!')
    elif current_hour >= 12 and current_hour < 18:
        print('Добрый день!')
    elif current_hour >= 18 and current_hour < 23:
        print('Добрый вечер!')
else:
    print('Доброй ночи!')