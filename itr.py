class RangeDown:
    """Iterator from max down to min (both inclusive)"""

    def __init__(self, min, max):
        self.current = max + 1
        self.min = min

    def __iter__(self):
        return self

    def __next__(self):
        self.current -= 1
        if self.current < self.min:
            raise StopIteration
        else:
            return self.current


if __name__ == '__main__':
    # Use iter() and next()
    itr = iter(RangeDown(6, 8)) # self.min = 6, self.current = 9  --> b

    print(next(itr))  # 8
    print(next(itr))  # 7
    print(next(itr))  # 6
    # print(next(itr))  # StopIteration

    # Iterate in for-in loop
    for i in RangeDown(6, 8):
        print(i, end=" ")  # 8 7 6
    print()

    # Use __iter__() and __next__()
    itr2 = RangeDown(9, 10).__iter__()
    print(itr2.__next__())  # 10
    print(itr2.__next__())  # 9
    print(itr2.__next__())  # StopIteration