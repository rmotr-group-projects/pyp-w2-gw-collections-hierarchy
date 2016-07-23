from copy import deepcopy

class ComparableMixin(object):
    def __eq__(self, other):
        # Not sure if this is a cop out
        return self.data == other.data
        
        # if isinstance(self,type(None)) or isinstance(other,type(None)):
        #     return False
        # try: 
        #     if len(self.data) != len(other.data):
        #         return False
        # except StopIteration, e:
        #     pass
        # compare_index = 0
        # for item in self.get_elements():
        #     if item != other.get_elements()[compare_index]:
        #         return False
        #     compare_index += 1
        # return True
            
    def __ne__(self, other):
        # Relies on __eq__
        if self == other:
            return False
        return True


class SequenceMixin(object):
    def __iter__(self):
        self.iter_index = 0
        return self

    def __next__(self):
        """This method will rely on the get_elements() method of the
        concrete class.
        """
        if not hasattr(self, 'get_elements'):
            raise ValueError("get_elements method not found")
        # Keep writing your code here
        elements = self.get_elements()
        if elements < 1:
            return None
        if self.iter_index < len(elements):
            index = self.iter_index
            self.iter_index += 1
            return elements[index]
        else:
            raise StopIteration()
        raise NotImplementedError()

    next = __next__

    def __len__(self):
        # Will rely on the iterator
        # can't do len(self.data)
        length = 0
        for item in self:
            length += 1
        return length
        
        # return self.data.__len__()

    def __getitem__(self, key):
        return self.data[key]
    
    def __setitem__(self, key, value):
        self.data[key] = value
        return self

    def __delitem__(self, key):
        del self.data[key]
        return self

    def __contains__(self, item):
        # Will rely on the iterator
        # return self.data.__contains__(item)
        for element in self.data:
            if item == element:
                return True
        return False

    def count(self):
        return len(self)

class RepresentableMixin(object):
    def __repr__(self):
        # Will rely on the iterator or __str__
        return self.data.__repr__()

    def __str__(self):
        # Will rely on the iterator
        return self.data.__str__()


class ConstructibleMixin(object):
    DATA_ATTR_NAME = 'data'

    def __init__(self, initial=None):
        setattr(self, self.DATA_ATTR_NAME,
                initial or self.DATA_DEFAULT_INITIAL)
        self.iter_index = 0


class OperableMixin(object):
    def __add__(self, other):
        # Should only work with .data
        # new_self = deepcopy(self)
        # for item in other:
        #     new_self.data.append(item)
        # return new_self

        new_self = deepcopy(self)
        for item in other.data:
            new_self.data.append(item)
        return new_self

    def __iadd__(self, other):
        return self + other


class AppendableMixin(object):
    def append(self, elem):
        # Relies on DATA_ATTR_NAME = 'data'
        self.data.append(elem)
        return None


class HashableMixin(object):
    def keys(self):
        return [keys for (keys,values) in self]

    def values(self):
        return [values for (keys, values) in self]

    def items(self):
        return [(keys, values) for (keys, values) in self]


class IndexableMixin(object):
    def index(self, x):
        index_value = 0
        matched = False
        for item in self:
            if x == item:
                return index_value
            index_value += 1
        raise ValueError
