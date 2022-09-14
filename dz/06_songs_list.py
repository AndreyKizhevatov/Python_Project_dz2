#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точносттю до долей минут

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ минут
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)

a = violator_songs_list[3][1]
b = violator_songs_list[5][1]
c = violator_songs_list[8][1]
three_songs1 = round(a+b+c,2)
print('Первый список трех песен:',three_songs1)

# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат ХХХ минут

d = violator_songs_list[1][1]
e = violator_songs_list[6][1]
f = violator_songs_list[7][1]
three_songs2 = round(d+e+f,2)
print('Второй список трех песен:',three_songs2)

g = violator_songs_list[0][1]
i = violator_songs_list[2][1]
h = violator_songs_list[4][1]
three_songs3 = round(g+i+h,2)
print('Третий список трех песен:',three_songs3)


