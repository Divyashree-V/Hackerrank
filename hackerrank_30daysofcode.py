# -*- coding: utf-8 -*-
"""Hackerrank_30Daysofcode

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1re-AUvDBBrqAwxKYWtwb5wJlxobO-m0N

###**Day 0: Hello, World.**
"""

# Read a full line of input from stdin and save it to our dynamically typed variable, input_string.
input_string = input()
# Print a string literal saying "Hello, World." to stdout.
print('Hello, World.')
# TODO: Write a line of code here that prints the contents of input_string to stdout.
input=('Enter the String')
print(input_string)

"""### **Day 1: Data Types**"""

i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
n=int(input())
j=float(input())
k=str(input())
print(n+i)
print(j+d)
x=s+k
print(x)

"""### **Day 2: Operators**"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * tip_percent / 100
    tax = meal_cost * tax_percent / 100
    totalCost = meal_cost + tip + tax
    print(str(round(totalCost)))

if __name__ == '__main__':
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())
    solve(meal_cost, tip_percent, tax_percent)

"""### **Day 3:Intro to Conditional Statements**"""

#!/bin/python3

import math
import os
import random
import re
import sys

n = int(input().strip())
if n%2 != 0:
    print('Weird')
if n%2 == 0:
    if n>=2 and n<=5:
        print('Not Weird')
    if n>=6 and n<=20:
        print('Weird')
    if n>20:
        print('Not Weird')

"""### **Day 4: Class vs. Instance**"""

class Person:
    age = 0
    def __init__(self,initialAge):
        if initialAge < 0:
            print ("Age is not valid, setting age to 0.")
        else:
            self.age = initialAge
    def amIOld(self):
        if self.age < 13:
            print ("You are young.")
        elif self.age >= 13 and self.age < 18:
            print ("You are a teenager.")
        else:
            print ("You are old.")
    def yearPasses(self):
        self.age += 1
t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")

"""### **Day 5: Loops**"""

#!/bin/python3

import math
import os
import random
import re
import sys

n = int(input())

for i in range(1, 11):
    print ("{} x {} = {}" .format(n, i, n * i))

"""### **Day 6: Let's Review**"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())

for i in range(t):
    S = str(input())
    print (S[::2], S[1::2])

"""### **Day 7: Arrays**"""

#!/bin/python3

import math
import os
import random
import re
import sys

n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
a =  arr[::-1]
print (" ".join(str(x) for x in a))

"""### **Day 8: Dictionaries and Maps**"""

n = int(input())
d = dict()

for i in range(0, n):
    name, number = input().split()
    d[name] = number

for i in range(0, n):
    try:
        name = input()
        if name in d:
            print(f"{name}={d[name]}")
        else:
            print("Not found")
    except:
        break

"""## **Day 9: Recursion 3**"""

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

"""## **Day 10: Binary Numbers**"""

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

"""## **Day 11: 2D Arrays**"""

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

"""## **Day 12: Inheritance**"""

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        a = sum(self.scores) / len(self.scores)
        if a < 40:
            return "T"
        elif (40 <= a) and (a < 55):
            return "D"
        elif (55 <= a) and (a < 70):
            return "P"
        elif (70 <= a) and (a < 80):
            return "A"
        elif (80 <= a) and (a < 90):
            return "E"
        elif (90 <= a) and (a <= 100):
            return "O"
        else:
            return ""
        
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())

"""## **Day 13: Abstract Classes**"""

from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author)
        self.price = price

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        
title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()

"""## **Day 14: Scope**"""

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
     
    def computeDifference(self):
        self.maximumDifference=max(a)-min(a)
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

"""## **Day 15: Linked List**"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
        if head is None:
            head = Node(data)
        elif head.next is None:
            head.next = Node(data)
        else: 
            self.insert(head.next, data)
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head);

"""## **Day 16: Exceptions - String to Integer**"""

#!/bin/python3

import sys
S = input().strip()
try: 
    r = int(S)
    print(r)
except ValueError:
    print("Bad String")

"""## **Day 17: More Exceptions**"""

class Calculator(Exception):
    def power(self,n,p):
        if (n<0 or p<0):
            raise Calculator("n and p should be non-negative")
        else:
            return pow(n,p)

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)

"""## **Day 18: Queues and Stacks**"""

import sys
from collections import deque

class Solution:
    def __init__(self):
        self.stack = deque()
        self.queue = deque()
    
    def pushCharacter(self,char):
        self.stack.append(char)
    
    def popCharacter(self):
        return self.stack.pop()
    
    def enqueueCharacter(self,char):
        self.queue.append(char)
    
    def dequeueCharacter(self):
        return self.queue.popleft()

# read the string..........

"""## **Day 19: Interfaces**"""

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        s = 0
        for i in range(1,n+1):
            if (n%i == 0):
                s+=i
        return s
....

"""## **Day 20: Sorting**"""

#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
numberOfSwaps = 0
for i in range(0,n):
    for j in range(0, n-1):
        if (a[j] > a[j + 1]):
            temp=a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            numberOfSwaps += 1
    if (numberOfSwaps == 0):
        break
print( "Array is sorted in " + str(numberOfSwaps) + " swaps." )
print( "First Element: " + str(a[0]) )
print( "Last Element: " +  str(a[n-1]) )

"""## **Day 21: Generics**"""

#include <iostream>
#include <vector>
#include <string>

using namespace std;

template<class T>
void printArray(vector<T> v) 
{
    for(int i=0;i<v.size();i++) 
    {
        cout<<v[i]<<endl;
    }
} 
int main() {......

"""## **Day 22: Binary Search Trees**"""

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        if root is None or (root.left is None and root.right is None):
            return 0
        else:
            return max(self.getHeight(root.left),self.getHeight(root.right))+1

T=int(input()....

"""## **Day 23: BST Level-Order Traversal**"""

import sys

    def levelOrder(self,root):
        queue = [root]
        while len(queue) is not 0:
            curr = queue[0]
            queue = queue[1:]
            print(str(curr.data) + " ", end="")
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)

"""## **Day 24: More Linked Lists**"""

def removeDuplicates(self,head):
        curr = head
        while curr is not None and curr.next is not None:
            while curr.next is not None and curr.data is curr.next.data:
                curr.next = curr.next.next
            curr = curr.next
        return head

"""## **Day 25: Running Time and Complexity**"""

from math import sqrt
T = int(input())

def isPrime(n):
    for i in range(2, int(sqrt(n) + 1)):
        if n % i is 0:
            return False
    return True

for _ in range(T):
    n = int(input())
    if n >= 2 and isPrime(n):
        print("Prime")
    else:
        print("Not prime")

"""## **Day 26: Nested Logic**"""

actually = str(input()).split(" ")
d = int(actually[0])
m = int(actually[1])
y = int(actually[2])

expected = str(input()).split(" ")
de = int(expected[0])
me = int(expected[1])
ye = int(expected[2])

fine = 0
if y > ye:
    fine = 10000
elif y == ye:
    if m > me:
        fine = (m - me) * 500
    elif m == me and d > de:
        fine = (d - de) * 15
print(fine)

"""## **Day 27: Testing**"""

class TestDataEmptyArray(object):
    
    @staticmethod
    def get_array():
        return []
        # complete this function

class TestDataUniqueValues(object):
    data = []
    for i in range(5):
        data.append(i)
    data[::-1]  
    @staticmethod
    def get_array():
        return TestDataUniqueValues.data
    @staticmethod
    def get_expected_result():
        data = TestDataUniqueValues.get_array()
        return data.index(min(data))

class TestDataExactlyTwoDifferentMinimums(object):
    data = []
    for i in range(5):
        data.append(i)
    data[::-1] 
    data.insert(0,0)
    
    @staticmethod
    def get_array():
        return TestDataExactlyTwoDifferentMinimums.data
    @staticmethod
    def get_expected_result():
        data = TestDataExactlyTwoDifferentMinimums.get_array()
        return data.index(min(data))

"""## **Day 28: RegEx, Patterns, and Intro to Databases**"""

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input())
    validNamesList = []
    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        if emailID.find("@gmail.com") != -1: 
            validNamesList.append(firstName)
    for i in sorted(validNamesList):
        print(i)

"""## **Day 29: Bitwise AND**"""

import sys

t = int(input().strip())
for a0 in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    print(k-1 if ((k-1) | k) <= n else k-2)