#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# TODO виконав

radius = 42


pi = 3.1415926
S = pi * radius**2
print(round(S,4))


point = (23, 34)


point_0 = (0, 0)
distance = ((point[0] - point_0[0])**2 + (point[1] - point_0[1])**2)**0.5
print(distance < radius)

point_2 = (30, 30)

distance_1 = ((point_2[0] - point_0[0])**2 + (point_2[1] - point_0[1])**2)**0.5
print(distance_1 < radius)
