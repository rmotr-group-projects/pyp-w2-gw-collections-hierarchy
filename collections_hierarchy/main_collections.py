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
        # should return a list of elements
        return getattr(self, self.DATA_ATTR_NAME)
        

class Dict(HashableMixin,
           ComparableMixin,
           SequenceMixin,
           RepresentableMixin,
           ConstructibleMixin):
    DATA_DEFAULT_INITIAL = {}

    def get_elements(self):
        return list(getattr(self, self.DATA_ATTR_NAME).keys())
    
    
# my_dict = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}
# for thing in my_dict:
#     print thing
# 
#
# a_list = List([1, 2])
# __init__(initial=[1, 2])
# a_list.data = [1, 2]
# getattr(a_list, "data") # [1, 2]

# other_list = List()
# __init__(initial=None)
# a_list.data = []