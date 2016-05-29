class ComparableMixin(object):
    def __eq__(self, other):
        self_list = getattr(self, self.DATA_ATTR_NAME)
        other_list = getattr(other, other.DATA_ATTR_NAME)
        self_type = type(self_list)
        other_type = type(other_list)
        
        if self_type != other_type:
            return False
        
        if len(self_list) != len(other_list):
            return False
        
        if self_type == list:
            for x, y in zip(self_list, other_list):
              if x != y:
                return False
        if self_type == dict:
            for x, y in zip(self_list.items(), other_list.items()):
              if x != y:
                  return False
        return True
        
    def __ne__(self, other):
        return not self == other

class SequenceMixin(object):
    def __iter__(self):
        self.current = iter(self.get_elements())
        return self.current

    def __next__(self):
        """This method will rely on the get_elements() method of the
        concrete class.
        """
        try:
            getattr(self, 'current')
        except AttributeError:
            self.current = iter(self)
        return next(self.current)

    next = __next__

    def __len__(self):
        return sum(1 for i in self)
        
    count = __len__

    def __getitem__(self, key):
        return getattr(self, self.DATA_ATTR_NAME)[key]

    def __setitem__(self, key, value):
        getattr(self, self.DATA_ATTR_NAME)[key] = value

    def __delitem__(self, key):
        del getattr(self, self.DATA_ATTR_NAME)[key]

    def __contains__(self, item):
        for elem in self:
            if item == elem:
                return True
        return False


class RepresentableMixin(object):
    def __repr__(self):
        return str(self)

    def __str__(self):
        self_type = type(getattr(self, self.DATA_ATTR_NAME))
        if self_type == list:
            return '[{}]'.format(', '.join(str(i) for i in self))


class ConstructibleMixin(object):
    DATA_ATTR_NAME = 'data'

    def __init__(self, initial=None):
        setattr(self, self.DATA_ATTR_NAME,
                initial or self.DATA_DEFAULT_INITIAL)


class OperableMixin(object):
    def __add__(self, other):
        mixin_type = type(self)
        new_elements = getattr(self, self.DATA_ATTR_NAME) + getattr(other, other.DATA_ATTR_NAME)
        return mixin_type(new_elements)

    def __iadd__(self, other):
        return self + other


class AppendableMixin(object):
    def append(self, elem):
        getattr(self, self.DATA_ATTR_NAME).append(elem)


class HashableMixin(object):
    def keys(self):
        return sorted(list(getattr(self, self.DATA_ATTR_NAME).keys()))

    def values(self):
        return sorted(list(getattr(self, self.DATA_ATTR_NAME).values()))

    def items(self):
        return sorted(list(getattr(self, self.DATA_ATTR_NAME).items()))


class IndexableMixin(object):
    def index(self, x):
        return getattr(self, self.DATA_ATTR_NAME).index(x)
