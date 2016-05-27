from collections_hierarchy.mixins import *


class List(ComparableMixin,
           SequenceMixin,
           RepresentableMixin,
           OperableMixin,
           ConstructibleMixin,
           IndexableMixin,
           AppendableMixin):
    DATA_DEFAULT_INITIAL = []
    
    def __init__(self, values):
        self.values = values
        self.i = -1

    def get_elements(self):
        pass


class Dict(HashableMixin,
           ComparableMixin,
           SequenceMixin,
           RepresentableMixin,
           ConstructibleMixin):
    DATA_DEFAULT_INITIAL = {}
    
    def __init__(self, values):
        self.values = values
        self.i = -1
        
    def get_elements(self):
        pass
