import unittest
from collections import OrderedDict

from codeskeleton import spec


class TestSpecCache(unittest.TestCase):
    def test_clear(self):
        cache = spec.SpecCache()
        cache.specs = OrderedDict([
            ('a', spec.Tree(base_directory='/mock1')),
            ('b', spec.Tree(base_directory='/mock2')),
        ])
        cache.clear()
        self.assertEqual(cache.specs, OrderedDict())

    def test_add_spec(self):
        cache = spec.SpecCache()
        tree = spec.Tree(base_directory='/mock', context='thecontext', id='mock')
        cache.add_spec(tree)
        self.assertEqual(cache.specs['thecontext.mock'], tree)

    def test_add_specs(self):
        cache = spec.SpecCache()
        tree1 = spec.Tree(base_directory='/mock1', context='thecontext', id='mock1')
        tree2 = spec.Tree(base_directory='/mock2', context='thecontext', id='mock2')
        cache.add_specs(tree1, tree2)
        self.assertEqual(len(cache.specs), 2)
        self.assertEqual(cache.specs['thecontext.mock1'], tree1)
        self.assertEqual(cache.specs['thecontext.mock2'], tree2)

    def test_get_by_id_valid_id(self):
        cache = spec.SpecCache()
        tree = spec.Tree(base_directory='/mock', context='thecontext', id='mock')
        cache.add_spec(tree)
        self.assertEqual(cache.get_spec('thecontext.mock'), tree)

    def test_get_by_id_invalid_id(self):
        cache = spec.SpecCache()
        with self.assertRaises(KeyError):
            cache.get_spec('test')
