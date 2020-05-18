x = 1000
y = 2

# print(hex(id(x)))
#
#
# def fun():
#     global x
#     print(hex(id(x)))
#     x += 1
#     print(hex(id(x)))
#     print('func : {}'.format(x))
#
#
# fun()
#
# print(hex(id(x)))
# print('main: {}'.format(x))

_x12121 = 1


def greeting(name):
    if name is None:
        return "Please send proper name"

    return f"Hello, {name}"


def num_print(n):
    if n is not None and n > 0:
        print(f"printing num : {n}")
    else:
        print("Please give proper & positive number")


# num_print(-5)

# positional arguments
# keyword arguments


def fun(a, b, c=1, d=2):
    print(a, b)


fun(1, 2)

#
# 1]: l = [1,2,3]
#
# In [2]: del l[1]
#
# In [3]: l
# Out[3]: [1, 3]
#
# In [4]: t = (1,2,3)
#
# In [5]: del t[3]
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-5-fac3d15da1b1> in <module>
# ----> 1 del t[3]
#
# TypeError: 'tuple' object doesn't support item deletion
#
# In [6]: s = 'Ramana'
#
# In [7]: del s[2]
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-7-e48aef1fce88> in <module>
# ----> 1 del s[2]
#
# TypeError: 'str' object doesn't support item deletion
#
# In [8]: l = [1,2, 3]
#
# In [9]: l.append(4)
#
# In [10]: l
# Out[10]: [1, 2, 3, 4]
#
# In [11]: l.append([5,6,7])
#
# In [12]: l
# Out[12]: [1, 2, 3, 4, [5, 6, 7]]
#
# In [13]: l.extend([8,9,10])
#
# In [14]: l
# Out[14]: [1, 2, 3, 4, [5, 6, 7], 8, 9, 10]
#
# In [15]: dir(l)
# Out[15]:
# ['__add__',
#  '__class__',
#  '__contains__',
#  '__delattr__',
#  '__delitem__',
#  '__dir__',
#  '__doc__',
#  '__eq__',
#  '__format__',
#  '__ge__',
#  '__getattribute__',
#  '__getitem__',
#  '__gt__',
#  '__hash__',
#  '__iadd__',
#  '__imul__',
#  '__init__',
#  '__init_subclass__',
#  '__iter__',
#  '__le__',
#  '__len__',
#  '__lt__',
#  '__mul__',
#  '__ne__',
#  '__new__',
#  '__reduce__',
#  '__reduce_ex__',
#  '__repr__',
#  '__reversed__',
#  '__rmul__',
#  '__setattr__',
#  '__setitem__',
#  '__sizeof__',
#  '__str__',
#  '__subclasshook__',
#  'append',
#  'clear',
#  'copy',
#  'count',
#  'extend',
#  'index',
#  'insert',
#  'pop',
#  'remove',
#  'reverse',
#  'sort']
#
# In [16]: l.clear()
#
# In [17]: l
# Out[17]: []
#
# In [18]: l = [1,2,3]
#
# In [19]: l1 = l
#
# In [20]: l1
# Out[20]: [1, 2, 3]
#
# In [21]: l.append(4)
#
# In [22]: l1
# Out[22]: [1, 2, 3, 4]
#
# In [23]: l2 = l1.copy()
#
# In [24]: l2
# Out[24]: [1, 2, 3, 4]
#
# In [25]: l1.append(5)
#
# In [26]: l1
# Out[26]: [1, 2, 3, 4, 5]
#
# In [27]: l2
# Out[27]: [1, 2, 3, 4]
#
# In [28]: l1.count(1)
# Out[28]: 1
#
# In [29]: l1.append(5)
#
# In [30]: l1
# Out[30]: [1, 2, 3, 4, 5, 5]
#
# In [31]: l1.count1()
# ---------------------------------------------------------------------------
# AttributeError                            Traceback (most recent call last)
# <ipython-input-31-d87cefb07e93> in <module>
# ----> 1 l1.count1()
#
# AttributeError: 'list' object has no attribute 'count1'
#
# In [32]: l1.count(1)
# Out[32]: 1
#
# In [33]: l1.count(5)
# Out[33]: 2
#
# In [34]: help(l1.index)
# Help on built-in function index:
#
# index(value, start=0, stop=9223372036854775807, /) method of builtins.list instance
#     Return first index of value.
#
#     Raises ValueError if the value is not present.
#
#
# In [35]: l1.index(5)
# Out[35]: 4
#
# In [36]: l1.index(4)
# Out[36]: 3
#
# In [37]: l1.index(5, 4)
# Out[37]: 4
#
# In [38]: l1.index(5, 5)
# Out[38]: 5
#
# In [39]: l1
# Out[39]: [1, 2, 3, 4, 5, 5]
#
# In [40]: l1.insert(4,10)
#
# In [41]: l1
# Out[41]: [1, 2, 3, 4, 10, 5, 5]
#
# In [42]: l1.pop()
# Out[42]: 5
#
# In [43]: l1
# Out[43]: [1, 2, 3, 4, 10, 5]
#
# In [44]: l1.pop()
# Out[44]: 5
#
# In [45]: l1
# Out[45]: [1, 2, 3, 4, 10]
#
# In [46]: l1.pop()
# Out[46]: 10
#
# In [47]: x = l1.pop()
#
# In [48]: x
# Out[48]: 4
#
# In [49]: l1
# Out[49]: [1, 2, 3]
#
# In [50]:
#
# In [50]:
#
# In [50]:
#
# In [50]: l1
# Out[50]: [1, 2, 3]
#
# In [51]: l1.remove(4)
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# <ipython-input-51-16bdbf2a3d9f> in <module>
# ----> 1 l1.remove(4)
#
# ValueError: list.remove(x): x not in list
#
# In [52]: l1.remove(3)
#
# In [53]: l1
# Out[53]: [1, 2]
#
# In [54]: l1.append(3,4,5)
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-54-91d8c0586607> in <module>
# ----> 1 l1.append(3,4,5)
#
# TypeError: append() takes exactly one argument (3 given)
#
# In [55]: l1.extend([3,4,5])
#
# In [56]: l1
# Out[56]: [1, 2, 3, 4, 5]
#
# In [57]: l1.revese()
# ---------------------------------------------------------------------------
# AttributeError                            Traceback (most recent call last)
# <ipython-input-57-43a06ae46635> in <module>
# ----> 1 l1.revese()
#
# AttributeError: 'list' object has no attribute 'revese'
#
# In [58]: l1.reverse()
#
# In [59]: l1
# Out[59]: [5, 4, 3, 2, 1]
#
# In [60]: l1.sort()
#
# In [61]: l1
# Out[61]: [1, 2, 3, 4, 5]
#
# In [62]:
#
# In [62]:
#
# In [62]: l1 = [9, 10, 23, 56, 7,1,2]
#
# In [63]: l1.reverse()
#
# In [64]: l1
# Out[64]: [2, 1, 7, 56, 23, 10, 9]
#
# In [65]: l1.sort()
#
# In [66]: l1
# Out[66]: [1, 2, 7, 9, 10, 23, 56]
#
# In [67]: help(l1.sort)
# Help on built-in function sort:
#
# sort(*, key=None, reverse=False) method of builtins.list instance
#     Stable sort *IN PLACE*.
#
#
# In [68]:
#
# In [68]: l1.sort(reverse=True)
#
# In [69]: l1
# Out[69]: [56, 23, 10, 9, 7, 2, 1]
#
# In [70]: d = dict()
#
# In [71]: d
# Out[71]: {}
#
# In [72]: d = {'name': "Ramana", 1 : 1}
#
# In [73]: d
# Out[73]: {'name': 'Ramana', 1: 1}
#
# In [74]: d = {'name': "Ramana", 1 : 1, "name": "Varma"}
#
# In [75]: d
# Out[75]: {'name': 'Varma', 1: 1}
#
# In [76]: d = {'name': "Ramana", 1 : 1, "name": "Varma", None: None}
#
# In [77]: d
# Out[77]: {'name': 'Varma', 1: 1, None: None}
#
# In [78]:
#
# In [78]: d[None]
#
# In [79]: d = {'name': "Ramana", 1 : 1, "name": "Varma", None: 'None'}
#
# In [80]: d[none]
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# <ipython-input-80-45083fcb7565> in <module>
# ----> 1 d[none]
#
# NameError: name 'none' is not defined
#
# In [81]: d[None]
# Out[81]: 'None'
#
# In [82]: d['age'] = 22
#
# In [83]: d
# Out[83]: {'name': 'Varma', 1: 1, None: 'None', 'age': 22}
#
# In [84]: d['age'] = 25
#
# In [85]: d
# Out[85]: {'name': 'Varma', 1: 1, None: 'None', 'age': 25}
#
# In [86]: len(d)
# Out[86]: 4
#
# In [87]: d.keys()
# Out[87]: dict_keys(['name', 1, None, 'age'])
#
# In [88]: for key in d.keys():
#     ...:     print(key)
#     ...:
# name
# 1
# None
# age
#
# In [89]: for l in d:
#     ...:     print(l)
#     ...:
# name
# 1
# None
# age
#
# In [90]: for l in d.values():
#     ...:     print(l)
#     ...:
#     ...:
# Varma
# 1
# None
# 25
#
# In [91]: ct2 = dict([('a', 1), ('c', 3), ('b', 2)])
#
# In [92]: ct2
# Out[92]: {'a': 1, 'c': 3, 'b': 2}
#
# In [93]: ct2 = dict([('a', 1,2), ('c', 3), ('b', 2)])
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# <ipython-input-93-1d7df02f6c50> in <module>
# ----> 1 ct2 = dict([('a', 1,2), ('c', 3), ('b', 2)])
#
# ValueError: dictionary update sequence element #0 has length 3; 2 is required
#
# In [94]:
#
# In [94]:
#
# In [94]: d
# Out[94]: {'name': 'Varma', 1: 1, None: 'None', 'age': 25}
#
# In [95]: help(d)
# Help on dict object:
#
# class dict(object)
#  |  dict() -> new empty dictionary
#  |  dict(mapping) -> new dictionary initialized from a mapping object's
#  |      (key, value) pairs
#  |  dict(iterable) -> new dictionary initialized as if via:
#  |      d = {}
#  |      for k, v in iterable:
#  |          d[k] = v
#  |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
#  |      in the keyword argument list.  For example:  dict(one=1, two=2)
#  |
#  |  Methods defined here:
#  |
#  |  __contains__(self, key, /)
#  |      True if the dictionary has the specified key, else False.
#  |
#  |  __delitem__(self, key, /)
#  |      Delete self[key].
#  |
#  |  __eq__(self, value, /)
#  |      Return self==value.
#  |
#  |  __ge__(self, value, /)
#  |      Return self>=value.
#  |
#  |  __getattribute__(self, name, /)
#  |      Return getattr(self, name).
#  |
#  |  __getitem__(...)
#  |      x.__getitem__(y) <==> x[y]
#  |
#  |  __gt__(self, value, /)
#  |      Return self>value.
#  |
#  |  __init__(self, /, *args, **kwargs)
#  |      Initialize self.  See help(type(self)) for accurate signature.
#  |
#  |  __iter__(self, /)
#  |      Implement iter(self).
#  |
#  |  __le__(self, value, /)
#  |      Return self<=value.
#  |
#  |  __len__(self, /)
#  |      Return len(self).
#  |
#  |  __lt__(self, value, /)
#  |      Return self<value.
#  |
#  |  __ne__(self, value, /)
#  |      Return self!=value.
#  |
#  |  __repr__(self, /)
#  |      Return repr(self).
#  |
#  |  __setitem__(self, key, value, /)
#  |      Set self[key] to value.
#  |
#  |  __sizeof__(...)
#  |      D.__sizeof__() -> size of D in memory, in bytes
#  |
#  |  clear(...)
#  |      D.clear() -> None.  Remove all items from D.
#  |
#  |  copy(...)
#  |      D.copy() -> a shallow copy of D
#  |
#  |  get(self, key, default=None, /)
#  |      Return the value for key if key is in the dictionary, else default.
#  |
#  |  items(...)
#  |      D.items() -> a set-like object providing a view on D's items
#  |
#  |  keys(...)
#  |      D.keys() -> a set-like object providing a view on D's keys
#  |
#  |  pop(...)
#  |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
#  |      If key is not found, d is returned if given, otherwise KeyError is raised
#  |
#  |  popitem(...)
#  |      D.popitem() -> (k, v), remove and return some (key, value) pair as a
#  |      2-tuple; but raise KeyError if D is empty.
#  |
#  |  setdefault(self, key, default=None, /)
#  |      Insert key with a value of default if key is not in the dictionary.
#  |
#  |      Return the value for key if key is in the dictionary, else default.
#  |
#  |  update(...)
#  |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
#  |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
#  |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
#  |      In either case, this is followed by: for k in F:  D[k] = F[k]
#  |
#  |  values(...)
#  |      D.values() -> an object providing a view on D's values
#  |
#  |  ----------------------------------------------------------------------
#  |  Class methods defined here:
#  |
#  |  fromkeys(iterable, value=None, /) from builtins.type
#  |      Create a new dictionary with keys from iterable and values set to value.
#  |
#  |  ----------------------------------------------------------------------
#  |  Static methods defined here:
#  |
#  |  __new__(*args, **kwargs) from builtins.type
#  |      Create and return a new object.  See help(type) for accurate signature.
#  |
#  |  ----------------------------------------------------------------------
#  |  Data and other attributes defined here:
#  |
#  |  __hash__ = None
#
#
# In [96]:
#
# In [96]:
#
# In [96]:
#
# In [96]:
#
# In [96]: dir(d)
# Out[96]:
# ['__class__',
#  '__contains__',
#  '__delattr__',
#  '__delitem__',
#  '__dir__',
#  '__doc__',
#  '__eq__',
#  '__format__',
#  '__ge__',
#  '__getattribute__',
#  '__getitem__',
#  '__gt__',
#  '__hash__',
#  '__init__',
#  '__init_subclass__',
#  '__iter__',
#  '__le__',
#  '__len__',
#  '__lt__',
#  '__ne__',
#  '__new__',
#  '__reduce__',
#  '__reduce_ex__',
#  '__repr__',
#  '__setattr__',
#  '__setitem__',
#  '__sizeof__',
#  '__str__',
#  '__subclasshook__',
#  'clear',
#  'copy',
#  'fromkeys',
#  'get',
#  'items',
#  'keys',
#  'pop',
#  'popitem',
#  'setdefault',
#  'update',
#  'values']
#
# In [97]: d
# Out[97]: {'name': 'Varma', 1: 1, None: 'None', 'age': 25}
#
# In [98]: d['name']
# Out[98]: 'Varma'
#
# In [99]: d['name'] = 'Ramana'
#
# In [100]: d
# Out[100]: {'name': 'Ramana', 1: 1, None: 'None', 'age': 25}
#
# In [101]: del d[None]
#
# In [102]: d
# Out[102]: {'name': 'Ramana', 1: 1, 'age': 25}
#
# In [103]: d['address'] = 'some address'
#
# In [104]: d
# Out[104]: {'name': 'Ramana', 1: 1, 'age': 25, 'address': 'some address'}
#
# In [105]: help(d.pop)
# Help on built-in function pop:
#
# pop(...) method of builtins.dict instance
#     D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
#     If key is not found, d is returned if given, otherwise KeyError is raised
#
#
# In [106]: d.pop('address')
# Out[106]: 'some address'
#
# In [107]: d
# Out[107]: {'name': 'Ramana', 1: 1, 'age': 25}
#
# In [108]:
#
# In [108]: help(d.popitem)
# Help on built-in function popitem:
#
# popitem(...) method of builtins.dict instance
#     D.popitem() -> (k, v), remove and return some (key, value) pair as a
#     2-tuple; but raise KeyError if D is empty.
#
#
# In [109]: d.pop({'age': 25})
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-109-37e9e71327f3> in <module>
# ----> 1 d.pop({'age': 25})
#
# TypeError: unhashable type: 'dict'
#
# In [110]: d.popitem()
# Out[110]: ('age', 25)
#
# In [111]: d['age'] = 28
#
# In [112]: d
# Out[112]: {'name': 'Ramana', 1: 1, 'age': 28}
#
# In [113]:
#
# In [113]:
#
# In [113]: d['adress'] = 'some addreess'
#
# In [114]: d.popitem()
# Out[114]: ('adress', 'some addreess')
#
# In [115]: d.popitem()
# Out[115]: ('age', 28)
#
# In [116]: d.popitem()
# Out[116]: (1, 1)
#
# In [117]: d
# Out[117]: {'name': 'Ramana'}
#
# In [118]: d
# Out[118]: {'name': 'Ramana'}
#
# In [119]: d.popitem()
# Out[119]: ('name', 'Ramana')
#
# In [120]: d
# Out[120]: {}
#
# In [121]: d.popitem()
# ---------------------------------------------------------------------------
# KeyError                                  Traceback (most recent call last)
# <ipython-input-121-83c64cff336b> in <module>
# ----> 1 d.popitem()
#
# KeyError: 'popitem(): dictionary is empty'
#
# In [122]:
#
# In [122]:
#
# In [122]: ct2 = dict([('a', 1), ('c', 3), ('b', 2)])
#
# In [123]: d = dict([('a', 1), ('c', 3), ('b', 2)])
#
# In [124]:
#
# In [124]: d
# Out[124]: {'a': 1, 'c': 3, 'b': 2}
#
# In [125]:
#
# In [125]: d.has_key('a')
# ---------------------------------------------------------------------------
# AttributeError                            Traceback (most recent call last)
# <ipython-input-125-41bea7058c52> in <module>
# ----> 1 d.has_key('a')
#
# AttributeError: 'dict' object has no attribute 'has_key'
#
# In [126]: help(d)
# Help on dict object:
#
# class dict(object)
#  |  dict() -> new empty dictionary
#  |  dict(mapping) -> new dictionary initialized from a mapping object's
#  |      (key, value) pairs
#  |  dict(iterable) -> new dictionary initialized as if via:
#  |      d = {}
#  |      for k, v in iterable:
#  |          d[k] = v
#  |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
#  |      in the keyword argument list.  For example:  dict(one=1, two=2)
#  |
#  |  Methods defined here:
#  |
#  |  __contains__(self, key, /)
#  |      True if the dictionary has the specified key, else False.
#  |
#  |  __delitem__(self, key, /)
#  |      Delete self[key].
#  |
#  |  __eq__(self, value, /)
#  |      Return self==value.
#  |
#  |  __ge__(self, value, /)
#  |      Return self>=value.
#  |
#  |  __getattribute__(self, name, /)
#  |      Return getattr(self, name).
#  |
#  |  __getitem__(...)
#  |      x.__getitem__(y) <==> x[y]
#  |
#  |  __gt__(self, value, /)
#  |      Return self>value.
#  |
#  |  __init__(self, /, *args, **kwargs)
#  |      Initialize self.  See help(type(self)) for accurate signature.
#  |
#  |  __iter__(self, /)
#  |      Implement iter(self).
#  |
#  |  __le__(self, value, /)
#  |      Return self<=value.
#  |
#  |  __len__(self, /)
#  |      Return len(self).
#  |
#  |  __lt__(self, value, /)
#  |      Return self<value.
#  |
#  |  __ne__(self, value, /)
#  |      Return self!=value.
#  |
#  |  __repr__(self, /)
#  |      Return repr(self).
#  |
#  |  __setitem__(self, key, value, /)
#  |      Set self[key] to value.
#  |
#  |  __sizeof__(...)
#  |      D.__sizeof__() -> size of D in memory, in bytes
#  |
#  |  clear(...)
#  |      D.clear() -> None.  Remove all items from D.
#  |
#  |  copy(...)
#  |      D.copy() -> a shallow copy of D
#  |
#  |  get(self, key, default=None, /)
#  |      Return the value for key if key is in the dictionary, else default.
#  |
#  |  items(...)
#  |      D.items() -> a set-like object providing a view on D's items
#  |
#  |  keys(...)
#  |      D.keys() -> a set-like object providing a view on D's keys
#  |
#  |  pop(...)
#  |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
#  |      If key is not found, d is returned if given, otherwise KeyError is raised
#  |
#  |  popitem(...)
#  |      D.popitem() -> (k, v), remove and return some (key, value) pair as a
#  |      2-tuple; but raise KeyError if D is empty.
#  |
#  |  setdefault(self, key, default=None, /)
#  |      Insert key with a value of default if key is not in the dictionary.
#  |
#  |      Return the value for key if key is in the dictionary, else default.
#  |
#  |  update(...)
#  |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
#  |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
#  |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
#  |      In either case, this is followed by: for k in F:  D[k] = F[k]
#  |
#  |  values(...)
#  |      D.values() -> an object providing a view on D's values
#  |
#  |  ----------------------------------------------------------------------
#  |  Class methods defined here:
#  |
#  |  fromkeys(iterable, value=None, /) from builtins.type
#  |      Create a new dictionary with keys from iterable and values set to value.
#  |
#  |  ----------------------------------------------------------------------
#  |  Static methods defined here:
#  |
#  |  __new__(*args, **kwargs) from builtins.type
#  |      Create and return a new object.  See help(type) for accurate signature.
#  |
#  |  ----------------------------------------------------------------------
#  |  Data and other attributes defined here:
#  |
#  |  __hash__ = None
#
#
# In [127]: d
# Out[127]: {'a': 1, 'c': 3, 'b': 2}
#
# In [128]: d['a']
# Out[128]: 1
#
# In [129]: d['d']
# ---------------------------------------------------------------------------
# KeyError                                  Traceback (most recent call last)
# <ipython-input-129-0d700facf69e> in <module>
# ----> 1 d['d']
#
# KeyError: 'd'
#
# In [130]: d.get('a')
# Out[130]: 1
#
# In [131]: d.get('b')
# Out[131]: 2
#
# In [132]: d.get('c')
# Out[132]: 3
#
# In [133]: d.get('d')
#
# In [134]: help(d.get)
# Help on built-in function get:
#
# get(key, default=None, /) method of builtins.dict instance
#     Return the value for key if key is in the dictionary, else default.
#
#
# In [135]:
#
# In [135]:
#
# In [135]: d.get('d', 'elemenet not exist')
# Out[135]: 'elemenet not exist'
#
# In [136]: d.get('d', defualt = 'elemenet not exist')
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-136-162d8ffbc4f5> in <module>
# ----> 1 d.get('d', defualt = 'elemenet not exist')
#
# TypeError: get() takes no keyword arguments
#
# In [137]: d.get('d', default = 'elemenet not exist')
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-137-400805aaa2f8> in <module>
# ----> 1 d.get('d', default = 'elemenet not exist')
#
# TypeError: get() takes no keyword arguments
#
# In [138]: d.get('d', default='elemenet not exist')
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-138-da8fb41d4e4d> in <module>
# ----> 1 d.get('d', default='elemenet not exist')
#
# TypeError: get() takes no keyword arguments
#
# In [139]: d.get('d', 'elemenet not exist')
# Out[139]: 'elemenet not exist'
#
# In [140]: d.get('d', None)
#
# In [141]: d.keys()
#      ...:
#      ...:
# Out[141]: dict_keys(['a', 'c', 'b'])
#
# In [142]:
#
# In [142]: list(d.keys())
# Out[142]: ['a', 'c', 'b']
#
# In [143]: d.values()
# Out[143]: dict_values([1, 3, 2])
#
# In [144]: tuple(d.values())
# Out[144]: (1, 3, 2)
#
# In [145]: d
# Out[145]: {'a': 1, 'c': 3, 'b': 2}
#
# In [146]: d.items()
# Out[146]: dict_items([('a', 1), ('c', 3), ('b', 2)])
#
# In [147]:
#
# In [147]:
#
# In [147]:
#
# In [147]:
#
# In [147]: a =1
#
# In [148]: b = 1
#
# In [149]: b = 2
#
# In [150]: a
# Out[150]: 1
#
# In [151]: b
# Out[151]: 2
#
# In [152]: a, b = 2, 4
#
# In [153]: a
# Out[153]: 2
#
# In [154]: b
# Out[154]: 4
#
# In [155]: 2, 4
# Out[155]: (2, 4)
#
# In [156]: a, b = (5, 10)
#
# In [157]: a
# Out[157]: 5
#
# In [158]: b
# Out[158]: 10
#
# In [159]: a, b = (5, 10, 15)
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# <ipython-input-159-2aa497b31e0a> in <module>
# ----> 1 a, b = (5, 10, 15)
#
# ValueError: too many values to unpack (expected 2)
#
# In [160]: a, b, v = (5, 10, 15)
#
# In [161]: v
# Out[161]: 15
#
# In [162]: a, b = (5, (10, 15))
#
# In [163]: a
# Out[163]: 5
#
# In [164]: b
# Out[164]: (10, 15)
#
# In [165]: (a, b) = (5, (10, 15))
#
# In [166]: a
# Out[166]: 5
#
# In [167]: b
# Out[167]: (10, 15)
#
# In [168]: d
# Out[168]: {'a': 1, 'c': 3, 'b': 2}
#
# In [169]: d.items()
# Out[169]: dict_items([('a', 1), ('c', 3), ('b', 2)])
#

sentence = "something is happend some days ago for some one, something some else."


'''
---- split
something
is
happend
some
days
ago
for 
some
one,
something
some
else.
---- rstrip - check .  or , in word and strip
something
is
happend
some
days
ago
for 
some
one
something
some
else
------
word_count = {}

{
'something' : 2,
'is' : 1,
'happend' : 1,
'some' : 1,
'days' : 1,
'ago' : 1,
'for' : 1,
'some' : 2,
'one' : 1,
'else' : 1,
}

word = 'something'
word_count = {}

if word not in word_count:
    word_count[word] = 1
else:
    word_count[word] = word_count.get(word) + 1
    

'''




