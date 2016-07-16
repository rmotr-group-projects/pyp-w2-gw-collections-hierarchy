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
        
        
        
    def __next__(self):
        """This method will rely on the get_elements() method of the
        concrete class.
        """
        
        if not hasattr(self, 'get_elements'):
            raise ValueError("get_elements method not found")

        element_list = getattr(self, 'get_elements') #create a list of only elements
        
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
        if isinstance(self, list):
            counter = 0
            if self != None:
                if isinstance(self, list): 
                    for i in self:
                        counter += 1
                    return counter
        if isinstance(self, dict):
            for key in self:
                for element in key:
                    counter += 1
            return counter
        else:
            return TypeError

    def __getitem__(self, key):
       #return getattr(self, DATA_ATTR_NAME[key])
        return (key, self.DATA_ATTR_NAME[key])

    def __setitem__(self, key, value):
        self.DATA_ATTR_NAME[key] = value

    def __delitem__(self, key):
        del self.DATA_ATTR_NAME[key]

    def __contains__(self, item):
        # Will rely on the iterator
      
        if item in self: #if getattr(self, DATA_ATTR_NAME[a]) == item:
            return True
        return False
        
    

class RepresentableMixin(object):
    def __repr__(self):
        return self.__str__
        # Will rely on the iterator or __str__

    def __str__(self):
        # Will rely on the iterator
        if isinstance(self, list):
            result = []
            for item in self:
                result.append(item)
            return str(result)
        if isinstance(self, dict):
            result = {}
            for key, value in self:
                result[key] = value
            return str(result)


class ConstructibleMixin(object):
    DATA_ATTR_NAME = 'data'
    
    def __init__(self, initial=None):
        setattr(self, self.DATA_ATTR_NAME,
                initial or self.DATA_DEFAULT_INITIAL)
                #setattr(self, 'data', 123) is equivalent to x.foobar = 123
                #getattr(self, DATA_ATTR_NAME)

class OperableMixin(object):
    def __add__(self, other):
        result = []
        # result.append(self)
        # result.append(other)
        for item in self:
            result.append(item)
        for item in other:
            result.append(other)
        return result 

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
        return [k for k, v in getattr(self, self.DATA_ATTR_NAME)]
        #for key in dict.iterkeys()
        
    def values(self):
        return [v for k, v in getattr(self, self.DATA_ATTR_NAME)]
        #for value in dict.itervalues()
        
    def items(self):
        return [(k, v) for k, v in getattr(self, self.DATA_ATTR_NAME)]
        #for k, v in dict.iteritems()

class IndexableMixin(object):
    def index(self, x):
        return getattr(self, self.DATA_ATTR_NAME[x])
        