import numpy as np
import pandas as pd
from pprint import pprint


def func1():
    # Constructing a Pandas' Series 1: Using a Value-List and an Index-List.
    s1 = pd.Series([5, 7, 3, 4, 5], index=['a', 'b', 'c', 'a', 'd'], name='x') # Not unique index

    pprint(s1)
    pprint(s1.index)
    pprint(s1.values)
    pprint(s1.name)
    pprint(s1.dtype)


def func2():
    # Accessing the Series: Indexing [idx], Dot .idx, and Slicing [start:stop:step]
    s1 = pd.Series([5, 7, 2, 5, 3], index=['a', 'b', 'c', 'd', 'a'], name='x')

    print(s1['a'])
    print(type(s1['a']))

    print(s1.b)
    print(type(s1.b))

    # slicing via index
    pprint(s1['b': 'd'])
    pprint(type(s1['b': 'd']))

    pprint(s1['b': 'd': 2]) # slicing with step

    # An numeric row-index starting from 0 is also maintained
    pprint(s1[::2])


def func3():
    s1 = pd.Series([5, 7, 2, 5, 3], index=['a', 'b', 'c', 'd', 'a'], name='x')

    # Selection with a List of Indexes
    # pprint(s1[['a', 'c']])

    # Element-wise Operations
    s1['a'] = 0
    pprint(s1)

    # Constructing a Pandas' Series 2: From a Value-List with Default Numeric Index
    s2 = pd.Series([5, 7, 2, 7, 3])
    # pprint(s2.index)

    # Constructing a Pandas' Series 3: From a NumPy's 1D ndarray
    arr1d = np.array([1.1, 2.2, 3.3, 4.4])
    s3 = pd.Series(arr1d, index=['a', 'b', 'c', 'd'])
    s3[0] = 99
    pprint(s3)


def func4():
    s1 = pd.Series([11, 22, 33, 44], index=['a', 'b', 'c', 'd'])
    s2 = pd.Series(s1)

    s1[1] = 99
    # pprint(s2)

    # Constructing a Pandas' Series 5: From a Python's Dictionary as Index-Value Pairs
    d = {'a': 11, 'b': 22, 'c': 33, 'd': 44}  # keys are unique in dictionary
    s1 = pd.Series(d)
    # pprint(s1)

    # If index is provided, match index with the dict's key
    s2 = pd.Series(d, index=['b', 'd', 'a', 'c', 'aa'])
    pprint(s2)


def func5():
    """ Series operations"""
    # Operations between a Series and a Scalar
    s1 = pd.Series([5, 4, 3, 2, 1], index=['a', 'b', 'c', 'd', 'e'])

    # pprint(s1 + 1)
    # pprint(s1 > 3)
    # pprint(s1[s1 > 3])

    # Operations between Two Series are Index-based
    s1 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
    s2 = pd.Series([4, 3, 2, 1], index=['c', 'a', 'b', 'aa'])

    pprint(s1 + s2)


def func6():
    # Statistical Methods on Series
    s1 = pd.Series([5, 4, 3, 2, 1], index=['a', 'b', 'c', 'd', 'e'])
    # pprint(np.sum(s1))
    # pprint(s1.sum())
    # pprint(s1.cumsum())

    m1 = np.arange(12, dtype=float).reshape(3, 4)
    m1[0, 1] = np.nan
    pprint(m1)
    pprint(m1.sum())
    pprint(m1.sum(axis=0))

    s1 = pd.Series([1, 2, np.NaN, 4, 5])
    pprint(s1)
    pprint(s1.sum())

    s1 = pd.Series([3, 2, 2, 1, np.nan, 6, 8, 4], index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
    pprint(s1.describe())

    pprint(s1.std())


# func1()
# func2()
# func3()
# func4()
#func5()

func6()
