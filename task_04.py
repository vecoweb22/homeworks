# Задача 4
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут
# Для того, чтобы задавать случайные значения, используйсте модуль random
# import random

import random
my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
my_time_songs = []
i = 0
while i <= 8:
    my_time_songs.extend([my_favorite_songs[i][1]])
    i = i + 1
print(
    f'Три песни звучат - {round(random.choice(my_time_songs)+random.choice(my_time_songs)+random.choice(my_time_songs), 2)} минут')

# Хорошо, можно еще вот так
# Решение 2
time = 0
for song in sample(my_favorite_songs, 3):
    print(song[0])
    time += song[1]

print(f'Три песни звучат {round(time, 2)}')
