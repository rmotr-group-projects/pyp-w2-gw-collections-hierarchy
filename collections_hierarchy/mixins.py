class ComparableMixin(object):
    def __eq__(self, other):
        return getattr(self, self.DATA_ATTR_NAME) == getattr(other, other.DATA_ATTR_NAME)
        
    def __ne__(self, other):
    #     # Relies in __eq__
        return not self.__eq__(other)


class SequenceMixin(object):
    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        """This method will rely on the get_elements() method of the
        concrete class.
        """
        if not hasattr(self, 'get_elements'):
            raise ValueError("get_elements method not found")
        # Keep writing your code here
        
        # raise NotImplementedError()
        if type(getattr(self, self.DATA_ATTR_NAME)) == list:
            self.identifier = "list"
            if self.counter < len(getattr(self, self.DATA_ATTR_NAME)):
                self.counter += 1
                return getattr(self, self.DATA_ATTR_NAME)[self.counter-1]
            else:
                raise StopIteration
        elif type(getattr(self, self.DATA_ATTR_NAME)) == dict:
            self.identifier = "dict"
            enum_dict = list(enumerate(getattr(self, self.DATA_ATTR_NAME)))
            self.get_value = ""
            if self.counter < len(enum_dict):
                self.counter += 1
                self.get_value = getattr(self, self.DATA_ATTR_NAME)[enum_dict[self.counter-1][1]]
                return enum_dict[self.counter-1][1]
            else:
                raise StopIteration

    next = __next__

    def __len__(self):
        # Will rely on the iterator
        # can't do len(self.data)
        # self = iter(self)
        # count = 0
        # for item in self:
        #     count += 1
        # return count
        return len(getattr(self, self.DATA_ATTR_NAME))
        
    def count(self):
        return len(self)

    
    # def __getitem__(self, key):
        
    #     length_of_self = len(self)
    #     if self.identifier == "dict":
    #         if key not in [item for item in self] and self.identifier == "dict":
    #             raise KeyError(str(key))
    #         for i in self:
    #             if key == i:
    #                 return self.get_value
    
    #     if self.identifier == "list":
    #         if type(key) != int and ":" not in str(key):  # here, it's receiving an 'a' yep
    #             raise TypeError('list indices must be integers or slices, not str')
    #         elif self.identifier == "list" and key > length_of_self-1:
    #             raise IndexError('list index out of range')
    #         for tuple_item in list(enumerate(self)):
    #             if tuple_item[0] == key:
    #                 return tuple_item[1]
                    
    def __getitem__(self, key):
        return getattr(self, self.DATA_ATTR_NAME)[key]

    def __setitem__(self, key, value):
        getattr(self, self.DATA_ATTR_NAME)[key] = value
        return
        # length_of_self = len(self)
        # if type(key) != int and ":" not in str(key) and self.identifier == "list":
        #     raise TypeError('list indices must be integers or slices, not str')
        # elif self.identifier == "list" and key > length_of_self:
        #     raise IndexError('list index out of range')
        # self.get_elements()[key] = value
        # return self.get_elements()[key]

    def __delitem__(self, key):
        del getattr(self, self.DATA_ATTR_NAME)[key]
        return

    def __contains__(self, item):
        # Will rely on the iterator
        
        if item in getattr(self, self.DATA_ATTR_NAME):
            return True
        else:
            return False


class RepresentableMixin(object):
    def __repr__(self):
        # Will rely on the iterator or __str__
        return str(self)

    def __str__(self):
        # Will rely on the iterator
        
        #if isinstance(self.get_elements()
        #self = iter(self)
        # self.stringed_list = "["
        # for i in self.get_elements():
        #     self.stringed_list = self.stringed_list + str(i) + ", "
        # self.stringed_list = self.stringed_list.rstrip(', ') + "]"
        # return self.stringed_list
        # return str(self.get_elements())
        # if type(getattr(self, self.DATA_ATTR_NAME)) == list:
            # for i in getattr(self, self.DATA_ATTR_NAME):
            
        return str(getattr(self, self.DATA_ATTR_NAME))

class ConstructibleMixin(object):
    DATA_ATTR_NAME = 'data'

    def __init__(self, initial=None):
        setattr(self, self.DATA_ATTR_NAME,
                initial or self.DATA_DEFAULT_INITIAL)
                

class OperableMixin(object):
    #OperableMixin is uniquely List Mixin
    
    def __add__(self, other):
        addList = getattr(self, self.DATA_ATTR_NAME) + getattr(other, other.DATA_ATTR_NAME)
        return ConstructibleMixin(addList) #<- who did this? i was thinking this too, i tried it once but dont remember if it worked
        #return self.DATA_ATTR_NAME + other.DATA_ATTR_NAME


    def __iadd__(self, other):
        for i in getattr(other, other.DATA_ATTR_NAME):
            getattr(self, self.DATA_ATTR_NAME).append(i)
        #new_list = getattr(self, self.DATA_ATTR_NAME) + getattr(other, other.DATA_ATTR_NAME)
        return self
        

class AppendableMixin(object):
    def append(self, elem):
        # Relies on DATA_ATTR_NAME = 'data'
        fixer = getattr(self, self.DATA_ATTR_NAME)
        fixer += [elem]
        return 


class HashableMixin(object):
    def keys(self):
        return [keyz for keyz in getattr(self, self.DATA_ATTR_NAME)]

    def values(self):
        return [getattr(self, self.DATA_ATTR_NAME)[keyz] for keyz in getattr(self, self.DATA_ATTR_NAME)]

    def items(self):
        return [(keyz,getattr(self, self.DATA_ATTR_NAME)[keyz]) for keyz in getattr(self, self.DATA_ATTR_NAME)]


class IndexableMixin(object):
    def index(self, x):
        if type(x) == int:
            for index in range(len(getattr(self, self.DATA_ATTR_NAME))):
                if getattr(self, self.DATA_ATTR_NAME)[index] == x:
                    return index
        else:
            raise ValueError