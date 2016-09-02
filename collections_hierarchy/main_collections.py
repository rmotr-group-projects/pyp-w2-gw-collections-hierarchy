from collections_hierarchy.mixins import *


class List(ConstructibleMixin,
           ComparableMixin,
           SequenceMixin,
           RepresentableMixin,
           OperableMixin,
           IndexableMixin,
           AppendableMixin):
    DATA_DEFAULT_INITIAL = []

    def get_elements(self):
        return self.data
    

class Dict(ConstructibleMixin,
           HashableMixin,
           ComparableMixin,
           SequenceMixin,
           RepresentableMixin):
    DATA_DEFAULT_INITIAL = {}

    def get_elements(self):
        return list(self.data.items())
