# This is a sample Python script.
from typing import Union, Any


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Izlen Umut Egeli PyCharm')


# import sys
# x = sys.argv[1]
# print(int(x) + 3)

# a = 5
# b = 6
# print(a, b)
# a, b = b, a
# print(a, b)
# number = input ('number =')
# x = int(number)
# x = 12
# if x < 10:
#    print(f' {x} is less than 10 ')
# elif x > 10:
#    print(f" {x}  is bigger than 10 ")
# else:
#    print(f" {x} is equal to 10 ")

# print(x)
# i = 1
# while i <= 5:
#    print('IZLEN')
#    j = 1
#   while j <= i:
#        print('ROCKS ', end="")  # print on the same line
#        j += 1
#    i += 1
#    print()  # new line
# print('End!')
# for i in [1, 'cat', 3.0]:
#    print(f" list is {i} ", end="")
# print()
# print("HEYOOO")
# for i in {3, 8, 'anne', 9, 3}:
#    print(f'cluster  {i}')
# a = {3: 'izlen', 8: 'inci', 4: 'anne'}
# for i in a.values():
#    print(i)
# from array import *

# first = array('i', [1, 4, 6, -5])
# x = array(first.typecode, (a * 3 for a in first))
# print(first)
# print(x)
# for j in x:
#    print(j)
# izlen = 3
# val = izlen
# izlen = array('i', [3, 5, 7, 9])
# for i in izlen:
#    print(i)
# print('boy: ', len(x))
# print(izlen.typecode)
# print(izlen.index(9))
# from numpy import *

# arr = array([1, 2, 3, 4, 5])
# print(arr)
# print(id(arr))
# arr1 = arr.copy()
# print(id(arr))
# print(id(arr1))
# arr[1] = 9
# print(arr)
# print(arr1)


# def gret(x, y):
#    c = x * y
#    d = x - y
#    return c, d


# result1, result2 = gret(3, 6)

# print(f'result1 = {result1}  result2 = {result2}')
# print(result1, "   ", end="")
# print(result2)


# def arti(z):
#    print(id(z), 'z=', z)
#    z[1] = 35
#    print(id(z), 'z1=', z)


# y= 1
# print(id(y), 'y=', y)
# arti(y)
# print(id(y), 'y1=', y)

# lst = [1, 3, 6]
# print(id(lst), 'lst=', lst)
# arti(lst)
# print(id(lst), 'lst=', lst)
# dic = {1: 'izlen', 2: 'kitap'}
# for i, j in dic.items():
#    print(i, j)


def fac(k):
    number = 1
    for i in range(k):
        number = number * (i + 1)
        print(number)
    return number


fac_number = fac(5)
print(fac_number)


def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


result = fact(5)
print('recursion ', result)

num = 0


def fact1(n):
    global num
    if n == 0:
        return 1
    num = num + 1
    return fact1(n - 1)


fact1(5)
print(" fact1 ", num)

is_even = lambda a: a % 2 == 0

nums = [2, 5, 8, 9, 4]

evens = list(filter(is_even, nums))
print(evens)

fruit = ["Apple", "Cherry"]
map = map(lambda s: s[0] == "A", fruit)

print(list(map))

fruit = ["Apple", "Cherry"]
fil = filter(lambda s: s[0] == "A", fruit)

print(list(fil))

from functools import reduce

list = [2, 4, 7, 3]
print(reduce(lambda a, b: a + b, list, 10))


def add1(d):
    d += 1
    x = d
    return d


def add1caller(function):
    x = 5
    return function(x)


all = add1caller(add1)
print(all)


def div(a, b):
    print(a / b)
    return a / b


def smart_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)

    return inner


div1 = smart_div(div)
print("sonuc", div1(2, 4))

from Calc import *

print("calc module ", addition(3, 6))


class CellPhone:
    def __init__(self, k, l):
        self.number1 = k
        self.number2 = l
        print(self.number1, " ", self.number2)

    def facetime(self):
        print("visual talk")
        print(self.number1, " ", self.number2)


a1 = CellPhone(3, 8)
CellPhone.facetime(a1)
a1.facetime()


def plus_one(number):
    def add_one(number):
        return number + 1

    result = add_one(number)
    return result


plus_one(5)


def plus_one(number):
    return number+1


def function_caller(function):
    number_to_add = 5
    return function(number_to_add)


function_caller(plus_one)

print("without paramater: ", plus_one(2))

def hello_function():
    def say_hello():
        print("Hi")
    return say_hello


hello = hello_function()
print(type(hello))
print(hello)
hello()

def print_message(message):
    def message_sender():
        print(message)
    message_sender()

print_message("14 Mayis")

def uppercase_decorator(function):
    def wrapper():
        func = function()
        print(type(func), func)
        make_uppercase = func.upper()
        print("make ",type(make_uppercase),make_uppercase)
        return make_uppercase
    print(type(function))
    print( "wrapper", type(wrapper))
    return wrapper


@uppercase_decorator
def say_hi():
    return 'hello there'

#decorate = uppercase_decorator(say_hi)
#print ("decorate", type(decorate), decorate)
#print(decorate())
print("IZLEN")
print("IZLEN",say_hi())
i = 5
print(type(i))


def say_name_decorator(function):
    def wrapper():
       func = function()
       print("EGELI", func)

    return wrapper

def say_name():
    print("hi")

say_name()


decorate = say_name_decorator(say_name)
print("wrapper")
decorate()

class School:
    school_name = "NAMIK KEMAL ORTA OKULU"

    def __init__(self,name,fcontact,basari):
        self.name_student = name
        self.familycontact = fcontact
        self.basari_ortalamasi = basari
        self.lap= self.laptop()

    class laptop:
        def __init__(self):
            self.cpu = "i5"


    def get_name(self):
        return self.name_student

    def change_name(self, nname):
        self.name_student = nname

    @classmethod
    def get_school_name(cls):
        return cls.school_name

    @staticmethod
    def zilcal():
        print(" Zil Cal")


student1 = School("IZLEN","INCI 05442865120","COK BASARILI")
print(student1.get_name(),student1.familycontact,student1.basari_ortalamasi)
print(School.school_name)
print(student1.school_name)
School.zilcal()
print("inner class",student1.lap.cpu)
print(type(student1.lap))
print(type(student1))
print(type(School))
print(type(student1.lap.cpu))

student2 = School("tombik","izlen","cok basarili")
print("first",student2.name_student)

student2 = student1

print("second",student2.name_student)
print(student1.lap.cpu)
s1 = student1.lap
print(type(s1))
print(type(student1.lap))

lap1 = School.laptop()
print("lap1",type(lap1))

from abc import ABC, abstractmethod

class Shape(ABC):
#class Shape():
    def __init__(self, shape_name):
        self.shape_name = shape_name

    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def __init__(selfself):
        super().__init__("circle")

    def draw (self):
        print("Drawing a circe")

circle = Circle()
circle.draw()


class Egeli:
    def __init__(self):
        i = 10

    def deneme(self):
        print(type(self))
        print(id(self))

a1 = Egeli()
a1.deneme()


a3 = [1, 3, 5, 9]
ita3 = iter(a3)
print(ita3)
print(id(ita3))
print(next(ita3))
print(next(ita3))
for i in a3:
    print(i)

print("yenisi",next(ita3))

f = open('MyData.jpg', 'ab')
#f.write('IZLEN UMUT EGELI')

f1 = open('2.jpg','rb')
for i in f1:
    f.write(i)

def search(l, n):

    i=0
    while i<len(l):
        if l[i] == n:
            pos = i
            globals()['glo'] = 9
            return True, pos
        i+=1
    return False, -1
glo= 3
l= [1, 4, 6, 8]
b,pos = search(l, 4)
if b:
    print("found",pos,glo)
else:
    print("not found")

k = [3,9,5,1,8]
print(k)
k.sort()
print(k)
l=0
u=len(k)
n= 1
def ysearch(k,n):
  k.sort()
  l= 0
  u=len(k) - 1

  while l <= u:
    m= (u+l)//2
    if k[m] == n:
       return m
    else:
       if n > k[m]:
           l = m + 1
       else:
           u = m - 1
  return -1

k =[2,5,7,10]
print("pos",ysearch(k, 10))

p= [33,3,55,5]
print(p)
for j in  range ((len(p) - 1),0,-1):
   for i in range(j) :
      if p[i] > p[i+1]:
        p[i], p[i+1] = p[i+1], p[i]

print("sorted",p)
g = [44, 88,2, 9]
print(g)
for i in range (len(g) - 1):
   minpos = i
   for j in range (i,len(g) - 1,1):
      if g[j+1] < g[minpos]:
          minpos = j+1
   g[i],g[minpos] = g[minpos], g[i]
   print(g)

print("selection sort",g)





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
