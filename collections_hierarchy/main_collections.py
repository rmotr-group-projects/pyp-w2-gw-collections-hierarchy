from collections_hierarchy.mixins import *
#from mixins import *

class List(ComparableMixin,
           SequenceMixin,
           RepresentableMixin,
           OperableMixin,
           ConstructibleMixin,
           IndexableMixin,
           AppendableMixin):
    DATA_DEFAULT_INITIAL = []

    def get_elements(self):
        # returns a list of the elements in List
        return getattr(self, self.DATA_ATTR_NAME)

class Dict(HashableMixin,
           ComparableMixin,
           SequenceMixin,
           RepresentableMixin,
           ConstructibleMixin):
    DATA_DEFAULT_INITIAL = {}

    def get_elements(self):
        # return a list of the keys from the dict
        # python2 .keys() gives a list, in python3 it give a dict_keys iterable
        # Using sorted since the tox tests seem to expect keys to be sorted
        return sorted(list(getattr(self, self.DATA_ATTR_NAME).keys()))

