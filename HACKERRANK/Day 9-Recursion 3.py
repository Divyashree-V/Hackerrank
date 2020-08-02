#!/bin/python3

import math
import os
import random
import re
import sys

N = int(input())

def factorial(x):
    if x == 0:
        return 1
    return x * factorial(x - 1)

print (factorial(N))
