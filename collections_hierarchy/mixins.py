class ComparableMixin(object):
    def __eq__(self, other):
        return self.data == other.data
    def __ne__(self, other):
        # Relies in __eq__
        return not self.__eq__(other)


class SequenceMixin(object):
    def __iter__(self):
        pass

    def __next__(self):
        """This method will rely on the get_elements() method of the
        concrete class.
        """
        if not hasattr(self, 'get_elements'):
            raise ValueError("get_elements method not found")
        # Keep writing your code here
        raise NotImplementedError()

    next = __next__

    def __len__(self):
        # Will rely on the iterator
        # can't do len(self.data)
        pass

    def __getitem__(self, key):
        pass

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass

    def __contains__(self, item):
        # Will rely on the iterator
        pass


class RepresentableMixin(object):
    def __repr__(self):
        # Will rely on the iterator or __str__
        return str(self)

    def __str__(self):
        # Will rely on the iterator
        pass


class ConstructibleMixin(object):
    DATA_ATTR_NAME = 'data'

    def __init__(self, initial=None):
        setattr(self, self.DATA_ATTR_NAME,
                initial or self.DATA_DEFAULT_INITIAL)


class OperableMixin(object):
    def __add__(self, other):
        pass

    def __iadd__(self, other):
        pass


class AppendableMixin(object):
    def append(self, elem):
        # Relies on DATA_ATTR_NAME = 'data'
        pass


class HashableMixin(object):
    def keys(self):
        pass

    def values(self):
        pass

    def items(self):
        pass


class IndexableMixin(object):
    def index(self, x):
        pass
