from copy import deepcopy

class ComparableMixin(object):
    #Implements comparison functionality. Common for List and Dict
    def __eq__(self, other):
        data1 = getattr(self, self.DATA_ATTR_NAME) #Get the value of the property that stores the data
        data2 = getattr(other, other.DATA_ATTR_NAME)
        
        if isinstance(data1, dict):
            return data1 == data2
        else:
            return sorted(data1) == sorted(data2)
        
    def __ne__(self, other):
        return not self.__eq__(other)

class SequenceMixin(object):
    def __iter__(self):
        elems = self.get_elements()
        self.iterator = iter(elems)
        return self
    
    def __next__(self):
        """This method will rely on the get_elements() method of the
        concrete class.
        """
        if not hasattr(self, 'get_elements'):
            raise ValueError("get_elements method not found")

        try:
            self.iterator
        except:
            self.iterator = iter(self.get_elements())
        return next(self.iterator)
       


    next = __next__

    def __len__(self):
        # uses the iterator to provide a count of the items
        c = 0
        for d in self:
            c += 1
        return c
    
    count = __len__

    def __getitem__(self, key):
        return getattr(self, self.DATA_ATTR_NAME)[key]

    def __setitem__(self, key, value):
        getattr(self, self.DATA_ATTR_NAME)[key] = value

    def __delitem__(self, key):
        del getattr(self, self.DATA_ATTR_NAME)[key]

    def __contains__(self, item):
        # Will rely on the iterator
        for d in self:
            if d == item:
                return True 
        return False

class RepresentableMixin(object):
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        # Will rely on the iterator
        l = ", ".join([ str(n) for n in self])
        s = self.DATA_ATTR_NAME
        
        if type(getattr(self, s)) is list:
            return '{}{}{}'.format('[', l, ']')
        elif type(getattr(self, s)) is dict:
            return '{}{}{}'.format('{', l, '}')
        

class ConstructibleMixin(object):
    DATA_ATTR_NAME = 'data'

    def __init__(self, initial=None):
        setattr(self, self.DATA_ATTR_NAME,
                initial or self.DATA_DEFAULT_INITIAL)


class OperableMixin(object):
    def __add__(self, other):
        new_list = deepcopy(self)
        new_list.data += other.data
        return new_list

    def __iadd__(self, other):
        return self.__add__(other)


class AppendableMixin(object):
    def append(self, elem):
        # Relies on DATA_ATTR_NAME = 'data'
        s = getattr(self, self.DATA_ATTR_NAME)
        
        if type(s) is list:
            s.append(elem)

class HashableMixin(object):
    def keys(self):
        s = getattr(self, self.DATA_ATTR_NAME)
        return sorted([n for n in s])

    def values(self):
        s = getattr(self, self.DATA_ATTR_NAME)
        return sorted([s[n] for n in s])

    def items(self):
        s = getattr(self, self.DATA_ATTR_NAME)
        return sorted([(n,s[n]) for n in s])
    
class IndexableMixin(object):
    def index(self, x):
        s = getattr(self, self.DATA_ATTR_NAME)
        return s.index(x)