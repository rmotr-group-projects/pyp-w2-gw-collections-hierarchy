from collections_hierarchy.mixins import *
from itertools import count as it_count


class List(ComparableMixin,
           SequenceMixin,
           RepresentableMixin,
           OperableMixin,
           ConstructibleMixin,
           IndexableMixin,
           AppendableMixin):
    DATA_DEFAULT_INITIAL = []
    
    def count(self):
        the_data = self.get_elements()
        return len(the_data)

    def get_elements(self):
        
        #return iterable object 
        return self.data
  


class Dict(HashableMixin,
           ComparableMixin,
           SequenceMixin,
           RepresentableMixin,
           ConstructibleMixin):
    DATA_DEFAULT_INITIAL = {}
    
    def count(self):
        the_data = self.get_elements()
        return len(the_data)

    def get_elements(self):
        return self.data.keys()
