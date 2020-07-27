# coding=utf-8
A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5))) # {'a': 1, 'b':2, 'c':3, 'd':4, 'e':5}
print(A0)
A1 = range(10) # range object(0,10) for python 3 -OR- [0,1,2,3,4,5,6,7,8,9] in python2.7
print(A1)
A2 = sorted([i for i in A1 if i in A0]) # []
print(A2)
A3 = sorted([A0[s] for s in A0]) # [1,2,3,4,5]
print(A3)
A4 = [i for i in A1 if i in A3] # [1,2,3,4,5]
print(A4)
A5 = {i:i*i for i in A1} # {0:0, 1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49, 8:64, 9:81}
print(A5)
A6 = [[i,i*i] for i in A1] # [[0,0], [1,1], [2,4], [3,9], [4,16], [5,25], [6,36], [7,49], [8,64],
# [9,81]]
print(A6)


print("============================================================================================")

def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

f(2) # [0,1]
f(3,[3,2,1]) # [3,2,1,0,1,4]
f(3) # [0,1,0,1,4]

print("============================================================================================")

l = [1,2,3]
t = (4,5,6)
d = {'a':7,'b':8,'c':9}

def f(*args,**kwargs): print(args, kwargs)

f() # () {}
f(1,2,3) # (1,2,3) {}
f(1,2,3,"groovy") # (1,2,3,"groovy") {}
f(a=1,b=2,c=3) # () {'a':1, 'b':2, 'c':3}
f(a=1,b=2,c=3,zzz="hi") # () {'a':1, 'b':2, 'c':3, 'zzz':'hi'}
f(1,2,3,a=1,b=2,c=3) # (1,2,3) {'a':1, 'b':2,'c':3}
f(*l,**d) # (1,2,3) {'a':7,'b':8,'c':9}
f(*t,**d) # (4,5,6) {'a':7,'b':8,'c':9}
f(1,2,*t) # (1,2,4,5,6) {}
f(q="winning",**d) # () {'a':7,'b':8,'c':9, 'q':'winning'}
f(1,2,*t,q="winning",**d) # (1,2,4,5,6) {'a':7,'b':8,'c':9, 'q':'winning'}
f(l,d) # ([1, 2, 3], {'a': 7, 'b': 8, 'c': 9}) {}
f(l,t,d) # ([1, 2, 3], (4, 5, 6), {'a': 7, 'b': 8, 'c': 9}) {}
#f(*l, *d) # (1, 2, 3, 'a', 'b', 'c') {}
# f(**l) # error

print("============================================================================================")

# Describe Python's garbage collection mechanism in brief.
#
# Answer
# A lot can be said here. There are a few main points that you should mention:
#
# Python maintains a count of the number of references to each object in memory. If a reference
# count goes to zero then the associated object is no longer live and the memory allocated to
# that object can be freed up for something else occasionally things called "reference cycles"
# happen. The garbage collector periodically looks for these and cleans them up. An example
# would be if you have two objects o1 and o2 such that o1.x == o2 and o2.x == o1. If o1 and o2 are
# not referenced by anything else then they shouldn't be live. But each of them has a reference
# count of 1. Certain heuristics are used to speed up garbage collection. For example, recently
# created objects are more likely to be dead. As objects are created, the garbage collector
# assigns them to generations. Each object gets one generation, and younger generations are
# dealt with first.

print("============================================================================================")

# Functions that Return Functions

def get_function():
    print("Inside get_function")
    def returned_function():
        print("inside returned_function")
        return 1
    print("Outside get_function")
    return returned_function

#returned_function() # will throw "NameError: name 'returned_function' is not defined"
x = get_function() # will print Inside get_function \n Outside get_function
print(x) # will print <function get_function.<locals>.returned_function at 0x7fb01029fd30>
x() # will print inside returned_function
print(x()) # will print inside returned_function \n 1

print("============================================================================================")

def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10) # [10]
list2 = extendList(123,[]) # [123]
list3 = extendList('a') # [10, 'a']

print(list1) # [10, 'a']
print(list2) # [123]
print(list3) # [10, 'a']

print("============================================================================================")

def multipliers():
    return [lambda x: i * x for i in range(4)]

print([m(2) for m in multipliers()])

# for m in multipliers():
#     print(m)
#     print(m(2))
# ?

print("============================================================================================")

class Parent(object):
    x = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

print(Parent.x, Child1.x, Child2.x) # 1,1,1
Child1.x = 2
print(Parent.x, Child1.x, Child2.x) #1,2,1
Parent.x = 3
print(Parent.x, Child1.x, Child2.x) #3,2,3
#The key to the answer is that, in Python, class variables are internally handled as dictionaries.
# If a variable name is not found in the dictionary of the current class, the class hierarchy
# (i.e., its parent classes) are searched until the referenced variable name is found (if the
# referenced variable name is not found in the class itself or anywhere in its hierarchy, an
# AttributeError occurs).

#Therefore, setting x = 1 in the Parent class makes the class variable x (with a value of 1)
# referenceable in that class and any of its children. That’s why the first print statement
# outputs 1 1 1.

# Subsequently, if any of its child classes overrides that value (for example, when we execute the
# statement Child1.x = 2), then the value is changed in that child only. That’s why the second
# print statement outputs 1 2 1.

# Finally, if the value is then changed in the Parent (for example, when we execute the statement
# Parent.x = 3), that change is reflected also by any children that have not yet overridden the
# value (which in this case would be Child2). That’s why the third print statement outputs 3 2 3.

print("============================================================================================")

def div1(x, y):
    print("%s/%s = %s" % (x, y, x / y))
def div2(x, y):
    print("%s//%s = %s" % (x, y, x // y))

div1(5, 2) # python3 = 2.5, python2 = 2
div1(5., 2) # python3 = 2.5, python2 = 2.5
div2(5, 2) # python3 = 2, python2 = 2
div2(5., 2.) # python3 = 2.0, python2 = 2.0

print("============================================================================================")

list = ['a', 'b', 'c', 'd', 'e']
print(list[10:]) # []; this will NOT throw IndexError

print("============================================================================================")

list = [ [ ] ] * 5
print(list)  # output? [[],[],[],[],[]]
list[0].append(10)
print(list)  # output? [[10], [10], [10], [10], [10]]
list[1].append(20)
print(list)  # output? [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20]]
list.append(30)
print(list)  # output? [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], 30]

# list = [ [ ] ] * 5 [[],[],[],[],[]]
# list.append([]) [[],[],[],[],[],[]]
# list[0].append(10)
# print(list)  # output? [[10], [10], [10], [10], [10], []]
# list[1].append(20)
# print(list)  # output? [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], []]
# list.append(30)
# print(list)  # output? [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], [], 30]

# The first line of output is presumably intuitive and easy to understand; i.e., list = [ [ ] ]
# * 5 simply creates a list of 5 lists.
#
# However, the key thing to understand here is that the statement list = [ [ ] ] * 5 does NOT
# create a list containing 5 distinct lists; rather, it creates a a list of 5 references to the
# same list. With this understanding, we can better understand the rest of the output.
#
# list[0].append(10) appends 10 to the first list. But since all 5 lists refer to the same list,
# the output is: [[10], [10], [10], [10], [10]].
#
# Similarly, list[1].append(20) appends 20 to the second list. But again, since all 5 lists refer
# to the same list, the output is now: [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20]].
#
# In contrast, list.append(30) is appending an entirely new element to the “outer” list, which
# therefore yields the output: [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], 30].

print("============================================================================================")

class DefaultDict(dict):
  def __missing__(self, key):
    return []

d = DefaultDict()
d['flop'] = 37
print(d)

print("============================================================================================")

# Use the dir() method to list the functions in a module.

# Monkey Patching
# class A:
#     def func(self):
#         print("func() is being called")
#
# def monkey_f():
#     print("monkey_f() is being called")
#
# A.func = monkey_f
# obj = A()
# obj.func()

print("============================================================================================")

a = True
b = False
c = False

if a or b and c:
    print("GEEKSFORGEEKS")
else:
    print("geeksforgeeks")
# GEEKSFORGEEKS

# In Python, AND operator has higher precedence than OR operator. So, it is evaluated first. i.e,
# (b and c) evaluates to false.Now OR operator is evaluated. Here, (True or False) evaluates to
# True. So the if condition becomes True and GEEKSFORGEEKS is printed as output.

print("============================================================================================")

a = True
b = False
c = False

if not a or b:
    print(1)
elif not a or not b and c:
    print(2)
elif not a or b or not b and a:
    print(3)
else:
    print(4)

#3
# In Python the precedence order is first NOT then AND and in last OR. So the if condition and
# second elif condition evaluates to False while third elif condition is evaluated to be True
# resulting in 3 as output.

print("============================================================================================")

count = 1

def doThis():
    global count
    for i in (1, 2, 3):
        count += 1

doThis()
print(count)
#4

print("============================================================================================")

class Acc:
    def __init__(self, id):
        self.id = id
        id = 555


acc = Acc(111)
print(acc.id)
#111

print("============================================================================================")

for i in range(2):
    print(i)
for i in range(4, 6):
    print(i)

# 0 1 4 5

print("============================================================================================")

values = [1, 2, 3, 4]
numbers = set(values)

def checknums(num):
    if num in numbers:
        return True
    else:
        return False

for i in filter(checknums, values):
    print(i)

print("============================================================================================")

class Geeks:
    def __init__(self, id):
        self.id = id

manager = Geeks(100)
manager.__dict__['life'] = 49
print(manager.life + len(manager.__dict__))

# 51
# In the above program we are creating a member variable having name ‘life’ by adding it directly
# to the dictionary of the object ‘manager’ of class ‘Geeks’. Total numbers of items in the
# dictionary is 2, the variables ‘life’ and ‘id’. Therefore the size or the length of the
# dictionary is 2 and the variable ‘life’ is assigned a value ’49’. So the sum of the variable
# ‘life’ and the size of the dictionary is 49 + 2 = 51.

print("============================================================================================")

a = "GeeksforGeeks "
b = 13
#print(a + b) # Error

print("============================================================================================")

def gfgFunction():
    "Geeksforgeeks is cool website for boosting up technical skills"
    return 1

print(gfgFunction.__doc__[17:21])
# cool

print("============================================================================================")

check1 = ['Learn', 'Quiz', 'Practice', 'Contribute']
check2 = check1
check3 = check1[:]

check2[0] = 'Code'
check3[1] = 'Mcq'

count = 0
for c in (check1, check2, check3):
    if c[0] == 'Code':
        count += 1
    if c[1] == 'Mcq':
        count += 10

print(count)
# 12
# When assigning check1 to check2, we create a second reference to the same list. Changes to
# check2 affects check1. When assigning the slice of all elements in check1 to check3, we are
# creating a full copy of check1 which can be modified independently (i.e, any change in check3
# will not affect check1).
# So, while checking check1 ‘Code’ gets matched and count increases to 1, but Mcq doest gets
# matched since its available only in check3.
# Now checking check2 here also ‘Code’ gets matched resulting in count value to 2.
# Finally while checking check3 which is separate than both check1 and check2 here only Mcq gets
# matched and count becomes 12.

print("============================================================================================")

def gfg(x, l=[]):
    for i in range(x):
        l.append(i * i)
    print(l)

gfg(2) # [0,1]
gfg(3, [3, 2, 1]) # [3,2,1,0,1,4]
gfg(3) # [0,1,0,1,4]

print("============================================================================================")

list1 = [1998, 2002, 1997, 2000]
list2 = [2014, 2016, 1996, 2009]

print("list1 + list 2 = : ", list1 + list2) # [1998, 2002, 1997, 2000, 2014, 2016, 1996, 2009]
print("list1 * 2 = : ", list1 * 2) # [1998, 2002, 1997, 2000, 1998, 2002, 1997, 2000]

print("============================================================================================")

data = [2, 3, 9]
temp = [[x for x in [data]] for x in range(3)]
print (temp)

print("============================================================================================")

data = [x for x in range(5)] # [0,1,2,3,4]
temp = [x for x in range(7) if x in data and x%2==0] # [0,2,4]
print(temp)

print("============================================================================================")

temp = 'Geeks 22536 for 445 Geeks'
data = [x for x in (int(x) for x in temp if x.isdigit()) if x%2 == 0]
print(data) # [2, 2, 6, 4, 4]

print("============================================================================================")

data = [x for x in (x for x in 'Geeks 22966 for Geeks' if x.isdigit()) if (x in ([x for x in
                                                                                  range(20)]))]
print(data) # []

print("============================================================================================")

#L1 = list()
L1 = []
L1.append([1, [2, 3], 4]) # [[1, [2, 3], 4]]
L1.extend([7, 8, 9]) # [[1, [2, 3], 4], 7, 8, 9]
print(L1[0][1][1] + L1[2]) # 11

print("============================================================================================")

L1 = [1, 1.33, 'GFG', 0, 'NO', None, 'G', True]
val1, val2 = 0, ''
for x in L1:
    if(type(x) == int or type(x) == float):
        val1 += x
    elif(type(x) == str):
        val2 += x
    else:
        break
print(val1, val2) # 2.33, GFGNO

print("============================================================================================")

L1 = [1, 2, 3, 4] # [[5], 2, 3, 4]
L2 = L1 # [[5], 2, 3, 4]
L3 = L1.copy() # [1, 2, 3, 4]
#L4 = list(L1) # [1, 2, 3, 4]
L1[0] = [5]
print(L1, L2, L3, L4)

print("============================================================================================")

T1 = (1)
T2 = (3, 4)
T1 += 5
print(T1) # 6; since T1 is INT and not TUPLE
# print(T1 + T2) # TypeError, since it attempts to add int with tuple

print("============================================================================================")

L = [1, 3, 5, 7, 9]
print(L.pop(-3), end = '  ')
print(L.remove(L[0]), end = '  ')
print(L)
# 5 None [3,7,9]

print("============================================================================================")

from math import sqrt
L1 = [x**2 for x in range(10)].pop() # [0,1,4,9,16,25,36,49,64,81]
# .pop() will pop the last element, hence L1 = 81
L1 += 19 # L1 = 100
print(sqrt(L1), end = " ") # 10.0
L1 = [x**2 for x in reversed(range(10))].pop() # 10.0
L1 += 16
print(int(sqrt(L1))) # 10.0 4

print("============================================================================================")

D = dict()
for x in enumerate(range(2)):
    D[x[0]] = x[1]
    D[x[1]+7] = x[0]
print(D)

print("============================================================================================")

mylist =[0, 5, 2, 0, 'gfg', '', []]
#print(list(filter(bool, mylist))) # [5,2,'gfg']

print("============================================================================================")

value_1 = [1,2,3,4]
data = 0
try:
    data = value_1[3]
except IndexError:
    print('GFG IndexError ', end='')
except:
    print('GeeksforGeeks IndexError ', end='')
finally:
    print('Geeks IndexError ', end='')

data = 10
try:
    data = data/0
except ZeroDivisionError:
    print('GFG ZeroDivisionError ', end='')
finally:
    print('GFG ZeroDivisionError ', end='')

# Geeks IndexError | GFG ZeroDivisionError GFG ZeroDivisionError

print("============================================================================================")

# run .py script from another .py script
############1
# dir_path = os.path.dirname(os.path.realpath(__file__))
# then join the file name you want
# file_path = os.path.join(dir_path,'plot.py')
# Finally your system call
#
# os.system(f'py {file_path}') # if you're on 3.6 and above.
# os.system('py %s' % file_path)

############2
# import os
# import subprocess
# import sys
#
# #py_filepath = 'C:/Users/benb/Desktop/flaskEconServer/plots.py'
# py_filepath = 'plots_test.py'
#
# args = '"%s" "%s" "%s"' % (sys.executable,                  # command
#                            py_filepath,                     # argv[0]
#                            os.path.basename(py_filepath))   # argv[1]
#
# proc = subprocess.run(args)
# print('returncode:', proc.returncode)

print("============================================================================================")

