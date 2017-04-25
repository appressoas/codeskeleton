import unittest

from codeskeleton import jinja2filters


class TestCamelCase(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(jinja2filters.camelcase.camelcase('test'), 'Test')

    def test_multiple_dashes(self):
        self.assertEqual(jinja2filters.camelcase.camelcase('my_awesome_test'), 'MyAwesomeTest')

    def test_multiple_words(self):
        self.assertEqual(jinja2filters.camelcase.camelcase('my awesome test'), 'MyAwesomeTest')

    def test_small_and_large_letter_combinations(self):
        self.assertEqual(jinja2filters.camelcase.camelcase('mY_aweSOME_tESt'), 'MyAwesomeTest')
