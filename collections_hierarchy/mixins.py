from copy import deepcopy

class ComparableMixin(object): # Subclassed in List & Dict
    def __eq__(self, other):
        data = getattr(
            self,
            self.DATA_ATTR_NAME
        )
        data2 = getattr(
            other,
            other.DATA_ATTR_NAME
        )
        return data == data2

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        data = getattr(
            self,
            self.DATA_ATTR_NAME
        )
        data2 = getattr(
            other,
            other.DATA_ATTR_NAME
        )
        return data < data2

    def __gt__(self, other):
        data = getattr(
            self,
            self.DATA_ATTR_NAME
        )
        data2 = getattr(
            other,
            other.DATA_ATTR_NAME
        )
        return data > data2

    def __le__(self, other):
        return not self > other

    def __ge__(self, other):
        return not self < other


class SequenceMixin(object): # Subclassed in List & Dict
    def __iter__(self):
        return iter(self.get_elements())

    def __next__(self):
        return next(iter(self))

    next = __next__

    def __len__(self):
        return sum([1 for item in self])
    
    def count(self):
        return len(self)

    def __getitem__(self, key):
        data = getattr(
            self,
            self.DATA_ATTR_NAME
        )
        return data[key]

    def __setitem__(self, key, value):
        data = getattr(
            self,
            self.DATA_ATTR_NAME
        )
        data[key] = value

    def __delitem__(self, key):
        data = getattr(
            self,
            self.DATA_ATTR_NAME
        )
        del data[key]

    def __contains__(self, item):
        return any([elem == item for elem in self])


class RepresentableMixin(object): # Subclassed in List & Dict
    def __repr__(self):
        return str(self)

    def __str__(self):
        data = getattr(
            self,
            self.DATA_ATTR_NAME
        )
        return str(data)


class ConstructibleMixin(object): # Subclassed in List & Dict
    DATA_ATTR_NAME = 'data'

    def __init__(self, initial=None):
        setattr(
            self,
            self.DATA_ATTR_NAME,
            initial or self.DATA_DEFAULT_INITIAL
        )
        
        
class OperableMixin(object): # Subclassed in List
    def __add__(self, other):
        new_obj = deepcopy(self)
        for elem in other:
            new_obj.append(elem)
        return new_obj

    def __iadd__(self, other):
        return self + other


class AppendableMixin(object): # Subclassed in List
    def append(self, elem):
        self[len(self):] = [elem]


class HashableMixin(object): # Subclassed in Dict
    def keys(self):
        return list(iter(self))

    def values(self):
        return [self[key] for key in self.keys()]

    def items(self):
        return [(key, self[key]) for key in self.keys()]


class IndexableMixin(object): # Subclassed in List
    def index(self, x):
        for i, elem in enumerate(self):
            if elem == x:
                return i
        
        raise ValueError('item "{}" not found'.format(x))