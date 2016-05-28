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
        #returns a list of elements 
        return getattr(self, self.DATA_ATTR_NAME)


class Dict(HashableMixin,
           ComparableMixin,
           SequenceMixin,
           RepresentableMixin,
           ConstructibleMixin):
    DATA_DEFAULT_INITIAL = {}
        
    def get_elements(self):
        return getattr(self, self.DATA_ATTR_NAME)
