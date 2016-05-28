from copy import deepcopy

class ComparableMixin(object):
    def __eq__(self, other):
        selfdata = getattr(self, self.DATA_ATTR_NAME)
        otherdata = getattr(other, other.DATA_ATTR_NAME)
        return selfdata == otherdata
        
    def __ne__(self, other):
        # Relies in __eq__
        selfdata = getattr(self, self.DATA_ATTR_NAME)
        otherdata = getattr(other, other.DATA_ATTR_NAME)
        return selfdata != otherdata


class SequenceMixin(object):
    def __iter__(self, count=0):
        self.count = count
        return iter(self.get_elements())

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

    def __len__(self):
        # Will rely on the iterator
        # can't do len(self.data)
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
        # Will rely on the iterator
        # return item in self would just call __contains__ again, so loop.
        for i in self:
            if i == item:
                return True
        return False


class RepresentableMixin(object):
    def __repr__(self):
        # Will rely on the iterator or __str__
        return str(self)

    def __str__(self):
        # Will rely on the iterator
        # for a list [1,2,3] str should return "[1,2,3]"
        # for a dict {'a': 1, 'b': 2} str should return "{'a': 1, 'b': 2}"
        return str(self.get_elements())


class ConstructibleMixin(object):
    DATA_ATTR_NAME = 'data'

    def __init__(self, initial=None):
        setattr(self, self.DATA_ATTR_NAME,
                initial or self.DATA_DEFAULT_INITIAL)


class OperableMixin(object):
    # OperableMixinList(ConstructibleMixin, OperableMixin)
    def __add__(self, other):
        new_list = deepcopy(self)
        selfdata = getattr(new_list, self.DATA_ATTR_NAME)
        otherdata = getattr(other, other.DATA_ATTR_NAME)
        
        #for elem in otherdata:  # can't iterate on other directly
        selfdata += otherdata
        return new_list

    def __iadd__(self, other):
        return self + other


class AppendableMixin(object):
    def append(self, elem):
        data = getattr(self, self.DATA_ATTR_NAME)
        # Relies on DATA_ATTR_NAME = 'data'
        return data.append(elem)


class HashableMixin(object):
    def keys(self):
        return [i for i in self]

    def values(self):
        return [self[i] for i in self.keys()]

    def items(self):
        return [(key, self[key]) for key in self.keys()]


class IndexableMixin(object):
    def index(self, x):
        for position, value in enumerate(self):
            #print('Position is {} value is {} x is {}').format(position, value, x)
            if value == x:
                return position

        raise ValueError('item not found: {}'.format(x))