class ComparableMixin(object):

    def __eq__(self, other):
        self_data = getattr(self, self.DATA_ATTR_NAME)
        other_data = getattr(other, other.DATA_ATTR_NAME)
        return self_data == other_data

    def __ne__(self, other):
        return self


class SequenceMixin(object):

    def __iter__(self):
        self.idx = -1
        return self

    def __next__(self):
        if not hasattr(self, 'get_elements'):
            raise ValueError("get_elements method not found")
        elements = self.get_elements()
        
        if not hasattr(self, 'idx'):
            self.idx = 0
        else:
            self.idx += 1

        if self.idx >= len(elements):
            raise StopIteration

        return elements[self.idx]

    next = __next__

    def __len__(self):
        count = 0
        for element in self:
            count += 1
        return count

    def __getitem__(self, key):
        return getattr(self, self.DATA_ATTR_NAME)[key]

    def __setitem__(self, key, value):
        getattr(self, self.DATA_ATTR_NAME)[key] = value

    def __delitem__(self, key):
        del getattr(self, self.DATA_ATTR_NAME)[key]

    def __contains__(self, item):
        return any(str(item) in str(element) for element in self)

    def count(self):
        return len(self)


class RepresentableMixin(object):

    def __str__(self):
        return str([elem for elem in self])

    def __repr__(self):
        return str(self)

class ConstructibleMixin(object):
    DATA_ATTR_NAME = 'data'

    def __init__(self, initial=None):
        setattr(self, self.DATA_ATTR_NAME,
                initial or self.DATA_DEFAULT_INITIAL)


class OperableMixin(object):

    def __add__(self, other):
        self_data = getattr(self, self.DATA_ATTR_NAME)
        other_data = getattr(other, other.DATA_ATTR_NAME)
        return self.__class__(self_data + other_data)

    def __iadd__(self, other):
        self = self + other
        return self


class AppendableMixin(object):

    def append(self, elem):
        getattr(self, self.DATA_ATTR_NAME).append(elem)


class HashableMixin(object):

    def keys(self):
        self_data = getattr(self, self.DATA_ATTR_NAME)
        return [key for key in self_data]

    def values(self):
        self_data = getattr(self, self.DATA_ATTR_NAME)
        return [self_data[key] for key in self_data]

    def items(self):
        self_data = getattr(self, self.DATA_ATTR_NAME)
        return [(key, self_data[key]) for key in self_data]


class IndexableMixin(object):

    def index(self, x):
        for idx, element in enumerate(self):
            if element == x:
                return idx
        raise ValueError
