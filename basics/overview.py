# comments

# sample comment
def print_name(name):
    """ This is function used
    to print given name"""
    print("name is : {}".format(name))
    a = 1

    if a == 1:
        print("i am 1 ")
        b = 2
        if b > 1:
            print("i am > 1")
            c = 3


# class comment
class Sample:
    """ This is sample class used for something
    multiple lines
    input parametes"""

    @staticmethod
    def print_name(self, name):
        """ This method is used to print given name"""
        print("name is : {}".format(name))


# a = 1
# print("hello world")
#
# print_name("Ramana")

# s = Sample()
# print(s.__doc__)
# print(print_name.__doc__)

# ---------------------------------------------------------------
# String

name = 'Ramana'
address = """My address is
at some where 
at some location"""
address1 = '''My location is at somewhere
at some location'''
#
# name = 'Ramana'
# print(hex(id(name)))
#
# name = "Varma"
# print(hex(id(name)))

# a = 1
# print(hex(id(name)))
#
# a = 10 ** 2
# print(hex(id(name)))
#
# print(a)
# # a --> 0x18aabea4930
# print(a)


# ---------------------------------------------------------------
# Variable type declaration

# a = 10
# print(type(a))
#
# a = "Ramana"
# print(type(a))
#
# a = [1, 2, 3, 4]
# print(type(a))


# ----------------------------------------------------------------
# Data types


name = "Ramana"  # string type
age = 22  # int
cost = 100.12  # float
married = True  # boolean True or False

# print(name, age, cost, married)
# print("name: " + name + " age: " + str(age), "cost: " + str(cost))
#
# print("My name is : {0}, and my age is {1}, cost :{2} and are you married :{3}".
#       format(age, name, cost, married))
#
# print(f"my name is {name}, age is {age}, cost of {cost} and married: {married}")

# print(type(age))
# age = str(age)
# print(type(age))
#
# print(type(married))

f = True
false = False

# ----------------------------------------------------------------
# Statement

# int a = 10 ;

a = 10; name = "Ramana"; age = 22  # not recommended

# print(a, name, age)

name = "Ramana"

# -----------------------------------------------------------------
# Compound statements and indentation

name = "Varma"

# if name == "Ramana":
#     print("Given name is : {}".format(name))
#     print()
# else:
#     print("Given name is something else")
#     print()

# function something(name, age){
#     print()
#
# }


def something(name1, age1):
    print()


# ------------------------------------------------------------------
# Assignment Operator
a = 10
name = "Ramana"


# ------------------------------------------------------------------
# Arithmetic Operators
#  + (add), - (subtract), * (multiply), / (divide), // (integer divide), ** (exponent), % (modulus).

a = 10
b = 20

# print(a + b)

# In [1]: 10 + 10
# Out[1]: 20
#
# In [2]: 10 - 10
# Out[2]: 0
#
# In [3]: 20 - 10
# Out[3]: 10
#
# In [4]: 20 * 10
# Out[4]: 200
#
# In [5]: 20 / 10
# Out[5]: 2.0
#
# In [6]: type(20/10)
# Out[6]: float
#
# In [7]: 22 / 10
# Out[7]: 2.2
#
# In [8]: 22 // 10
# Out[8]: 2
#
# In [9]: 29/10
# Out[9]: 2.9
#
# In [10]: 29//10
# Out[10]: 2
#
# In [11]: round(29/10)
# Out[11]: 3
#
# In [12]: round(25/10)
# Out[12]: 2
#
# In [13]: round(26/10)
# Out[13]: 3
#
# In [14]: 2 ** 2
# Out[14]: 4
#
# In [15]: 2 ** 10
# Out[15]: 1024
#
# In [16]: 22 % 10
# Out[16]: 2
#
# In [17]: 23 % 10
# Out[17]: 3
#
# In [18]: i = 10

# -----------------------------------------------------------------
# Compound Assignment Operators: +=, -=, *=, /=, //=, **=, %=.
a = 10
a += 10
a -= 10
a *= 10
a //= 10
a **= 2
a %= 9

#print(a)

# ------------------------------------------------------------------
# Comparision Operators
# ==, !=, <, <=, >, >=, in, not in, is, not is.

# In [26]: a = 10
#
# In [27]: a == 10
# Out[27]: True
#
# In [28]: if a == 10:
#     ...:     print("true")
#     ...: else:
#     ...:     print("false")
#     ...:
# true
#
# In [29]: a != 10
# Out[29]: False
#
# In [30]: a != 9
# Out[30]: True
#
# In [31]: a < 5
# Out[31]: False
#
# In [32]: a > 5
# Out[32]: True
#
# In [33]: a >= 5
# Out[33]: True
#
# In [34]: a <= 5
# Out[34]: False
#
# In [36]: if a >= 5:
#     ...:     print("true")
#     ...:
# true
#
# In [37]: if a <= 5:
#     ...:     print("true")
#     ...:
#     ...:
#
# In [38]: a = 10
#
# In [39]: b = 10
#
# In [40]: a is b
# Out[40]: True
#
# In [41]: hex(id(a))
# Out[41]: '0x7ff82d04a2b0'
#
# In [42]: hex(id(b))
# Out[42]: '0x7ff82d04a2b0'
#
# In [43]: b = 11
#
# In [44]: hex(id(b))
# Out[44]: '0x7ff82d04a2d0'
#
# In [45]: hex(id(a))
# Out[45]: '0x7ff82d04a2b0'
#
# In [46]: a - 128
# Out[46]: -118
#
# In [47]: a = 128
#
# In [48]: b = 128
#
# In [49]: hex(id(a))
# Out[49]: '0x7ff82d04b170'
#
# In [50]: hex(id(b))
# Out[50]: '0x7ff82d04b170'
#
# In [51]: hex(id(a)), hex(id(b))
# Out[51]: ('0x7ff82d04b170', '0x7ff82d04b170')
#
#
# In [53]: a = 256; b= 256
#
# In [54]: hex(id(a)), hex(id(b))
# Out[54]: ('0x7ff82d04c170', '0x7ff82d04c170')
#
# In [55]: a = 258; b= 258
#
# In [56]: hex(id(a)), hex(id(b))
# Out[56]: ('0x250fe588ad0', '0x250fe588f50')
#
# In [57]: a = 257; b= 257
#
# In [58]: hex(id(a)), hex(id(b))
# Out[58]: ('0x250fe588790', '0x250fe5888f0')
#
# In [59]: 2 * 8
# Out[59]: 16
#
# In [60]: 2 * 16
# Out[60]: 32
#
# In [61]: 2 ** 8
# Out[61]: 256
#
# In [62]:
#
# In [62]: a = 257; b= 257
#
# In [63]: a is b
# Out[63]: False
#
# In [64]: a is not b
# Out[64]: True
#
#
# In [66]: a is not b
# Out[66]: True
#
# In [67]: l = [1, 2, 3, 4, 5]
#
# In [68]: 1 in l
# Out[68]: True
#
# In [69]: 6 in l
# Out[69]: False
#
# In [70]: 1 not in l
# Out[70]: False
#
# In [71]: 1 not in l
# Out[71]: False

# In [72]: name = "Ramana"
#
# In [73]:
#
# In [73]: 'R' in name
# Out[73]: True
#
# In [74]: 'Ram' in name
# Out[74]: True
#
# In [75]: 'ana' in name
# Out[75]: True
#
# In [76]: 'anan' in name
# Out[76]: False
#
# In [77]: 'Ram' in name
# Out[77]: True
#
# In [78]: 'maR' in name
# Out[78]: False
#
# In [79]: 'maR' not in name


# -------------------------------------------------------------
# Logical Operators: and, or, not

# In [81]: a = 10 ; b = 5
#
# In [82]: name = "Ramana"
#
# In [83]: age = 20
#
# In [85]: if name == "Ramana" and age >= 18:
#     ...:     print("Eligigle for voting")
#     ...: else:
#     ...:     print("not eligible")
#     ...:
# Eligigle for voting
#
# In [86]: True and True
# Out[86]: True
#
# In [87]: True and False
# Out[87]: False
#
# In [88]: False and True
# Out[88]: False
#
# In [89]: False and False
# Out[89]: False
#
# In [90]: True or False
# Out[90]: True
#
# In [91]: if name == "anything" or age >=18:
#     ...:     print("eligible")
#     ...: else:
#     ...:     print("not eligible")
#     ...:
# eligible
#
# In [92]: not True
# Out[92]: False
#
# In [93]: not False
# Out[93]: True
#
# In [94]: if not name == "anything":
#     ...:     print("anything")
#     ...:
# anything
#
# In [95]: if not name == "Ramana":
#     ...:     print("anything")
#     ...:
#     ...:

# Condition statements

# age = 45
#
# if age < 18:
#     print("minor")
# elif age >= 18 and age <= 40:
#     print("He is Major and not retired")
# elif age > 40 and age <=50:
#     print("he can take vacation")
# else:
#     print("Retired")

# (True and True) or (False and True) --> True or False --> True

age = 19

# Shorthand if-else --> True_expr if test else false_expr

eligible_for_voting = "if successed" if age >= 18 else "Failed"

# print(eligible_for_voting)

# Loops --> while and for loop

i = 1

# while i <= 10:
#     print(i)
#     i += 1

# for i in range(2, 11, 2):
#     print(i)

# for i in "Ramana":
#     print(i)

aa = 10
bb = 11

# break
# while i <= aa:
#     if i == bb:
#         break
#     print(i)
#     i += 1
# else:
#     print("i am loop else")


# continue

i = 0
bb = 5
# while i < 10:
#     i += 1
#     if i == 4 or i == 5 or i == 6:
#         continue
#
#     print(i)
    # some login
    # extra logic


# -----------------------------------------------------------
# List

# In [118]: l = []
#
# In [119]: l = [1, 2, 3, 4, 5]
#
# In [120]: l
# Out[120]: [1, 2, 3, 4, 5]
#
# In [121]: print(l)
# [1, 2, 3, 4, 5]
#
# In [122]: colors = ["red", "pink", "blue", "green", "yellow"]
#
# In [123]:
#
# In [123]:
#
# In [123]: print(colors)
# ['red', 'pink', 'blue', 'green', 'yellow']
#
# In [124]: print(colors[2])
# blue
#
# In [125]: colors[2] = "Blue"
#
# In [126]: colors
# Out[126]: ['red', 'pink', 'Blue', 'green', 'yellow']
#
# In [127]: len(colors)
# Out[127]: 5
#
# In [128]: colors[0]
# Out[128]: 'red'
#
# In [129]: colors[4]
# Out[129]: 'yellow'
#
# In [130]: colors[-1]
# Out[130]: 'yellow'
#
# In [131]: colors[-2]
# Out[131]: 'green'
#
# In [132]: colors[1]
# Out[132]: 'pink'
#
# In [133]: colors[0]
# Out[133]: 'red'
#
# In [134]: length = len(colors)
#
#
# NameError: name 'lenght' is not defined
#
# In [136]: length
# Out[136]: 5
#
# In [137]: length/2
# Out[137]: 2.5
#
# In [138]: mid = length//2
#
# In [139]: colors[mid]
# Out[139]: 'Blue'
#
# In [140]: colors
# Out[140]: ['red', 'pink', 'Blue', 'green', 'yellow']
#
#
# In [143]: colors
# Out[143]: ['red', 'pink', 'Blue', 'green', 'yellow']
#
# In [144]:
#
# In [145]: colors[1:2]
# Out[145]: ['pink']
#
# In [146]: colors[0:3]
# Out[146]: ['red', 'pink', 'Blue']
#
# In [147]: colors
# Out[147]: ['red', 'pink', 'Blue', 'green', 'yellow']
#
# In [148]: colors[-1:-4]
# Out[148]: []
#
# In [149]: colors[-1:4]
# Out[149]: []
#
# In [150]: colors[-1:2]
# Out[150]: []
#
# In [151]: colors[-1:]
# Out[151]: ['yellow']
#
# In [152]: colors[-1:0]
# Out[152]: []
#
# In [153]: colors[-1:1]
# Out[153]: []
#
# In [154]: colors[-1:2]
# Out[154]: []
#
# In [155]: colors[-1:3]
# Out[155]: []
#
# In [156]: colors[-1:-4]
# Out[156]: []
#
# In [157]: colors[0:-1]
# Out[157]: ['red', 'pink', 'Blue', 'green']
#
# In [158]: colors[-1:]
# Out[158]: ['yellow']
#
# In [161]: colors[:-1]
# Out[161]: ['red', 'pink', 'Blue', 'green']
#
#
# In [164]: colors
# Out[164]: ['red', 'pink', 'Blue', 'green', 'yellow']
#
# In [165]: colors[0:]
# Out[165]: ['red', 'pink', 'Blue', 'green', 'yellow']
#
# In [166]: colors[-4:]
# Out[166]: ['pink', 'Blue', 'green', 'yellow']
#
# In [167]: colors[-3:]
# Out[167]: ['Blue', 'green', 'yellow']
#
# In [168]: colors[:-3]
# Out[168]: ['red', 'pink']
#
# In [169]: colors
# Out[169]: ['red', 'pink', 'Blue', 'green', 'yellow']
#
# In [173]: colors[-2:-5:-1]
# Out[173]: ['green', 'Blue', 'pink']
#
#
# In [177]: colors
# Out[177]: ['red', 'pink', 'Blue', 'green', 'yellow']
#
#
# In [179]: colors[1: 4]
# Out[179]: ['pink', 'Blue', 'green']
#
# In [180]: colors[1: 4:2]
# Out[180]: ['pink', 'green']
#
# In [181]: l = list(range(1, 10))
#
# In [182]: l
# Out[182]: [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
#
# In [184]: l[1:10:3]
# Out[184]: [2, 5, 8]
#
# In [185]: l[10:1:-3]
# Out[185]: [9, 6, 3]
#
#
# In [187]: l[-1:-10:-3]
# Out[187]: [9, 6, 3]
#
# In [188]: len(l)
# Out[188]: 9
#
# In [189]: l
# Out[189]: [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# In [190]: min(l)
# Out[190]: 1
#
# In [191]: max(l)
# Out[191]: 9
#
# In [192]: sum(l)
# Out[192]: 45
#
# In [193]: colors
# Out[193]: ['red', 'pink', 'Blue', 'green', 'yellow']
#
#
# In [195]: ':'.join(colors)
# Out[195]: 'red:pink:Blue:green:yellow'
#
# In [196]: ','.join(colors)
# Out[196]: 'red,pink,Blue,green,yellow'
#
# In [197]: '\n'.join(colors)
# Out[197]: 'red\npink\nBlue\ngreen\nyellow'


# Data structures
# List
# tuple
# dict
# set

# In [199]: l
# Out[199]: [1, 2, 3, 4]
#
# In [200]:
#
# In [200]: t = (1,2,3,4)
#
# In [201]: l.append(5)
#
# In [202]: l
# Out[202]: [1, 2, 3, 4, 5]
#
# In [203]: t.append(5)
# ---------------------------------------------------------------------------
# AttributeError                            Traceback (most recent call last)
# <ipython-input-203-7bc26d8122b5> in <module>
# ----> 1 t.append(5)
#
# AttributeError: 'tuple' object has no attribute 'append'
#
# In [204]: t.count()
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-204-9ccfa7eed41a> in <module>
# ----> 1 t.count()
#
# TypeError: count() takes exactly one argument (0 given)
#
# In [205]: t.count
# Out[205]: <function tuple.count(value, /)>
#
# In [206]: t.count()
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-206-9ccfa7eed41a> in <module>
# ----> 1 t.count()
#
# TypeError: count() takes exactly one argument (0 given)
#
# In [207]:
#
# In [207]: d = {"one": 1, "two": 2}
#
# In [208]: d
# Out[208]: {'one': 1, 'two': 2}
#
# In [209]: varma = {"name": "Varma", "age": 30, "gender": "male", "dob": "10-10-10", "address": "Some address"}
#
# In [210]: varma
# Out[210]:
# {'name': 'Varma',
#  'age': 30,
#  'gender': 'male',
#  'dob': '10-10-10',
#  'address': 'Some address'}
#
# In [211]: varma = {"name": "Varma", "age": 30, "gender": "male", "dob": "10-10-10", "address": ["address1", "address2"]
#      ...:  }
#
# In [212]: varma
# Out[212]:
# {'name': 'Varma',
#  'age': 30,
#  'gender': 'male',
#  'dob': '10-10-10',
#  'address': ['address1', 'address2']}
#
#
# In [214]:
#
# In [214]:
#
# In [214]: varma = {"name": "Varma", "age": 30, "gender": "male", "dob": "10-10-10", "address": ["address1", "address2"]
#      ...:  , "hobbies": {"playing": ["crickent", "football"], "indoor_games": ["carroms"]}}
#
# In [215]:
#
# In [215]:
#
# In [215]: varma
# Out[215]:
# {'name': 'Varma',
#  'age': 30,
#  'gender': 'male',
#  'dob': '10-10-10',
#  'address': ['address1', 'address2'],
#  'hobbies': {'playing': ['crickent', 'football'], 'indoor_games': ['carroms']}}
#
# In [216]: varma['name']
# Out[216]: 'Varma'
#
# In [217]: varma['age']
# Out[217]: 30
#
# In [218]: varma['address']
# Out[218]: ['address1', 'address2']
#
# In [219]: varma['hobbies']
# Out[219]: {'playing': ['crickent', 'football'], 'indoor_games': ['carroms']}
#
# In [220]: varma['hobbies']['indoor_games']
# Out[220]: ['carroms']
#
#
# In [222]: varma['hobbies']['games']
# ---------------------------------------------------------------------------
# KeyError                                  Traceback (most recent call last)
# <ipython-input-222-9ad1cafa3cec> in <module>
# ----> 1 varma['hobbies']['games']
#
# KeyError: 'games'
#
# In [223]: varma = {"name": "Varma", "name": "Ramana"}
#
# In [224]: varma
# Out[224]: {'name': 'Ramana'}
#
# In [225]: varma
# Out[225]: {'name': 'Ramana'}
#
# In [226]: varma['age'] = 22
#
# In [227]: varma
# Out[227]: {'name': 'Ramana', 'age': 22}
#
# In [228]: colors
# Out[228]: ['red', 'pink', 'Blue', 'green', 'yellow']
#
# In [229]:
#
# In [229]: varma
# Out[229]: {'name': 'Ramana', 'age': 22}
#
# In [230]: del varma['age']
#
# In [231]: varma
# Out[231]: {'name': 'Ramana'}
#
# In [232]: t = (1,2,3)
#
# In [233]:
#
# In [233]: s = {1,2,3,4}
#
# In [234]: s = {1,2,3,4, 1,2}
#
# In [235]: s
# Out[235]: {1, 2, 3, 4}
#
# In [236]: s.add(5)
#
# In [237]: s
# Out[237]: {1, 2, 3, 4, 5}
#
# In [238]: s.add(5)
#
# In [239]: s
# Out[239]: {1, 2, 3, 4, 5}
#
#
# In [241]: s.discard(3)
#
# In [242]: s
# Out[242]: {1, 2, 4, 5}
#
#
# In [244]: s
# Out[244]: {1, 2, 4, 5}
#
# In [245]: s1 = {1,2,3}
#
# In [246]: s2 = {3,4,5}
#
# In [247]: s.union(s2)
# Out[247]: {1, 2, 3, 4, 5}
#
# In [248]: s.intersection(s2)
# Out[248]: {4, 5}
#
# In [249]: s.clear()
#
# In [250]: s
# Out[250]: set()
#
# In [251]: t = (1,2,3)
#
# In [252]: t
# Out[252]: (1, 2, 3)
#
# In [253]: t[0]
# Out[253]: 1
#
# In [254]:

# --------------------------------------------------------------
# Sequences (String, List, Tuple)
# in, not in: membership test.
# +: concatenation
# *: repetition
# [i], [-i]: indexing
# [m:n:step]: slicing
# len(seq), min(seq), max(seq)
# seq.index(), seq.count()


# For mutable sequences (list) only:
# Assignment via [i], [-i] (indexing) and [m:n:step] (slicing)
# Assignment via =, += (compound concatenation), *= (compound repetition)
# del: delete
# seq.clear(), seq.append(), seq.extend(), seq.insert(), seq.remove(), seq.pop(), seq.copy(), seq.reverse()
#

# ---------------------------------------------------------------

a = 5
b = 10


def arithmetic_operations(a, b):
    return a + b, a-b, a/b, a % b


print(arithmetic_operations(10, 5))
