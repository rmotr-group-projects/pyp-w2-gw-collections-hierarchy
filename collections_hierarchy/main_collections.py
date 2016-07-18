from collections_hierarchy.mixins import *


class List(ComparableMixin,
           SequenceMixin,
           RepresentableMixin,
           OperableMixin,
           ConstructibleMixin,
           IndexableMixin,
           AppendableMixin):
    DATA_DEFAULT_INITIAL = []

    def get_elements(self):
        return [elem for elem in getattr(self, self.DATA_ATTR_NAME)]
        
    def count(self):
        return len(getattr(self, self.DATA_ATTR_NAME))


class Dict(HashableMixin,
           ComparableMixin,
           SequenceMixin,
           RepresentableMixin,
           ConstructibleMixin):
    DATA_DEFAULT_INITIAL = {}

    def get_elements(self):
        return [key for key in getattr(self, self.DATA_ATTR_NAME)]

    def count(self):
        return len(getattr(self, self.DATA_ATTR_NAME))
        
        
class Tuple(ComparableMixin,
            SequenceMixin,
            RepresentableMixin,
            ConstructibleMixin,
            IndexableMixin):
    DATA_DEFAULT_INITIAL = ()

    def get_elements(self):
        return [elem for elem in getattr(self, self.DATA_ATTR_NAME)]
        
    def count(self):
        return len(getattr(self, self.DATA_ATTR_NAME))