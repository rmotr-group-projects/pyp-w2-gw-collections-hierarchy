class ComparableMixin(object):
    def __eq__(self, other):
        return self.data == other.data
    def __ne__(self, other):
        # Relies in __eq__
        return self.data != other.data
        


class SequenceMixin(object):
    
    #current_index = 0 
    #elements = []
    
    def __iter__(self):
        if not hasattr(self, 'get_elements'):
            raise ValueError("get_elements method not found")
            
        self.elements = self.get_elements()
        self.current_index = 0 
        return self

    def __next__(self):
        """This method will rely on the get_elements() method of the
        concrete class.
        """
        if not hasattr(self, 'get_elements'):
            raise ValueError("get_elements method not found")
        # Keep writing your code here
        
        if not hasattr(self, 'current_index'):
            self.current_index = 0
        if not hasattr(self, 'elements'):
            self.elements = self.get_elements()
            
 
        #print self.elements
        while self.current_index < len (self.elements):
            elem =  self.elements[self.current_index]
            self.current_index += 1
            
            return elem	
        raise StopIteration()
       
       
       
    next = __next__

    def __len__(self):
        # Will rely on the iterator
        # can't do len(self.data)
        #if not hasattr(self, 'elements'):
            #self.elements = self.get_elements()
        #return len(self.elements)
        return len(self.data)


    def __getitem__(self, key):
        
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __contains__(self, item):
        # Will rely on the iterator
        return item in self.data


class RepresentableMixin(object):
    def __repr__(self):
        return str(self.data)

    def __str__(self):
        return str(self.data)
        


class ConstructibleMixin(object):
    DATA_ATTR_NAME = 'data'

    def __init__(self, initial=None):
        setattr(self, self.DATA_ATTR_NAME,
                initial or self.DATA_DEFAULT_INITIAL)


class OperableMixin(object):
    def __add__(self, other):
        #create a new instance of the same type as self
        newcollection = (type(self))()
        setattr(newcollection, 'data',
                self.data + other.data)
        return newcollection

    def __iadd__(self, other):
        self.data += other.data
        return self


class AppendableMixin(object):
    def append(self, elem):
        return self.data.append(elem)
        # Relies on DATA_ATTR_NAME = 'data'


class HashableMixin(object):
    def keys(self):
        return self.data.keys()

    def values(self):
        return self.data.values()

    def items(self):
        return self.data.items()


class IndexableMixin(object):
    def index(self, x):
        return self.data.index(x)
