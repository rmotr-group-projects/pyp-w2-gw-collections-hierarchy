class ComparableMixin(object):
    def __eq__(self, other):
        return self.data == other
        
    def __ne__(self, other):
        if self.data == other:
            return False
        else:
            return True


class SequenceMixin(object):
    def __iter__(self):
        self.curr_elements = self.get_elements()
        self.curr_idx = 0
        return self

    def __next__(self):
        if not hasattr(self, 'get_elements'):
            raise AttributeError("SequenceMixin object has no attribute \
            'get_elements")
        

        if not hasattr(self, 'curr_elements'):
            self.__iter__()
         
        if self.curr_idx < len(self.curr_elements) :
            curr_item = self.curr_elements[self.curr_idx]
            self.curr_idx += 1
            return curr_item
            
        else: 
            raise StopIteration

    next = __next__

    def __len__(self):
        count = 0
        for items in self.data:
            count += 1
        
        return count

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value
        
    
    def __delitem__(self, key):
        self.data.pop(key)


    def __contains__(self, item):
        for data_item in self.data : 
            if item == data_item :
                return True
        else :
            return False


class RepresentableMixin(object):
    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.data)


class ConstructibleMixin(object):
    DATA_ATTR_NAME = 'data'

    def __init__(self, initial=None):
        setattr(self, self.DATA_ATTR_NAME,
                initial or self.DATA_DEFAULT_INITIAL)


class OperableMixin(object):
    def __add__(self, other):
        new_items_list = self.data + other.data
        return self.__class__(new_items_list)


    def __iadd__(self, other):
        return self.data + other.data


class AppendableMixin(object):
    def append(self, elem):
        self.data.append(elem)


class HashableMixin(object):
    def keys(self):
        return [keys for keys in self.data.keys()]

    def values(self):
        return [values for values in self.data.values()]

    def items(self):
        return [(key, value) for key, value in self.data.items()]


class IndexableMixin(object):
    def index(self, x):
        for pos, item in enumerate(self.data) :
            if item == x : 
                return pos
        else :
            raise ValueError
