class ComparableMixin(object):
    def __eq__(self, other):
        return self == other

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return len(self) < len(other)

    def __gt__(self, other):
        return len(self) > len(other)

    def __le__(self, other):
        return len(self) <= len(other)

    def __ge__(self, other):
        return len(self) >= len(other)


class SequenceMixin(object):
    def __iter__(self):
        return iter(self)

    def __next__(self):
        if isinstance(self.values, list):
            if self.i > len(self.values) - 1:
                raise StopIteration
            else:
                self.i += 1
                return self.values[self.i]
                
        #if isistance(self.values, dict):
                
                 
            

    next = __next__

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    def __contains__(self, item):
        return item in self


class RepresentableMixin(object):
    def __repr__(self):
        return "%s" % type(object)

    def __str__(self):
        #return("{}".format(self)) -> recursion error
        return "%s" % self
        

class ConstructibleMixin(object):
    DATA_ATTR_NAME = 'data'

    def __init__(self, initial=None):
        self.initial = initial


class OperableMixin(object):
    def __add__(self, other):
        return self + other

    def __iadd__(self, other):
        self = self + other


class AppendableMixin(object):
    def append(self, elem):
        return self.append(elem)


class HashableMixin(object):
    def keys(self):
        return self

    def values(self):
        return self.values()

    def items(self):
        return self.items()


class IndexableMixin(object):
    def index(self, x):
        return self[x]
