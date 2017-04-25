import unittest

from codeskeleton.postprocessors.newline_at_end import newline_at_end


class TestNewlineAtEnd(unittest.TestCase):
    def test_already_ok(self):
        self.assertEqual(newline_at_end(content='test\n'), 'test\n')

    def test_adds_if_no_newline(self):
        self.assertEqual(newline_at_end(content='test'), 'test\n')

    def test_fixes_if_strange_whitespace(self):
        self.assertEqual(newline_at_end(content='test   \n  '), 'test\n')

    def test_empty_string_does_not_get_newline_added(self):
        self.assertEqual(newline_at_end(content=''), '')
