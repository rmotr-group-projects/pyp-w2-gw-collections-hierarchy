# [pyp-w2] Collections Hierarchy

Today, we are going to implement part of the Python collections hierarchy using Mixins.

It's normal to think about the collections hierarchy as a tree. But, a lot of
functionality is shared between classes in different levels of the hierarchy. That's
the perfect use case for Mixins.

Each `Mixin` class will implement just a portion of the collection behavior.
If you evaluate each Mixin by itself, they probably don't make sense, and that's expected.
They are thought to be used together, plugged into bigger classes that combines their functionality.

These are the main Mixins we identified for you (you can find them in the `mixins.py` file):
```
ComparableMixin

SequenceMixin

RepresentableMixin

ConstructibleMixin

OperableMixin

AppendableMixin

HashableMixin

IndexableMixin
```

Each of them has a pre set group of methods you will have to respect and implement.

**The objective of the assignment** is to implement two concrete collection classes: `List` and `Dict` (defined in `main_collections.py`). You can also try creating your own concrete collections, like `Set` or `Tuple` for a few extra points. Make sure to add extra test cases if you write you own extra collections.
