from .mixins import *


class List(ComparableMixin,
           SequenceMixin,
           RepresentableMixin,
           OperableMixin,
           ConstructibleMixin,
           IndexableMixin,
           AppendableMixin):
    DATA_DEFAULT_INITIAL = []

    
    def get_elements(self):
        return getattr(self,self.DATA_ATTR_NAME)
    
    def count(self):
        return len(self.data)
        

class Dict(HashableMixin,
           ComparableMixin,
           SequenceMixin,
           RepresentableMixin,
           ConstructibleMixin):
    DATA_DEFAULT_INITIAL = {}

    def get_elements(self):
        return [key for key in self.data.keys()]
        
    def count(self):
        return len(self.data)
