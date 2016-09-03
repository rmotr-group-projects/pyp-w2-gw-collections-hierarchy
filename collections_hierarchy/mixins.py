class ComparableMixin(object):
    def __eq__(self, other):
        if self.data==other:
            return True
        else:
            return False

    def __ne__(self, other):
        if not self.__eq__(other):
            return True


class SequenceMixin(object):
    def __iter__(self):
        for Data in self.data:
            yield Data

    def __next__(self):
        """This method will rely on the get_elements() method of the
        concrete class.
        """
        if not hasattr(self, 'get_elements'):
            raise ValueError("get_elements method not found")
        # Keep writing your code here
        return self.__getitem__(self)

    next = __next__

    def __len__(self):
        # Will rely on the iterator
        # can't do len(self.data)
        self.counter=0
        for items in self.data:
            self.counter+=1
        return self.counter
        
    def __getitem__(self, key):
        try:
            return self.data[key]
        except IndexError:
            print('Index out of range.')

    def __setitem__(self, key, value):
        try:
            self.data[key] = value
        except IndexError:
            print('Index out of range.')

    def __delitem__(self, key):
        try:
            self.data = [elem for elem in self.data if not self.data[key]]
        except IndexError:
            print('Index out of range.')

    def __contains__(self, item):
        # Will rely on the iterator
        if item not in self.data:
            return False
        else: 
            return True


class RepresentableMixin(object):
    def __repr__(self):
        # Will rely on the iterator or __str__
        pass

    def __str__(self):
        return str(self.data) 
        


class ConstructibleMixin(object):
    DATA_ATTR_NAME = 'data'

    def __init__(self, initial=None):
        setattr(self, self.DATA_ATTR_NAME,
                initial or self.DATA_DEFAULT_INITIAL)


class OperableMixin(object):
    def __add__(self, other):
        obj=object.__new__(type(self))
        obj.data=self.data+other.data
        return obj
        
    def __iadd__(self, other):
        data=self.data+other.data
        self.data=data
        return self


class AppendableMixin(object):
    def append(self, elem):
        # Relies on DATA_ATTR_NAME = 'data'
        self.data.append(elem)
        return self.data


class HashableMixin(object):
    def keys(self):
        return self.data.keys()

    def values(self):
        return self.values()

    def items(self):
        return self.items()


class IndexableMixin(object):
    def index(self, x):
        call = getattr(SequenceMixin, '__len__')    #allows the use of len
        for i in range(0, call(self)):              #We can use the list positions now
            if self.data[i] == x:
                return i
        print(x)
        if x not in self:
            raise ValueError
