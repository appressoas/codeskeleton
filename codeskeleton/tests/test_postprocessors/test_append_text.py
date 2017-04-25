import unittest

from codeskeleton.postprocessors.append_text import append_text


class TestAppendText(unittest.TestCase):
    def test_append_text(self):
        self.assertEqual(append_text(content='test', text='suffix'), 'testsuffix')

    def test_no_text_argument(self):
        self.assertEqual(append_text(content='test'), 'test')
