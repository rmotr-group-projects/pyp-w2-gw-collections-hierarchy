from copy import deepcopy

class ComparableMixin(object):
    def __eq__(self, other):
        selfdata = getattr(self, self.DATA_ATTR_NAME)
        otherdata = getattr(other, other.DATA_ATTR_NAME)
        return selfdata == otherdata
    
    def __ne__(self, other):
        selfdata = getattr(self, self.DATA_ATTR_NAME)
        otherdata = getattr(other, other.DATA_ATTR_NAME)
        return selfdata != otherdata

    def __lt__(self, other):
        selfdata = getattr(self, self.DATA_ATTR_NAME)
        otherdata = getattr(other, other.DATA_ATTR_NAME)
        return selfdata <  otherdata
        
    def __gt__(self, other):
        selfdata = getattr(self, self.DATA_ATTR_NAME)
        otherdata = getattr(other, other.DATA_ATTR_NAME)
        return selfdata >  otherdata

    def __le__(self, other):
        selfdata = getattr(self, self.DATA_ATTR_NAME)
        otherdata = getattr(other, other.DATA_ATTR_NAME)
        return selfdata <=  otherdata

    def __ge__(self, other):
        selfdata = getattr(self, self.DATA_ATTR_NAME)
        otherdata = getattr(other, other.DATA_ATTR_NAME)
        return selfdata >=  otherdata


class SequenceMixin(object):
    # Used by List and by Dict
    def __iter__(self):
        # iterate over the right portion of the list or dict.
        elements = self.get_elements()
        return iter(elements)

    def __next__(self):
        return iter(self).next
        
    next = __next__

    def __len__(self):
        return sum(1 for i in self)
        
    def count(self):
        return len(self)

    def __getitem__(self, key):
        selfdata = getattr(self, self.DATA_ATTR_NAME)
        # in a dict, this will return dict{key}
        # in a list, this will reurn list[list position]
        return selfdata[key]

    def __setitem__(self, key, value):
        selfdata = getattr(self, self.DATA_ATTR_NAME)
        # in a dict, this will set dict{key}
        # in a list, this will set list[list position]
        #   this will fail on a list without that position existing.
        # TODO: bounds checking, raise error?  [see if it fails test.]
        selfdata[key] = value

    def __delitem__(self, key):
        selfdata = getattr(self, self.DATA_ATTR_NAME)
        # in a dict, this will set dict{key}
        # in a list, this will set list[list position]
        #   this will fail on a list without that position existing.
        # TODO: bounds checking, raise error?  [see if it fails test.]
        del selfdata[key]

    def __contains__(self, item):
        # return item in self would just call __contains__ again, so loop.
        for i in self:
            if i == item:
                return True
        return False


class RepresentableMixin(object):
    # Used by List and by Dict
    def __repr__(self):
        return str(self)

    def __str__(self):
        # for a list [1,2,3] str should return "[1,2,3]"
        # for a dict {'a': 1, 'b': 2} str should return "{'a': 1, 'b': 2}"
        return str(self.get_elements())
       

class ConstructibleMixin(object):
    # Used by List and by Dict
    DATA_ATTR_NAME = 'data'

    def __init__(self, initial=None):
        setattr(self, self.DATA_ATTR_NAME, initial or DATA_DEFAULT_INITIAL)


class OperableMixin(object):
    # Used by List only
    # self + other
    def __add__(self, other):
        new_list = deepcopy(self)
        for elem in other:
            new_list.append(elem)
        return new_list

    # self += other
    def __iadd__(self, other):
        for elem in other:
            self.append(elem)
        return self

class AppendableMixin(object):
    # Used by List only.
    def append(self, elem):
        return self.get_elements().append(elem)


class HashableMixin(object):
    # Used by Dict only.
    def keys(self):
        return [i for i in self]

    def values(self):
        return [self[i] for i in self.keys()]

    def items(self):
        return [(key, self[key]) for key in self.keys()]


class IndexableMixin(object):
    # Used by List only.
    def index(self, x):
        #print('Indexable List item is').format(self)
        for position, value in enumerate(self):
            #print('Position is {} value is {} x is {}').format(position, value, x)
            if value == x:
                return position
        
        raise ValueError('item not found: {}'.format(x))
