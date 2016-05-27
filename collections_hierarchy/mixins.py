import copy 

class ComparableMixin(object):
    '''
    Use the builtin python comparisons
    '''
    def __eq__(self, other):
        return getattr(self, self.DATA_ATTR_NAME) == getattr(other, other.DATA_ATTR_NAME)

    def __ne__(self, other):
        return getattr(self, self.DATA_ATTR_NAME) != getattr(other, other.DATA_ATTR_NAME)
        
    def __lt__(self, other):
        return getattr(self, self.DATA_ATTR_NAME) < getattr(other, other.DATA_ATTR_NAME)

    def __gt__(self, other):
        return getattr(self, self.DATA_ATTR_NAME) > getattr(other, other.DATA_ATTR_NAME)

    def __le__(self, other):
        return getattr(self, self.DATA_ATTR_NAME) <= getattr(other, other.DATA_ATTR_NAME)

    def __ge__(self, other):
        return getattr(self, self.DATA_ATTR_NAME) >= getattr(other, other.DATA_ATTR_NAME)

class SequenceMixin(object):
    def __iter__(self):
        # This is called at the start of an iteration

        return iter(self.get_elements())

        # alternate way to do it:
        # self.iter_counter = 0
        # return self

    def __next__(self): 
        # steps through all elements, raises StopIteration at the end
        return next(iter(self.get_elements()))

        # alternate way to do it:
        # loop through all elements given by get_elements
        # raise stop iteration at end
        # if self.iter_counter == len(self):
        #     raise StopIteration()
        # self.iter_counter += 1
        # return self.get_elements()[self.iter_counter - 1]

    next = __next__ # for python 3 and python 2

    def __len__(self):
        return len(getattr(self, self.DATA_ATTR_NAME))

    def __getitem__(self, key): # accesses item using [] format
        return getattr(self, self.DATA_ATTR_NAME)[key]

    def __setitem__(self, key, value):
        getattr(self, self.DATA_ATTR_NAME)[key] = value

    def __delitem__(self, key):
        del getattr(self, self.DATA_ATTR_NAME)[key]
        
    def __contains__(self, item):
        return item in getattr(self, self.DATA_ATTR_NAME)
        
    def count(self):
        '''
        Normally list.count(x) counts occurences of x in list, but we
        are just using count as alias of len
        '''
        return len(self)

class RepresentableMixin(object):
    def __repr__(self):
        return str(getattr(self, self.DATA_ATTR_NAME))

    def __str__(self):
        return repr(getattr(self, self.DATA_ATTR_NAME))

class ConstructibleMixin(object):
    DATA_ATTR_NAME = 'data'

    def __init__(self, initial=None):
        # self.data will either be a list [] or dict {}
        setattr(self, self.DATA_ATTR_NAME, initial or self.DATA_DEFAULT_INITIAL)

class OperableMixin(object):
    '''
    Used by Lists to combine 2 Lists into 1
    Initially we attempted L1 + L2 but this converts a List into a list
    '''
    def __add__(self, other):
        '''
        Append all the elements from other (using iteration) onto a copy of self
        '''
        new_list = copy.deepcopy(self) # use copy to avoid referencing conflicts
        for elem in other:
            new_list.append(elem)
        return new_list
        
    def __iadd__(self, other):
        '''
        Makes use of the __add__ above to modify self
        '''
        self = self + other
        return self

class AppendableMixin(object):
    '''
    Used by Lists to append a new elem to the end of the list
    '''
    def append(self, elem):
        getattr(self, self.DATA_ATTR_NAME).append(elem)

class HashableMixin(object):
    '''
    Used by Dicts to access keys, values, and items in list form
    To pass tox tests it seems like the key lists need to be sorted
    Here we know get_elements() will be sorted so we can use that
    '''
    def keys(self):
        # returns keys as a list
        return self.get_elements()

    def values(self):
        # returns values as a list
        return [self[key] for key in self.get_elements()]

    def items(self):
        # returns a list of (key, value) tuples
        return [(key, self[key]) for key in self.get_elements()]

class IndexableMixin(object):
    '''
    Returns the index of the first occurence of x in the List
    '''
    def index(self, x):
        return getattr(self, self.DATA_ATTR_NAME).index(x)
