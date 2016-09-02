from collections_hierarchy.mixins import *


class List(ComparableMixin,
           SequenceMixin,
           RepresentableMixin,
           OperableMixin,
           ConstructibleMixin,
           IndexableMixin,
           AppendableMixin):
    DATA_DEFAULT_INITIAL = []
    
    def count(self):
        return len(self)
    
    def get_elements(self):
        return self.data
    


class Dict(HashableMixin,
           ComparableMixin,
           SequenceMixin,
           RepresentableMixin,
           ConstructibleMixin):
    DATA_DEFAULT_INITIAL = {}

    def get_elements(self):
        return self.data.keys()
    
    def count(self):
        return len(self)
        
    def __setitem__(self, key, value):
        self.data.update({key:value})
        return self