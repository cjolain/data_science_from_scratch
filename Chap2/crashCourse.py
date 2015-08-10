# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 14:57:58 2015

@author: chris
"""
from __future__ import division
from collections import defaultdict
from functools import partial

import re

my_regex=re.compile("[0-9]+",re.I)

def double (x):
    return x*2
    
def apply_to_one(f):
    return f(1)

my_double=double
#print apply_to_one(double)

y= apply_to_one(lambda x:x+4)
#print r"\t"

try:
    print 0/10
except ZeroDivisionError:
    print"lololol"

x=range(10)
#print x
zero=x[0]
nine=x[-1]
eight=x[-2]

#print x[3:-2]

x=[1,2,3]
x.extend([4,5,6])
#print x

def sum_product(x,y):
    return x+y,x*y

s,p=sum_product(4,5)
#print p

words_count=defaultdict(dict)
words_count["Joel"]["number"]="ef"
#print words_count

# Functional tools:
def exp(base,power):
    return base ** power
    
def two_to_the(power):
    return exp(2,power)


myOddList=map(lambda x:2*x,[x for x in range(1,5)])
def multiply(x,y):
    return x*y
    
products=map(multiply,[1,2],[4,5])
#print products

xs=[1,2,3,4]
multiply=reduce(multiply,xs)
#print multiply

list1=['a','b','c']
list2=[1,2,3]
a=zip(list1,list2)
print a

# means argument unpacking
letter,number=zip(*a)
print letter, number
print list(letter)

def doubler(f):
    def g(x):
        return 2*f(x)
    return g

def f1(x):
    return x+1

g=doubler(f1)
print g(-1)

def f2(x,y):
    return x+y

def magic(*args,**kwargs):
    print"unamed args: ",args
    print"keyword args: ",kwargs

magic(1,2,key="word",key3="word2")

def other_way_magic(x,y,z):
    return x+y+z

x_y_list=[1,2]
z_dict={"z":3}
print other_way_magic(*x_y_list,**z_dict)

def doubler_correct(f):
    def g(*args,**kwargs):
        return 2*f(*args,**kwargs)
    return g
g=doubler_correct(f2)
print g(1,2)
