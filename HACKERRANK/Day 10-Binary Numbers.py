#!/bin/python3

import math
import os
import random
import re
import sys

n = int(input().strip())
a = str(bin(n)[2:])
b = a.split("0")
max_length = 0

for i in b:
    if len(i) > max_length:
        max_length = len(i)
        
print (max_length)
