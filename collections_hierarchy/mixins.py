class ComparableMixin(object):
    def __eq__(self, other):
        if type(other.get_elements) == list:
            return self.get_elements() == other.get_elements()
        else:
            return False
        
    def __ne__(self, other):
    #     # Relies in __eq__
        return not self.__eq__(other)


class SequenceMixin(object):
    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        # if self.counter == None:
        #     self.counter = 0
        """This method will rely on the get_elements() method of the
        concrete class.
        """
        if not hasattr(self, 'get_elements'):
            raise ValueError("get_elements method not found")
        # Keep writing your code here
        
        # raise NotImplementedError()
        #print(hasattr(self, 'get_elements'))
        if self.counter < len(self.get_elements()):
            self.counter += 1
            return self.get_elements()[self.counter-1]
        else:
            raise StopIteration

    next = __next__


    def __len__(self):
        # Will rely on the iterator
        # can't do len(self.data)
    
        count = 0
        for item in self.get_elements():
            count += 1
        return count
        

    def __getitem__(self, key):
        #print(type(self.get_elements()))
        if key not in [item[0] for item in self.get_elements()]:
            raise KeyError
        if self.get_elements() == []:
            raise IndexError
        return self.get_elements()[key]

    def __setitem__(self, key, value):
        self.get_elements()[key] = value
        return self.get_elements()[key]

    def __delitem__(self, key):
        # for item in self.get_elements():
        #     if item
        pass

    def __contains__(self, item):
        # Will rely on the iterator
        
        if item in self.get_elements():
            return True
        else:
            return False


class RepresentableMixin(object):
    def __repr__(self):
        # Will rely on the iterator or __str__
        return self.stringed_list

    def __str__(self):
        # Will rely on the iterator
        
        #if isinstance(self.get_elements()
        #self = iter(self)
        self.stringed_list = "["
        for i in self.get_elements():
            self.stringed_list = self.stringed_list + str(i) + ", "
        self.stringed_list = self.stringed_list.rstrip(', ') + "]"
        return self.stringed_list
        # return str(self.get_elements())

class ConstructibleMixin(object):
    DATA_ATTR_NAME = 'data'

    def __init__(self, initial=None):
        setattr(self, self.DATA_ATTR_NAME,
                initial or self.DATA_DEFAULT_INITIAL)
                

class OperableMixin(object):
    def __add__(self, other):
        # if other.get_elements() != []:
        #     for item in other.get_elements():
        #         self.append(item)
        return ConstructibleMixin(self.get_elements() + other.get_elements())
        #pass

    def __iadd__(self, other):
        self.data += other.data
        return ConstructibleMixin(self.data)
        
        # pass


class AppendableMixin(object):
    def append(self, elem):
        # Relies on DATA_ATTR_NAME = 'data'
        self.data += list(elem)
        return ConstructibleMixin(self.data)
        #pass[1,2,[2,3],{3:2}]


class HashableMixin(object):
    def keys(self):
        return [keyz for keyz in self.get_elements()]

    def values(self):
        return [self.get_elements()[keyz] for keyz in self.get_elements()]

    def items(self):
        return [(keyz,self.get_elements()[keyz]) for keyz in self.get_elements()]


class IndexableMixin(object):
    def index(self, x):
        if type(x) == int:
            for index in range(len(self.data)):
                if self.get_elements()[index] == x:
                    return index
        else:
            raise ValueError
    
    
####################################
# HERE IS A TEST ###################
####################################

# class Node(ComparableMixin):
#     def __init__(self, elem=None, next=None):
#         self.elem = elem
#         self.next = next
    
#     def __eq__(self, other):
#         if isinstance(other, self.__class__):
#             return str(self) == str(other)
#         else:
#             return False
#     def __ne__(self, other):
#         # Relies in __eq__
#         return not self.__eq__(other)

# # a = Node()
# # b = Node()

# # print(a==b)
# class SequenceMixinList(ConstructibleMixin, SequenceMixin):
#     DATA_DEFAULT_INITIAL = []

#     def get_elements(self):
#         return self.data
        
# class SequenceMixinDict(ConstructibleMixin, SequenceMixin):
#     DATA_DEFAULT_INITIAL = {}

#     def get_elements(self):
#         return list(self.data.items())
        
# d = SequenceMixinDict()
# # d['a']