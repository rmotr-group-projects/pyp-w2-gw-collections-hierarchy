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
        raise NotImplementedError()

    next = __next__

    def __len__(self):
        # Will rely on the iterator
        # can't do len(self.data)
        return self.count()
        
    def count(self):
        self.counter=0
        while self.data:
            self.counter+=1
        return self.counter

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass

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
        a_list=[]
        for i in self:
            a_list.append(i)
        for i in other:
            a_list.append(i)
        return a_list

    def __iadd__(self, other):
        for i in other:
            self.data.append(i)
        return self


class AppendableMixin(object):
    def append(self, elem):
        # Relies on DATA_ATTR_NAME = 'data'
        self.data.append(elem)


class HashableMixin(object):
    def keys(self):
        pass

    def values(self):
        pass

    def items(self):
        pass


class IndexableMixin(object):
    def index(self, x):
        call = getattr(SequenceMixin, '__len__')    #allows the use of len
        for i in range(0, call(self)):              #We can use the list positions now
            if self.data[i] == x:
                return i
        print(x)
        if x not in self:
            raise ValueError
