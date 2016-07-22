class ComparableMixin(object):
    def __eq__(self, other):
        return getattr(self, self.DATA_ATTR_NAME) == getattr(other, other.DATA_ATTR_NAME)
        
    def __ne__(self, other):
        return not self.__eq__(other)


class SequenceMixin(object):
    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        """This method will rely on the get_elements() method of the
        concrete class.
        """
        
        loadData = getattr(self, self.DATA_ATTR_NAME)
        
        if not hasattr(self, 'get_elements'):
            raise ValueError("get_elements method not found")
        
        if type(loadData) == list:
            if self.counter < len(loadData):
                self.counter += 1
                return loadData[self.counter-1]
            else:
                raise StopIteration
        elif type(loadData) == dict:
            enum_dict = list(enumerate(loadData))
            self.get_value = ""
            if self.counter < len(enum_dict):
                self.counter += 1
                self.get_value = loadData[enum_dict[self.counter-1][1]]
                return enum_dict[self.counter-1][1]
            else:
                raise StopIteration

    next = __next__

    def __len__(self):
        self = iter(self)
        count = 0
        for item in self:
            count += 1
        return count
        
    def count(self):
        return len(self)
                    
    def __getitem__(self, key):
        return getattr(self, self.DATA_ATTR_NAME)[key]

    def __setitem__(self, key, value):
        getattr(self, self.DATA_ATTR_NAME)[key] = value
        return

    def __delitem__(self, key):
        del getattr(self, self.DATA_ATTR_NAME)[key]
        return

    def __contains__(self, item):
        if item in getattr(self, self.DATA_ATTR_NAME):
            return True
        else:
            return False


class RepresentableMixin(object):
    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(getattr(self, self.DATA_ATTR_NAME))

class ConstructibleMixin(object):
    DATA_ATTR_NAME = 'data'

    def __init__(self, initial=None):
        setattr(self, self.DATA_ATTR_NAME,
                initial or self.DATA_DEFAULT_INITIAL)
                

class OperableMixin(object):
    
    def __add__(self, other):
        # another_self = copy.deepcopy(self)
        # another_self += other
        #return another_self
        addList = getattr(self, self.DATA_ATTR_NAME) + getattr(other, other.DATA_ATTR_NAME)
        return ConstructibleMixin(addList)


    def __iadd__(self, other):
        iaddList = getattr(self, self.DATA_ATTR_NAME) + getattr(other, other.DATA_ATTR_NAME)
        setattr(self,self.DATA_ATTR_NAME,iaddList)
        return self
        

class AppendableMixin(object):
    def append(self, elem):
        # Relies on DATA_ATTR_NAME = 'data'
        appList = getattr(self, self.DATA_ATTR_NAME) + [elem]
        setattr(self,self.DATA_ATTR_NAME,appList)
        return self 


class HashableMixin(object):
    def keys(self):
        return list(getattr(self,self.DATA_ATTR_NAME))

    def values(self):
        return list(zip(*self.items()))[1]

    def items(self):
        dict = getattr(self,self.DATA_ATTR_NAME)
        return [(keyz,dict[keyz]) for keyz in dict]


class IndexableMixin(object):
    def index(self, x):
        if type(x) == int:
            for index in range(len(getattr(self, self.DATA_ATTR_NAME))):
                if getattr(self, self.DATA_ATTR_NAME)[index] == x:
                    return index
        else:
            raise ValueError