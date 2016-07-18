class ComparableMixin(object):
    def __eq__(self, other):
        self_data = getattr(self, self.DATA_ATTR_NAME)
        other_data = getattr(other, other.DATA_ATTR_NAME)
        if self_data == other_data:
            return True
        return False
        
    def __ne__(self, other):
        return not self == other


class SequenceMixin(object):
    def __iter__(self):
        self.i =  0
        return self
        
    def __next__(self):
        """This method will rely on the get_elements() method of the
        concrete class.
        """
        
        if not hasattr(self, 'get_elements'):
            raise ValueError("get_elements method not found")

        element_list = getattr(self, 'get_elements')() #self.get_elements
        
        while self.i < len(element_list):
            element = element_list[self.i]
            self.i += 1
            return element 
        raise StopIteration
        
        raise NotImplementedError() #we have to put this somewhere

    next = __next__ #accounts for the difference between python 2 and 3

    def __len__(self):
        # Will rely on the iterator 
        # can't do len(self.data) 
        count = 0
        
        for item in getattr(self, self.DATA_ATTR_NAME):
            count += 1
        return count
    count = __len__

    def __getitem__(self, key):
        return getattr(self, self.DATA_ATTR_NAME)[key] # "data"[key] :-O

    def __setitem__(self, key, value):
        getattr(self, self.DATA_ATTR_NAME)[key] = value
        
    def __delitem__(self, key):
        del getattr(self, self.DATA_ATTR_NAME)[key]

    def __contains__(self, item):
        # Will rely on the iterator
      
        if item in getattr(self, self.DATA_ATTR_NAME): #if getattr(self, DATA_ATTR_NAME[a]) == item:
            return True
        return False
        
    

class RepresentableMixin(object):
    def __repr__(self):
        return str(self)
        # Will rely on the iterator or __str__

    def __str__(self):
        # Will rely on the iterator
        result = []
        for item in getattr(self, self.DATA_ATTR_NAME):
            result.append(item)
            
        return str(result)
        
class ConstructibleMixin(object):
    DATA_ATTR_NAME = 'data'
    
    def __init__(self, initial=None):
        setattr(self, self.DATA_ATTR_NAME,
                initial or self.DATA_DEFAULT_INITIAL)


class OperableMixin(object):
    def __add__(self, other): # List(1,2) + List(3,4) => [1,2,3,4]       List(1,2,3,4)
        result = []

        for item in getattr(self, self.DATA_ATTR_NAME):
            result.append(item)
        
        for item in getattr(other, other.DATA_ATTR_NAME):
            result.append(item)
        
        
        return self.__class__(result) 

    def __iadd__(self, other):
        for item in other:
            self.append(item)
        return self
    
class AppendableMixin(object): # List().append()
    def append(self, elem):
        # Relies on DATA_ATTR_NAME = 'data', can assume that the underlying data structure
        #is a list, since lists can append, can also be tuple, or set maybe?
        existing_data = getattr(self, self.DATA_ATTR_NAME)
        existing_data.append(elem)



class HashableMixin(object):
    def keys(self):
        key = sorted( getattr(self, 'get_elements')())
        return key
        
    def values(self):
        return sorted(list(getattr(self, self.DATA_ATTR_NAME).values()))
        
    def items(self):
        return sorted(list(getattr(self, self.DATA_ATTR_NAME).items()))

class IndexableMixin(object):
    def index(self, x):
        for ind, value in enumerate(getattr(self, self.DATA_ATTR_NAME)):    # (index, value)
            if x == value:
                return ind
        raise ValueError