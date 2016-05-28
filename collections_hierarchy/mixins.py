class ComparableMixin(object):
    def __eq__(self, other):
        self_list = getattr(self, self.DATA_ATTR_NAME)
        other_list = getattr(other, other.DATA_ATTR_NAME)
        self_type = type(self_list)
        other_type = type(other_list)
        
        if self_type != other_type:
            return False
        
        if len(self_list) != len(other_list):
            return False
        
        if self_type == list:
            for x, y in zip(self_list, other_list):
              if x != y:
                return False
        if self_type == dict:
            for x, y in zip(self_list.items(), other_list.items()):
              if x != y:
                  return False
                
        return True
        
    def __ne__(self, other):
        return not self == other

class SequenceMixin(object):
    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        """This method will rely on the get_elements() method of the
        concrete class.
        """
        try:
            getattr(self, 'current')
        except AttributeError:
            self.current = 0
        
        if not hasattr(self, 'get_elements'):
            raise ValueError("get_elements method not found")
            
        elements = self.get_elements()
        
        if len(elements) <= self.current:
            raise StopIteration
        return_elem = elements[self.current]
        self.current += 1
        return return_elem

    next = __next__

    def __len__(self):
        return sum(1 for i in self)

    def __getitem__(self, key):
        return getattr(self, self.DATA_ATTR_NAME)[key]

    def __setitem__(self, key, value):
        getattr(self, self.DATA_ATTR_NAME)[key] = value

    def __delitem__(self, key):
        del getattr(self, self.DATA_ATTR_NAME)[key]

    def __contains__(self, item):
        
        for elem in self:
            if item == elem or item in elem:
                return True
        return False


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
        pass

    def values(self):
        pass

    def items(self):
        pass


class IndexableMixin(object):
    def index(self, x):
        if getattr(self, self.DATA_ATTR_NAME):
            raise IndexError
        return getattr(self, self.DATA_ATTR_NAME)[x]
