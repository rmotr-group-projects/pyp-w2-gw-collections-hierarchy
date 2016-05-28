from copy import deepcopy

class ComparableMixin(object):
    def __eq__(self, other):
        data = getattr(self, self.DATA_ATTR_NAME)
        other_data = getattr(other, other.DATA_ATTR_NAME)
        
        if isinstance(self, HashableMixin) and isinstance(other, HashableMixin):
            return sorted(data.items()) == sorted(other_data.items())
        
        
        return data == other_data
        
            
    def __ne__(self, other):
        # Relies in __eq__
        return not self == other


class SequenceMixin(object):
    def __iter__(self):
        self.iterator = iter(self.get_elements())
        return self
       

    def __next__(self):
        """This method will rely on the get_elements() method of the
        concrete class.
        """
        if not hasattr(self, 'get_elements'):
            raise ValueError("get_elements method not found")
            
        try:
            self.iterator
        except:
            self.iterator = iter(self.get_elements())
        return next(self.iterator)


    next = __next__
    
    def count(self):
        return len(self)
        
    def __len__(self):
        # Will rely on the iterator
        # can't do len(self.data)
        count = 0
        for _ in self:
            count += 1
        return count

    def __getitem__(self, key):
        data = getattr(self, self.DATA_ATTR_NAME)
        return data[key]

    def __setitem__(self, key, value):
        data = getattr(self, self.DATA_ATTR_NAME)
        data[key] = value

    def __delitem__(self, key):
        data = getattr(self, self.DATA_ATTR_NAME)
        del data[key]

    def __contains__(self, item):
        # Will rely on the iterator
        for value in self:
            if value == item:
                return True
        return False


class RepresentableMixin(object):
    def __repr__(self):
        return "type: {0} \nelements: {1}".format(self.__class__.__name__, str(self))

    def __str__(self):
        # Will rely on the iterator
        data = getattr(self, self.DATA_ATTR_NAME)
        return str(data)


class ConstructibleMixin(object):
    DATA_ATTR_NAME = 'data'

    def __init__(self, initial=None):
        setattr(self, self.DATA_ATTR_NAME,
                initial or self.DATA_DEFAULT_INITIAL)


class OperableMixin(object):
    def __add__(self, other):
        new_object = deepcopy(self)
        data = getattr(new_object, self.DATA_ATTR_NAME)
        other_data = getattr(other, other.DATA_ATTR_NAME)
        
        
        if isinstance(self, HashableMixin) and isinstance(other, HashableMixin):
            data.update(other)
        else:
            data += other_data
        
        return new_object 
        
    def __iadd__(self, other):
        data = getattr(self, self.DATA_ATTR_NAME)
        other_data = getattr(other, other.DATA_ATTR_NAME)
        
        if isinstance(self, HashableMixin) and isinstance(other, HashableMixin):
            return data.update(other)
        else: 
            data += other_data
        return self
        


class AppendableMixin(object):
    def append(self, elem):
        # Relies on DATA_ATTR_NAME = 'data'
        data = getattr(self, self.DATA_ATTR_NAME)
        
        if isinstance(self, HashableMixin):
            data.update(elem)
        else: 
            data.append(elem)


class HashableMixin(object):
    def keys(self):
        data = getattr(self, self.DATA_ATTR_NAME)
        return data.keys()

    def values(self):
        data = getattr(self, self.DATA_ATTR_NAME)
        return data.values()

    def items(self):
        data = getattr(self, self.DATA_ATTR_NAME)
        return data.items()


class IndexableMixin(object):
    def index(self, x):
        for count in range(len(self)):
            if x == self[count]:
                return count
        raise ValueError()
