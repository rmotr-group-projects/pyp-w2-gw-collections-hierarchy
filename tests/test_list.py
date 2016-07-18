# -*- coding: utf-8 -*-
import unittest

from collections_hierarchy.main_collections import *


class ListTestCase(unittest.TestCase):

    def test_list_create(self):
        l1 = List([2, 4, 6, 8, 10])
        self.assertEqual(l1[0], 2)
        self.assertEqual(l1[2], 6)

    def test_list_iadd(self):
        l1 = List([2, 4, 6, 8, 10])
        l1 += List([20, 30, 40])
        self.assertEqual(l1, List([2, 4, 6, 8, 10, 20, 30, 40]))

    def test_list_add(self):
        l1 = List([2, 4, 6, 8, 10])
        l2 = l1 + List([20, 30, 40])
        self.assertEqual(l1, List([2, 4, 6, 8, 10]))
        self.assertEqual(l2, List([2, 4, 6, 8, 10, 20, 30, 40]))
        self.assertNotEqual(id(l1), id(l2))

    def test_list_append(self):
        l1 = List([2, 4, 6, 8, 10])
        l1.append(20)
        self.assertEqual(l1, List([2, 4, 6, 8, 10, 20]))

    def test_list_len(self):
        l1 = List([2, 4, 6, 8, 10])
        self.assertEqual(len(l1), 5)

    def test_list_count(self):
        l1 = List([2, 4, 6, 8, 10])
        self.assertEqual(l1.count(), 5)

    def test_list_eq(self):
        l1 = List([2, 4, 6, 8, 10])
        self.assertTrue(l1 == List([2, 4, 6, 8, 10]))

    def test_list_ne(self):
        l1 = List([2, 4, 6, 8, 10])
        self.assertTrue(l1 != List([2, 4]))

    def test_list_index(self):
        l1 = List([2, 4, 6, 8, 10])
        self.assertEqual(l1.index(10), 4)
        with self.assertRaises(ValueError):
            l1.index("hello")

    def test_list_iterable(self):
        l1 = List([2, 4, 6, 8, 10])
        expected = []
        for elem in l1:
            expected.append(elem)
        expected = List(expected)
        self.assertEqual(l1, expected)

    def test_list_contains(self):
        l1 = List([2, 4, 6, 8, 10])
        self.assertTrue(4 in l1)

    def test_list_str(self):
        l1 = List([2, 4, 6, 8, 10])
        self.assertEqual(str(l1), "[2, 4, 6, 8, 10]")
    def test_list_repr(self):
        l1 = List([2, 4, 6, 8, 10])
        self.assertEqual(repr(l1), "[2, 4, 6, 8, 10]")