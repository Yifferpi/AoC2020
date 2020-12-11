#! /usr/bin/env python3

import numpy as np
from scipy.signal import convolve2d

switch = {'L':0, '.':(-1), '#':1}
kernel = np.array([[1,1,1],[1,0,1],[1,1,1]])

def init():
    rows = open("input.txt", 'r').read().split('\n')[0:-2]
    shape = (len(rows), len(rows[0]))
    arr = np.zeros(shape)
    for i in range(0, shape[0]):
        for j in range(0, shape[1]):
            arr[i][j] = switch.get(rows[i][j])
    return arr

def run(f):
    oldarr = init()
    newarr = f(oldarr)
    while not np.array_equal(newarr, oldarr):
        oldarr = newarr
        newarr = f(oldarr)
    newarr[newarr < 0] = 0
    return np.count_nonzero(newarr)

#=====Part 1=====
def part1(arr):
    tmp = np.copy(arr)
    tmp[tmp < 0] = 0
    tmp = convolve2d(tmp, kernel, 'same')
    res = np.copy(arr)
    res[tmp == 0] = 1
    res[tmp > 3] = 0
    res[arr == (-1)] = -1
    return res

#=====Part 2=====
def bounds(arr, i, j):
    x, y = arr.shape
    if (i < 0) or (i >= x):
        return False
    if (j < 0) or (j >= y):
        return False
    return True

def checkOcc(arr, direction, i, j):
    dx, dy = direction
    x, y = i + dx, j + dy
    while bounds(arr, x, y):
        if arr[x][y] == (-1):
            x, y = x + dx, y + dy
            continue
        return arr[x][y]
    return 0

def comp(arr, i, j):
     if arr[i][j] == (-1):
         return -1
     directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
     num = 0
     for d in directions:
         num = num + checkOcc(arr, d, i, j)
     if num > 4:
         return 0
     if num == 0:
         return 1
     return arr[i][j]

def part2(arr):
    tmp = np.empty(arr.shape)
    for i in range(0, arr.shape[0]):
        for j in range(0, arr.shape[1]):
            tmp[i][j] = comp(arr, i, j)
    return tmp

print(run(part1))
print(run(part2))
