class ComparableMixin(object):
    def __eq__(self, other):
        attr1 = getattr(self, self.DATA_ATTR_NAME)
        attr2 = getattr(other, other.DATA_ATTR_NAME)
        return attr1 == attr2
        
    def __ne__(self, other):
        # Relies in __eq__
        return not (self == other) #same as calling self.__eq__(other)


class SequenceMixin(object):
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        """This method will rely on the get_elements() method of the
        concrete class.
        """
        if not hasattr(self, 'get_elements'):
            raise ValueError("get_elements method not found")

        if not hasattr(self, 'index'):
        return 
        
        elem_list = self.get_elements()
        if self.index < len(elem_list):
            elem = elem_list[self.index]
            self.index +=1
            return elem
        else:
            raise StopIteration()

    next = __next__

    def __len__(self):
        # Will rely on the iterator
        num = 0
        for i in self.data: 
            num += 1
        return num
        

    def __getitem__(self, key):
        pass

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass

    def __contains__(self, item):
        # Will rely on the iterator
        @if val in self:
            return True
        


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
        data=getattr(self, self.DATA_ATTR_NAME)
        data+=[elem]
        return self.data


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
