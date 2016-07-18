# -*- coding: utf-8 -*-
import unittest

from collections_hierarchy.main_collections import *


class TupleTestCase(unittest.TestCase):

    def test_tuple_create(self):
        t1 = Tuple((2, 4, 6, 8, 10))
        self.assertEqual(t1[0], 2)
        self.assertEqual(t1[2], 6)

    # NOT SURE ABOUT THIS TWO TESTS
    # def test_tuple_iadd(self):
    #     t1 = Tuple((2, 4, 6, 8, 10))
    #     t1 += Tuple((20, 30, 40))
    #     self.assertEqual(t1, Tuple((2, 4, 6, 8, 10, 20, 30, 40)))

    # def test_tuple_add(self):
    #     t1 = Tuple((2, 4, 6, 8, 10))
    #     t2 = t1 + Tuple((20, 30, 40))
    #     self.assertEqual(t1, Tuple((2, 4, 6, 8, 10)))
    #     self.assertEqual(t2, Tuple((2, 4, 6, 8, 10, 20, 30, 40)))
    #     self.assertNotEqual(id(t1), id(t2))

    def test_tuple_len(self):
        t1 = Tuple((2, 4, 6, 8, 10))
        self.assertEqual(len(t1), 5)

    def test_tuple_count(self):
        t1 = Tuple((2, 4, 6, 8, 10))
        self.assertEqual(t1.count(), 5)

    def test_tuple_eq(self):
        t1 = Tuple((2, 4, 6, 8, 10))
        self.assertTrue(t1 == Tuple((2, 4, 6, 8, 10)))

    def test_tuple_ne(self):
        t1 = Tuple((2, 4, 6, 8, 10))
        self.assertTrue(t1 != Tuple((2, 4)))

    def test_tuple_index(self):
        t1 = Tuple((2, 4, 6, 8, 10))
        self.assertEqual(t1.index(10), 4)
        with self.assertRaises(ValueError):
            t1.index("hello")

    def test_tuple_iterable(self):
        t1 = Tuple((2, 4, 6, 8, 10))
        expected = []
        for elem in t1:
            expected.append(elem)
        expected = Tuple(tuple(expected))
        self.assertEqual(t1, expected)

    def test_tuple_contains(self):
        t1 = Tuple((2, 4, 6, 8, 10))
        self.assertTrue(4 in t1)

    def test_tuple_str(self):
        t1 = Tuple((2, 4, 6, 8, 10))
        self.assertEqual(str(t1), "(2, 4, 6, 8, 10)")
