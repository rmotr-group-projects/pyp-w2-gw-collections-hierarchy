#from collections_hierarchy.main_collections import *
from functools import reduce

# LIST & DICT
class ComparableMixin(object):
    def __eq__(self, other):
        if other is None:
            return False
        return self.data == other.data
    
    def __ne__(self, other):
        return not self == other

# LIST & DICT
class SequenceMixin(object):
    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        """This method will rely on the get_elements() method of the
        concrete class.
        """
        if not hasattr(self, 'get_elements'):
            raise ValueError("get_elements method not found")
        data_list = self.get_elements()
        if self.counter == len(data_list):
            raise StopIteration()
        self.counter += 1
        return data_list[self.counter-1]
        

    next = __next__

    def __len__(self):
        return reduce(lambda x, y: x + 1, [n for n in self], 0)
        
    count = __len__

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __contains__(self, item):
        # Will rely on the iterator
        for val in self:
            if val == item:
                return True
        return False
        

# LIST & DICT
class RepresentableMixin(object):
    def __repr__(self):
        return str(self)

    def __str__(self):
        if type(self.data) is list:
            return '[' + ', '.join(str(element) for element in self) + ']'
        elif type(self.data) is dict:
            return '{' + ', '.join("'" + str(key) + "': " + str(self[key]) for key in self) + '}'
            

# LIST & DICT
class ConstructibleMixin(object):
    DATA_ATTR_NAME = 'data'

    def __init__(self, initial=None):
        self.counter = 0
        setattr(self, self.DATA_ATTR_NAME,
                initial or self.DATA_DEFAULT_INITIAL)


# LIST ONLY
class OperableMixin(object):
    def __add__(self, other):
        new_list = self.data + other.data
        return type(self)(new_list)
        
    def __iadd__(self, other):
        for n in other:
            self.data.append(n)
        return self

# LIST ONLY
class AppendableMixin(object):
    def append(self, elem):
        # Relies on DATA_ATTR_NAME = 'data'
        self.data.append(elem)

# DICT ONLY
class HashableMixin(object):
    def keys(self):
        return list(self.data.keys())

    def values(self):
        return list(self.data.values())

    def items(self):
        return list(self.data.items())


# LIST ONLY
class IndexableMixin(object):
    def index(self, x):
        for i, elem in enumerate(self):
            if elem == x:
                return i
        raise ValueError()




