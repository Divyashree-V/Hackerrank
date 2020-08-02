#!/bin/python3

import math
import os
import random
import re
import sys

a = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   a.append(arr_t)
    
s_list = []

def cal_sum(i,j):
    return(a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+1] + a[i+2][j] + a[i+2][j+1] + a[i+2][j+2])

for j in range(0,4):
    for i in range(0,4):
        sum = cal_sum(i,j)
        s_list.append(sum)
    
print(max(s_list))
