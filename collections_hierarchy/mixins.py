class ComparableMixin(object):
    def __eq__(self, other):
        selfObj = getattr(self, self.DATA_ATTR_NAME)
        otherObj = getattr(other, other.DATA_ATTR_NAME)
        
        if (len(selfObj) != len(otherObj)):
            return False

        objTypesAreDicts = isinstance(selfObj, dict) and isinstance(otherObj, dict)
        objTypesAreLists = isinstance(selfObj, list) and isinstance(otherObj, list)
        
        if (objTypesAreDicts):
            return selfObj == otherObj
        elif (objTypesAreLists):
            return sorted(selfObj) == sorted(otherObj)
        else:
            return False
        
    def __ne__(self, other):
        # Relies in __eq__
        return not self == other


class SequenceMixin(object):
    def __iter__(self): #hangout?
        # #how to iterate over a mixin in class
        # element = self.index() # get first element
        # while element:
        #     yield element
        #     element = self.next
        # raise StopIteration
        # 
        # 
        self.iterator = iter(self.get_elements())
        return self.iterator
        

    def __next__(self):
        """This method will rely on the get_elements() method of the
        concrete class.
        """
        if not hasattr(self, 'get_elements'):
            raise ValueError("get_elements method not found")
        # Keep writing your code here
        
        try:
            getattr(self, "iterator")   
        except AttributeError:
            self.iterator = iter(self)
        
        return next(self.iterator)
        
    # Fixes an issue with conversion between Python 2 and 3
    next = __next__

    def __len__(self):
        # Will rely on the iterator
        # can't do len(self.data)
        count = 0
        for item in self:
            count += 1
        return count
        
    count = __len__

    def __getitem__(self, key):
        return getattr(self, self.DATA_ATTR_NAME)[key]

    def __setitem__(self, key, value):
        getattr(self, self.DATA_ATTR_NAME)[key] = value
        
    def __delitem__(self, key):
        del getattr(self, self.DATA_ATTR_NAME)[key]

    def __contains__(self, item):
        # Will rely on the iterator
        for elem in getattr(self, self.DATA_ATTR_NAME):
            if elem == item:
                return True
        return False


class RepresentableMixin(object):
    def __repr__(self):
        # Will rely on the iterator or __str__
        return str(self)

    def __str__(self):
        # Will rely on the iterator
        
        s = ", ".join(str(elem) for elem in self)
        return "[{}]".format(s)
        

class ConstructibleMixin(object):
    DATA_ATTR_NAME = 'data'

    def __init__(self, initial=None):
        setattr(self, self.DATA_ATTR_NAME,
                initial or self.DATA_DEFAULT_INITIAL)

    # starts our object setattr(object, name, value)
class OperableMixin(object):
    def __add__(self, other):
        newObject = getattr(self, self.DATA_ATTR_NAME) + getattr(other, other.DATA_ATTR_NAME)
        return type(self)(newObject)
        
    def __iadd__(self, other):
        return self + other


class AppendableMixin(object):
    def append(self, elem):
        # Relies on DATA_ATTR_NAME = 'data'
        object = getattr(self, self.DATA_ATTR_NAME)
        objectIsList = isinstance(object, list)
        if objectIsList:
            object.append(elem)
        
        
class HashableMixin(object):
    def keys(self):
        keys = getattr(self, self.DATA_ATTR_NAME).keys()
        return sorted(list(keys))

    def values(self):
        values = getattr(self, self.DATA_ATTR_NAME).values()
        return sorted(list(values))

    def items(self):
        items = getattr(self, self.DATA_ATTR_NAME).items()
        return sorted(list(items))        


class IndexableMixin(object):
    def index(self, x):
        return getattr(self, self.DATA_ATTR_NAME).index(x)
