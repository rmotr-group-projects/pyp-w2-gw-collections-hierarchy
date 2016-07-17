class ComparableMixin(object):
    def __eq__(self, other):
        return self.data == other
        
    def __ne__(self, other):
        # Relies in __eq__
        return False if self.data == other else True

class SequenceMixin(object):
    def __iter__(self):
        self.elements = self.get_elements()
        self.length = len(self.elements)
        self.index = 0
        return self
        
    def __next__(self):
        if not hasattr(self, 'get_elements'):
            raise ValueError("get_elements method not found")
        if not hasattr(self, 'elements'):
            self.__iter__()
        while self.index <= self.length-1:
            elem = self.elements[self.index]
            self.index += 1
            return elem
        raise StopIteration()

    next = __next__

    def __len__(self):
        data = getattr(self, self.DATA_ATTR_NAME)
        if data:
            for index, item in enumerate(data):
                pass
            return index+1
        else:
            return 0

    def __getitem__(self, key):
        return self.data[key]
        
    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        data = getattr(self, self.DATA_ATTR_NAME)
        if isinstance(data, list):
            if len(data) == 0:
                raise IndexError()
            if key >= len(self):
                raise KeyError()
            new_elems = []
            for count, elem in enumerate(data):
                if count != key:
                    new_elems.append(elem)
            self.data = new_elems

        if isinstance(data, dict):
            if key not in data or len(data)==0:
                raise KeyError()
            new_elems = {}
            for elem in data:
                if elem != key:
                    new_elems[elem] = data[elem]
            self.data = new_elems

    def __contains__(self, item):
        for elem in getattr(self, self.DATA_ATTR_NAME):
            if elem == item:
                return True
        return False
        
class RepresentableMixin(object):
    def __repr__(self):
        # Will rely on the iterator or __str__
        return str(self)

    def __str__(self):
        # Will rely on the iterator
        elem_str = '['
        count = 1
        elements = getattr(self, self.DATA_ATTR_NAME)
        for elem in elements:
            if count < len(elements):
                elem_str += str(elem) + ', '
            else:
                elem_str += str(elem) + ']'
            count += 1
        return elem_str
        
class ConstructibleMixin(object):
    DATA_ATTR_NAME = 'data'
    def __init__(self, initial=None):
        setattr(self, self.DATA_ATTR_NAME,
                initial or self.DATA_DEFAULT_INITIAL)
        '''For example, setattr(x, 'foobar', 123) is equivalent to x.foobar = 123.'''

class OperableMixin(object):
    def __add__(self, other):
        return self.__class__([n for n in getattr(self, self.DATA_ATTR_NAME)] + \
                              [n for n in getattr(other, other.DATA_ATTR_NAME)])

    def __iadd__(self, other):
        return self + other

class AppendableMixin(object):
    def append(self, elem):
        # Relies on DATA_ATTR_NAME = 'data'
        data = getattr(self, self.DATA_ATTR_NAME) 
        data += [elem]

class HashableMixin(object):
    def keys(self):
        return list(self.data.keys())

    def values(self):
        return [i for i in self.data.values()] 
        
    def items(self):
        return [i for i in self.data.items()]

class IndexableMixin(object):
    def index(self, x):
        elements = getattr(self, self.DATA_ATTR_NAME)
        for count, elem in enumerate(elements):
            if elem == x:
                return count
        else:
            raise ValueError()
