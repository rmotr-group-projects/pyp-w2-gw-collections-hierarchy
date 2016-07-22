import unittest
import six

from collections_hierarchy.main import *


class DictTestCase(unittest.TestCase):

    def test_dict_create(self):
        d1 = Dict({'a': 1, 'b': 2})
        self.assertEqual(d1['a'], 1)
        with self.assertRaises(KeyError):
            d1['hello']

    def test_dict_iter(self):
        d1 = Dict({'a': 1, 'b': 2}) #{'a': 1, 'b': 2}
        print('RANDOM STUFF TO FIND: ', d1.get_elements())
        print([key for key in d1])
        for key in d1:
            print key
        print('*****************************************************')
        six.assertCountEqual(self, [key for key in d1], ['a', 'b'])

    def test_dict_contains(self):
        d1 = Dict({'a': 1, 'b': 2})
        self.assertTrue('a' in d1)
        self.assertFalse('z' in d1)

    def test_dict_len(self):
        d1 = Dict({'a': 1, 'b': 2})
        self.assertEqual(len(d1), 2)

    def test_dict_count(self):
        d1 = Dict({'a': 1, 'b': 2})
        self.assertEqual(d1.count(), 2)

    def test_dict_eq(self):
        d1 = Dict({'a': 1, 'b': 2})
        self.assertTrue(d1 == Dict({'a': 1, 'b': 2}))

    def test_dict_setitem(self):
        d1 = Dict({'a': 1, 'b': 2})
        d1['z'] = 10
        self.assertEqual(d1, Dict({'a': 1, 'b': 2, 'z': 10}))

    def test_dict_keys(self):
        six.assertCountEqual(self, Dict({'a': 1, 'b': 2}).keys(), ['a', 'b'])

    def test_dict_values(self):
        six.assertCountEqual(self, Dict({'a': 1, 'b': 2}).values(), [1, 2])

    def test_dict_items(self):
        six.assertCountEqual(
            self, 
            Dict({'a': 1, 'b': 2}).items(), 
            [('a', 1), ('b', 2)]
        )
