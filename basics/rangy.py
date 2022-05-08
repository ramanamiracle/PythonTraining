def range_down(min, max):
   """A generator function contains yield statement and creates a generator iterator object"""
   current = max
   while current >= min:
       yield current # 8 | 7 | 6 | 5|
       current -= 1   # Count down


for i in range_down(5, 100000):
   print(i, end=" ")  # 8 7 6 5