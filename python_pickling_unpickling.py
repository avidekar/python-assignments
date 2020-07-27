# tested on python3.8 version

import pickle
import types

class PythonPickle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = lambda c: c*c

    def __getstate__(self):

        del_list = []
        attributes = self.__dict__.copy()
        for key, value in attributes.items():
            if type(value) is types.LambdaType:
                del_list.append(key)

        for item in del_list:
            del attributes[item]

        return attributes

a_obj = PythonPickle(3, 6, 9)
# pickle class instance

# Whenever an object is pickled, the __reduce__ method defined by it gets called. This method
# returns either a string, which may represent the name of a Python global, or a tuple describing
# how to reconstruct this object when unpickling.

pickled_a_obj = pickle.dumps(a_obj)
print(pickled_a_obj)
# unpickle class instance
unpickled_a_obj = pickle.loads(pickled_a_obj)
print(unpickled_a_obj)