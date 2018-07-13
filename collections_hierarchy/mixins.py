class ComparableMixin(object):
    def __eq__(self, other):
        return getattr(self, self.DATA_ATTR_NAME) == getattr(other, other.DATA_ATTR_NAME)

    def __ne__(self, other):
        # Relies in __eq__
        return not self.__eq__(other)


class SequenceMixin(object):
    def __iter__(self):
        self.my_iter = 0
        return self

    def __next__(self):
        """This method will rely on the get_elements() method of the
        concrete class.
        """
        if not hasattr(self, 'get_elements'):
            raise ValueError("get_elements method not found")

        if not hasattr(self, "my_iter"):
            self.my_iter = 0

        if self.my_iter < len(self.get_elements()):
            n = self.get_elements()[self.my_iter]
            self.my_iter += 1
            return n
        else:
            raise StopIteration

    next = __next__

    def __len__(self):
        # Will rely on the iterator
        # can't do len(self.data)
        count = 0
        for d in getattr(self, self.DATA_ATTR_NAME):
            count += 1
        return count

    def count(self):
        return self.__len__()

    def __getitem__(self, key):
        return getattr(self, self.DATA_ATTR_NAME)[key]

    def __setitem__(self, key, value):
        getattr(self, self.DATA_ATTR_NAME)[key] = value

    def __delitem__(self, key):
        del getattr(self, self.DATA_ATTR_NAME)[key]

    def __contains__(self, item):
        # Will rely on the iterator
        return item in getattr(self, self.DATA_ATTR_NAME)


class RepresentableMixin(object):
    def __repr__(self):
        # Will rely on the iterator or __str__
        return str(self)

    def __str__(self):
        # Will rely on the iterator
        return '[{}]'.format(", ".join(str(e) for e in getattr(self, self.DATA_ATTR_NAME))) if getattr(self, self.DATA_ATTR_NAME) else "[]"


class ConstructibleMixin(object):
    DATA_ATTR_NAME = 'data'

    def __init__(self, initial=None):
        setattr(self, self.DATA_ATTR_NAME,
                initial or self.DATA_DEFAULT_INITIAL)


class OperableMixin(object):
    def __add__(self, other):
        obj = type(self)()
        obj.data = getattr(self, self.DATA_ATTR_NAME) + getattr(other, other.DATA_ATTR_NAME)
        return obj

    def __iadd__(self, other):
        return self + other


class AppendableMixin(object):
    def append(self, elem):
        # Relies on DATA_ATTR_NAME = 'data'
        return getattr(self, self.DATA_ATTR_NAME).append(elem)


class HashableMixin(object):
    def keys(self):
        return getattr(self, self.DATA_ATTR_NAME).keys()

    def values(self):
        return getattr(self, self.DATA_ATTR_NAME).values()

    def items(self):
        return getattr(self, self.DATA_ATTR_NAME).items()


class IndexableMixin(object):
    def index(self, x):
        for i, e in enumerate(getattr(self, self.DATA_ATTR_NAME)):
            if e == x:
                return i
        raise ValueError
