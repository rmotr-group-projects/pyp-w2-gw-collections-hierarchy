class ComparableMixin(object):
    def __eq__(self, other):
        self_data = getattr(self, self.DATA_ATTR_NAME)
        other_data = getattr(other, other.DATA_ATTR_NAME)
        return self_data == other_data
            
    def __ne__(self, other):
        return not self.data == other.data


class SequenceMixin(object):
    
    def __iter__(self):
        self.index = 0
        self.elements = self.get_elements()
        return self

    def __next__(self):
        """This method will rely on the get_elements() method of the
        concrete class.
        """
        if not hasattr(self, 'get_elements'):
            raise ValueError("get_elements method not found")

        if self.index >= len(getattr(self, self.DATA_ATTR_NAME)):
            raise StopIteration()
        
        value = self.elements[self.index]
        self.index += 1
        return value

    next = __next__

    def __len__(self):
        count = 0
        for elem in getattr(self, self.DATA_ATTR_NAME):
            count += 1
        return count
        
    def __getitem__(self, key):
        return getattr(self, self.DATA_ATTR_NAME)[key]

    def __setitem__(self, key, value):
        getattr(self, self.DATA_ATTR_NAME)[key] = value
        
    def __delitem__(self, key):
        del getattr(self, self.DATA_ATTR_NAME)[key]

    def __contains__(self, item):
        return item in getattr(self, self.DATA_ATTR_NAME)


class RepresentableMixin(object):
    def __repr__(self):
        # Will rely on the iterator or __str__
        pass

    def __str__(self):
        # Will rely on the iterator
        return "{}".format(getattr(self, self.DATA_ATTR_NAME))


class ConstructibleMixin(object):
    DATA_ATTR_NAME = 'data'

    def __init__(self, initial=None):
        setattr(self, self.DATA_ATTR_NAME,
                initial or self.DATA_DEFAULT_INITIAL)
        
class OperableMixin(object):
    def __add__(self, other):
        aux_list = []
        for elem in self.data:
            aux_list.append(elem)
            
        for elem in other.data:
            aux_list.append(elem)
            
        return self.__class__(aux_list)

    def __iadd__(self, other):
        for elem in getattr(other, other.DATA_ATTR_NAME):
            getattr(self, self.DATA_ATTR_NAME).append(elem)
        return self


class AppendableMixin(object):
    def append(self, elem):
        self.data.append(elem)


class HashableMixin(object):
    def keys(self):
        return getattr(self, self.DATA_ATTR_NAME).keys()

    def values(self):
        return getattr(self, self.DATA_ATTR_NAME).values()

    def items(self):
        return getattr(self, self.DATA_ATTR_NAME).items()


class IndexableMixin(object):
    def index(self, x):
        for index, value in enumerate(getattr(self, self.DATA_ATTR_NAME)):
            if value == x:
                return index
        raise ValueError
