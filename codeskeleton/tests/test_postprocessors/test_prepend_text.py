import unittest

from codeskeleton.postprocessors.prepend_text import prepend_text


class TestPrependText(unittest.TestCase):
    def test_prepend_text(self):
        self.assertEqual(prepend_text(content='test', text='prefix'), 'prefixtest')

    def test_no_text_argument(self):
        self.assertEqual(prepend_text(content='test'), 'test')
