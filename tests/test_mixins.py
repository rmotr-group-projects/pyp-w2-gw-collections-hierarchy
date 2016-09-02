import unittest
from collections_hierarchy.mixins import (
    ConstructibleMixin, ConstructibleMixin, ComparableMixin,
    SequenceMixin, OperableMixin, AppendableMixin)


# ====== DO NOT MODIFY ====== #
class AppendableMixinList(ConstructibleMixin, AppendableMixin):
    DATA_DEFAULT_INITIAL = []


class ComparableMixinList(ConstructibleMixin, ComparableMixin):
    DATA_DEFAULT_INITIAL = []


class ComparableMixinDict(ConstructibleMixin, ComparableMixin):
    DATA_DEFAULT_INITIAL = {}


class SequenceMixinList(ConstructibleMixin, SequenceMixin):
    DATA_DEFAULT_INITIAL = []

    def get_elements(self):
        return self.data


class SequenceMixinDict(ConstructibleMixin, SequenceMixin):
    DATA_DEFAULT_INITIAL = {}

    def get_elements(self):
        return list(self.data.items())


class OperableMixinList(ConstructibleMixin, OperableMixin):
    DATA_DEFAULT_INITIAL = []

# ====== DO NOT MODIFY ====== #


class AppendableMixinTestCase(unittest.TestCase):
    def test_appendable_mixin_appends_to_empty_collection(self):
        l = AppendableMixinList()

        l.append(1)
        self.assertEqual(l.data, [1])

        l.append('hello')
        self.assertEqual(l.data, [1, 'hello'])

    def test_appendable_mixin_appends_to_not_empty_collection(self):
        l = AppendableMixinList(['world', 9])

        l.append('Python')
        self.assertEqual(l.data, ['world', 9, 'Python'])


class ComparableMixinTestCase(unittest.TestCase):
    def test_comparables_in_empty_collection(self):
        l1 = ComparableMixinList()
        l2 = ComparableMixinList()
        self.assertEqual(l1, l2)

        d1 = ComparableMixinDict()
        d2 = ComparableMixinDict()
        self.assertEqual(d1, d2)

    def test_comparables_in_non_empty_collection(self):
        l1 = ComparableMixinList([1, 2, 3])
        l2 = ComparableMixinList([1, 2, 3])
        self.assertEqual(l1, l2)

        d1 = ComparableMixinDict({'a': 1, 'b': 2})
        d2 = ComparableMixinDict({'a': 1, 'b': 2})
        self.assertEqual(d1, d2)

    def test_not_equal_length(self):
        l1 = ComparableMixinList([1, 2, 3])
        l2 = ComparableMixinList([1])
        self.assertNotEqual(l1, l2)

        d1 = ComparableMixinDict({'a': 1})
        d2 = ComparableMixinDict({'a': 1, 'b': 2})
        self.assertNotEqual(d1, d2)

    def test_not_equal_elements(self):
        l1 = ComparableMixinList([1, 2, 3])
        l2 = ComparableMixinList([1, 2, 9])
        self.assertNotEqual(l1, l2)

        d1 = ComparableMixinDict({'a': 1, 'b': 9})
        d2 = ComparableMixinDict({'a': 1, 'b': 2})
        self.assertNotEqual(d1, d2)


class SequenceMixinTestCase(unittest.TestCase):#############
    def test_iterator_next(self):
        l = SequenceMixinList(['hello', 9, 'Python'])

        self.assertEqual(next(l), 'hello')
        self.assertEqual(next(l), 9)
        self.assertEqual(next(l), 'Python')

        with self.assertRaises(StopIteration):
            next(l)

        d = SequenceMixinDict({'a': 1, 'b': 2})
        items = list(d.data.items())

        self.assertEqual(next(d), items[0])
        self.assertEqual(next(d), items[1])

        with self.assertRaises(StopIteration):
            next(d)

    def test_iterator_is_rewinded(self):
        l = SequenceMixinList(['hello', 9, 'Python'])
        self.assertEqual(next(l), 'hello')
        it = iter(l)
        self.assertEqual(next(it), 'hello')

        d = SequenceMixinDict({'a': 1, 'b': 2})
        items = list(d.data.items())
        self.assertEqual(next(d), items[0])
        it = iter(d)
        self.assertEqual(next(it), items[0])

    def test_len_for_empty_collections(self):
        l = SequenceMixinList()
        self.assertEqual(len(l), 0)

        d = SequenceMixinDict()
        self.assertEqual(len(d), 0)

    def test_len_for_non_empty_collections(self):
        l = SequenceMixinList(['hello', 9, 'Python'])
        self.assertEqual(len(l), 3)

        d = SequenceMixinDict({'a': 1, 'b': 2})
        self.assertEqual(len(d), 2)

    def test_get_item_for_empty_collections(self):
        l = SequenceMixinList()
        with self.assertRaises(IndexError):
            l[0]

        d = SequenceMixinDict()
        with self.assertRaises(KeyError):
            d['a']

    def test_get_item_for_non_empty_collection(self):
        l = SequenceMixinList(['hello', 9, 'Python'])
        self.assertEqual(l[0], 'hello')
        self.assertEqual(l[1], 9)
        self.assertEqual(l[2], 'Python')

        d = SequenceMixinDict({'a': 1, 'b': 2})
        self.assertEqual(d['a'], 1)
        self.assertEqual(d['b'], 2)

    def test_del_item_for_empty_collections(self):
        l = SequenceMixinList()
        with self.assertRaises(IndexError):
            del l[0]

        d = SequenceMixinDict()
        with self.assertRaises(KeyError):
            del d['a']

    def test_del_item_for_non_empty_collection(self):
        l = SequenceMixinList(['hello', 9, 'Python'])
        del l[0]
        self.assertEqual(l.data, [9, 'Python'])

        l = SequenceMixinList(['hello', 9, 'Python'])
        del l[1]
        self.assertEqual(l.data, ['hello', 'Python'])

        l = SequenceMixinList(['hello', 9, 'Python'])
        del l[2]
        self.assertEqual(l.data, ['hello', 9])

        d = SequenceMixinDict({'a': 1, 'b': 2})
        del d['a']
        self.assertEqual(d.data, {'b': 2})

        d = SequenceMixinDict({'a': 1, 'b': 2})
        del d['b']
        self.assertEqual(d.data, {'a': 1})

    def test_contains_for_empty_collections(self):
        l = SequenceMixinList()
        self.assertFalse(3 in l)

        d = SequenceMixinDict()
        self.assertFalse('a' in d)

    def test_contains_for_non_empty_collection(self):
        l = SequenceMixinList(['hello', 9, 'Python'])
        self.assertTrue('hello' in l)
        self.assertTrue(9 in l)
        self.assertTrue('Python' in l)

        d = SequenceMixinList({'a': 1, 'b': 2})
        self.assertTrue('a' in d)
        self.assertTrue('b' in d)


class OperableMixinTestCase(unittest.TestCase):
    def test_add_with_empty_collection(self):
        l1 = OperableMixinList()
        l2 = OperableMixinList([1, 2, 3])
        self.assertEqual((l1 + l2).data, [1, 2, 3])
        self.assertEqual(l1.data, [])
        self.assertEqual(l2.data, [1, 2, 3])

    def test_add_with_non_empty_collection(self):
        l1 = OperableMixinList([1, 2])
        l2 = OperableMixinList([3, 4])
        self.assertEqual((l1 + l2).data, [1, 2, 3, 4])
        self.assertEqual(l1.data, [1, 2])
        self.assertEqual(l2.data, [3, 4])
