class ComparableMixin(object):
    def __eq__(self, other):
        if len(self.get_elements()) != len(other):
            return False
        for index, item in enumerate(self.get_elements()):
            if item != other[index]:
                return False
        return True
            
            
    def __ne__(self, other):
        # Relies in __eq__
        if self.__eq__ == True:
            return False
        return True


class SequenceMixin(object):
    def __iter__(self):
        self.index = 0
        return self

        if self.index < len(elements:
        """This method will rely on the get_elements() method of the
        concrete class.
        """
        if not hasattr(self, 'get_elements'):
            raise ValueError("get_elements method not found")
        
        # Keep writing your code here
        elements = self.get_elements()
        if self.index < len(elements):
            index = self.index
            self.index += 1
            return elements[index]
        else:
            raise StopIteration()
        raise NotImplementedError()

    next = __next__

    def __len__(self):
        # Will rely on the iterator
        # can't do len(self.data)
        return self.get_elements.__len__()

    def __getitem__(self, key):
        pass

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass

    def __contains__(self, item):
        # Will rely on the iterator
        if item in self.get_elements


class RepresentableMixin(object):
    def __repr__(self):
        # Will rely on the iterator or __str__
        pass

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
        r[keys for (keys, values) in self.data ]

    def values(self):
        [values for (keys, values) in self.data ]

    def items(self):
        [(keys, values) for (keys, values) in self.data]


class IndexableMixin(object):
    def index(self, x):
        pass
