# __iter__ method that is called on initialization of an iterator. This should return an object
# that has a next or __next__ (in Python 3) method.
# next ( __next__ in Python 3) The iterator next method should return the next value for the
# iterable. When an iterator is used with a ‘for in’ loop, the for loop implicitly calls next()
# on the iterator object. This method should raise a StopIteration to signal the end of the
# iteration.

# How an iterator really works in Python
# value = "Geeks"
# iter_obj = iter(value)
# print(iter_obj)
#
# while True:
#     try:
#         item = next(iter_obj)
#         print(item)
#     except StopIteration:
#         break

class Test:
    def __init__(self, limit):
        self.limit = limit

    # called when iteration is initiliazed
    def __iter__(self):
        print("__iter__ function called")
        self.x = 10
        return self

    # To move to next element. In python3
    # we need to replace next with __next__
    def __next__(self):
        print("__next__ function called")
        x = self.x

        # Stop iteration if limit is reached
        if x > self.limit:
            raise StopIteration

        # Else increment and return old value
        self.x = x + 1
        return x


for index in Test(15):
    print(index)

for index in Test(5):
    print(index)