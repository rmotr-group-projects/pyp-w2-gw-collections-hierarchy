class ComparableMixin(object):
    #Implements comparison functionality. Common for List and Dict
    def __eq__(self, other):
        s = self.DATA_ATTR_NAME #Get the name of the property that stores the data
        data1 = getattr(self, s) #Get the value of the property that stores the data
        data2 = getattr(other, s)
        
        if type(data1) == type(data2):
            return data1 == data2
        
    def __ne__(self, other):
        if not self.__eq__(other):
            return True

class SequenceMixin(object):
    def __iter__(self):
        data1 = getattr(self, self.DATA_ATTR_NAME)
        for d in data1:
            while d:
                if type(data1) is list:
                    yield d
                elif type(data1) is dict:
                    yield data1[d]

    def __next__(self):
        """This method will rely on the get_elements() method of the
        concrete class.
        """
        if not hasattr(self, 'get_elements'):
            raise ValueError("get_elements method not found")
        self.get_elements()
        raise NotImplementedError()

    next = __next__

    def __len__(self):
        # uses the iterator to provide a count of the items
        c = 0
        for d in self:
            c += 1
            return c

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
        return self.__str__()

    def __str__(self):
        # Will rely on the iterator
        # uses the iterator to return a list for formatting
        l = ",".join(map(str, self))
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
        pass

    def __iadd__(self, other):
        pass


class AppendableMixin(object):
    def append(self, elem):
        # Relies on DATA_ATTR_NAME = 'data'
        s = getattr(self, self.DATA_ATTR_NAME)
        
        if type(s) is list:
            s.append(elem)

class HashableMixin(object):
    def keys(self):
        s = getattr(self, self.DATA_ATTR_NAME)
        return [n for n in s]

    def values(self):
        s = getattr(self, self.DATA_ATTR_NAME)
        return [s[n] for n in s]

    def items(self):
        s = getattr(self, self.DATA_ATTR_NAME)
        return [(n,s[n]) for n in s]
    
class IndexableMixin(object):
    def index(self, x):
        s = getattr(self, self.DATA_ATTR_NAME)
        return s[x]