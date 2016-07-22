class ComparableMixin(object):
    def __eq__(self, other):
        return self
        
    def __ne__(self, other):
        return self


class SequenceMixin(object):
    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        """This method will rely on the get_elements() method of the
        concrete class.
        """
        if not hasattr(self, 'get_elements'):
            raise ValueError("get_elements method not found")
    
        elements = self.get_elements()
        if self.i == len(elements):
            raise StopIteration()
        self.i += 1
        # if isinstance(self, Dict):
            
        return elements[self.i - 1]
            
    next = __next__

    def __len__(self):
        counter = 0
        for a in getattr(self, self.DATA_ATTR_NAME):
            counter += 1
        return counter
    
    count = __len__

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value
        return self.data[key]

    def __delitem__(self, key):
        return self.data.pop(key)

    def __contains__(self, item):
        return item in self.data


class RepresentableMixin(object):
    def __repr__(self):
        # Will rely on the iterator or __str__
        return str(self.get_elements())

    def __str__(self):
        # Will rely on the iterator
        return str(self.get_elements())


class ConstructibleMixin(object):
    DATA_ATTR_NAME = 'data'

    def __init__(self, initial=None):
        self.i = 0
        setattr(self, self.DATA_ATTR_NAME,
                initial or self.DATA_DEFAULT_INITIAL)


class OperableMixin(object):
    def __add__(self, other):
        new_self = self.__class__()
        l = self.data + other.data
        setattr(new_self, 'data', l)
        return new_self

    def __iadd__(self, other):
        self.data = list(self.data) + list(other)
        return self.data


class AppendableMixin(object):
    def append(self, elem):
        self.data.append(elem)

class HashableMixin(object):
    def keys(self):
        return [key for key in self.data]

    def values(self):
        return [self.data[key] for key in self.data]

    def items(self):
        return [(key, self.data[key]) for key in self.data]


class IndexableMixin(object):
    def index(self, x):
        i = 0
        for i, item in enumerate(self.data):
            if item == x:
                return i
        raise ValueError