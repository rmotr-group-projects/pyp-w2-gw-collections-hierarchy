class ComparableMixin(object):
    def __eq__(self, other):
        if self.data == other.data:
            return True
        return False

    def __ne__(self, other):
        # Relies in __eq__
        return not self.__eq__(other)
        


class SequenceMixin(object):

    def __init__(self, counter=0):
        self.counter = counter

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        """This method will rely on the get_elements() method of the
        concrete class.
        """
        try:
            self.counter
        except AttributeError:
            self.counter = 0
        if not hasattr(self, 'get_elements'):
            raise ValueError("get_elements method not found")
        data = self.get_elements()
        try:
            if isinstance(data[0], tuple):
                return_val = data[self.counter][0]
            if not isinstance(data[0], tuple):
                return_val = data[self.counter]
            self.counter += 1
        except IndexError:
            raise StopIteration
        return return_val
    
    next = __next__

    def __len__(self):
        # Will rely on the iterator
        # can't do len(self.data)
        len_count = 0
        for elem in self:
            len_count += 1
        return len_count
        
    def count(self):
        return len(self)
        
    def __getitem__(self, key):
        elements = self.get_elements()
        if not elements and isinstance(key, str):
            raise KeyError
        if isinstance(elements[0], tuple):
            for element in elements:
                if element[0] == key:
                    return element[1]
            raise KeyError
        return elements[key]
        
    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __contains__(self, item):
        # Will rely on the iterator
        for x in self.get_elements():
            if isinstance(x, tuple):
                if item == x[0]:
                    return True
            if item == x:
                return True
        return False


class RepresentableMixin(object):
    def __repr__(self):
        # Will rely on the iterator or __str__
        return str(self)

    def __str__(self):
        # Will rely on the iterator
        return_val = None
        for x in self.get_elements():
            if isinstance(x, tuple):
                if not return_val:
                    return_val = {}
                return_val[x[0]] = x[1]
                continue
            if not return_val:
                return_val = []
            return_val.append(x)
        
        return str(return_val)


class ConstructibleMixin(object):
    DATA_ATTR_NAME = 'data'

    def __init__(self, initial=None):
        setattr(self, self.DATA_ATTR_NAME,
                initial or self.DATA_DEFAULT_INITIAL)


class OperableMixin(object):
    def __add__(self, other):
        new_obj = object.__new__(self.__class__)
        new_obj.data = self.data + other.data
        return new_obj

    def __iadd__(self, other):
        self.data = self.data + other.data
        return self
        
class AppendableMixin(object):
    def append(self, elem):
        # Relies on DATA_ATTR_NAME = 'data'
        self.data.append(elem)


class HashableMixin(object):
    def keys(self):
       return [x[0] for x in self.get_elements()] 

    def values(self):
       return [x[1] for x in self.get_elements()]

    def items(self):
        return self.get_elements()


class IndexableMixin(object):
    def index(self, x):
        if not isinstance(x, int):
            raise ValueError
        counter = 0
        for item in self.get_elements():
            if item == x:
                return counter
            counter += 1
