class ComparableMixin(object):
    def __eq__(self, other):
        for x, y in zip(self, other):
            if not x == y:
                pass
            else:
                return self == other

    def __ne__(self, other):
        for x, y in zip(self, other):
            if x == y:
                pass
            else:
                return not self == other

    def __lt__(self, other):
        return self < other

    def __gt__(self, other):
        return self > other

    def __le__(self, other):
        return self <= other

    def __ge__(self, other):
        return self >= other


class SequenceMixin(object):
    def __iter__(self):
        self.n = 0
        self.elements = self.get_elements()
        return(self)

    def __next__(self):
        while self.n < len(self.elements):
            element = self.elements[self.n]
            self.n += 1
            return element

        raise StopIteration
            
    next = __next__

    def __len__(self):
        return len(self)

    def __getitem__(self, key):
        return self[key]

    def __setitem__(self, key, value):
        self[key] = value

    def __delitem__(self, key):
        del self[key]

    def __contains__(self, item):
        return item in self.elements


class RepresentableMixin(object):
    def __repr__(self):
        return str(self.elements)

    def __str__(self):
        return str(self.elements)


class ConstructibleMixin(object):
    DATA_ATTR_NAME = 'data'

    def __init__(self, initial=None):
        self.initial = initial or self.DATA_DEFAULT_INITIAL
        setattr(self, self.DATA_ATTR_NAME, self.initial)
        

class OperableMixin(object):
    def __add__(self, other):
        return self.elements + other.elements

    def __iadd__(self, other):
        return self.data + other.data


class AppendableMixin(object):
    def append(self, elem):
        return self.elements.append(elem)


class HashableMixin(object):
    def keys(self):
        return self.elements.keys()

    def values(self):
        return self.elements.values()

    def items(self):
        return self.elements.items()


class IndexableMixin(object):
    def index(self, x):
        return self[x]
