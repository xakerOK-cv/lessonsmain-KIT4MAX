#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов
# yjdsq

sites = {
    'Kiev': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2
distance = dict()
kiev = sites['Kiev']
london = sites['London']
paris = sites['Paris']
kiev_london = ((kiev[0] - london[0]) ** 2 + (kiev[1] - london[1]) ** 2) ** 0.5
kiev_london = round(kiev_london, 2)
kiev_paris = ((kiev[0] - paris[0]) ** 2 + (kiev[1] - paris[1]) ** 2) ** 0.5
kiev_paris = round(kiev_paris, 2)
london_paris = ((london[0] - paris[0]) ** 2 + (london[1] - paris[1]) ** 2) ** 0.5
london_paris = round(london_paris, 2)

print(kiev_london)
print(kiev_paris)

distance['Kiev'] = {}
distance['Kiev']['London'] = kiev_london
distance['Kiev']['Paris'] = kiev_paris

distance['London'] = {}
distance['London']['Paris'] = london_paris

print(distance)

# Супер чекаю на інші завдання




