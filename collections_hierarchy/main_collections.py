from collections_hierarchy.mixins import *


class List(ComparableMixin,
           SequenceMixin,
           RepresentableMixin,
           OperableMixin,
           ConstructibleMixin,
           IndexableMixin,
           AppendableMixin):
    DATA_DEFAULT_INITIAL = []
#do constructible, indexable and appendable first?
    def get_elements(self):
        elementlist = []
        # for element in getattr(self, DATA_ATTR_NAME):
        for element in self:
            elementlist.append(element)
        return elementlist


class Dict(HashableMixin,
           ComparableMixin,
           SequenceMixin,
           RepresentableMixin,
           ConstructibleMixin):
    DATA_DEFAULT_INITIAL = {}
#do constructible and hashable
    def get_elements(self):
        elementlist = []
        # for key, value in getattr(self, DATA_ATTR_NAME):
        for key, value in self:
            elementlist.append(value)
        return elementlist