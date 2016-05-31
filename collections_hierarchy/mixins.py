class ComparableMixin(object):
    def __eq__(self, other):
        return self.get_elements() == other

    def __ne__(self, other):
        return self.get_elements() != other

    def __lt__(self, other):
        return len(self.get_elements()) < len(other)

    def __gt__(self, other):
        return len(self.get_elements()) > len(other)

    def __le__(self, other):
        return len(self.get_elements()) <= len(other)

    def __ge__(self, other):
        return len(self.get_elements()) >= len(other)


class SequenceMixin(object):
    def __iter__(self):
        self.container_index = -1
        return iter(self.get_elements())

    def __next__(self):
        if isinstance(self.get_elements, list):
            if self.container_index > len(self.get_elements()):
                raise StopIteration

            self.container_index += 1
            return self.get_elements()[self.container_index]
        
        if isinstance(self.get_elements, dict):
            if self.container_index > len(list(self.get_elements().keys())):
                raise StopIteration
            
            self.container_index += 1
            return self.get_elements()[list(self.get_elements().keys())[self.container_index]]
            
            

    next = __next__

    def __len__(self):
        return len(self.get_elements())

    def __getitem__(self, key):
        return self.get_elements()[key]

    def __setitem__(self, key, value):
        self.get_elements()[key] = value

    def __delitem__(self, key):
        del self.get_elements()[key]

    def __contains__(self, item):
        return item in self.get_elements()
        
    def count(self):
        return len(self.get_elements())


class RepresentableMixin(object):
    def __repr__(self):
        return "%s" % type(self.get_elements())

    def __str__(self):
        #return("{}".format(self)) -> recursion error
        return "%s" % self.get_elements()
        

class ConstructibleMixin(object):
    DATA_ATTR_NAME = 'data'

    def __init__(self, initial=None):                                                        
        setattr(self, 
                self.DATA_ATTR_NAME, 
                initial or 
                self.DATA_DEFAULT_INITIAL)
        


class OperableMixin(object):
    def __add__(self, other):
        return self.get_elements() + other.get_elements()

    def __iadd__(self, other):
        orig = self.get_elements()
        new = other.get_elements()
        orig += new
        return orig
    
class AppendableMixin(object):
    def append(self, elem):
        return self.get_elements().append(elem)


class HashableMixin(object):
    def keys(self):
        return self.get_elements().keys()

    def values(self):
        return self.get_elements().values()

    def items(self):
        return self.get_elements().items()


class IndexableMixin(object):
    def index(self, x):
        return self.get_elements().index(x)

            
