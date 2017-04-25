import unittest
from collections import OrderedDict

import re

from codeskeleton import exceptions
from codeskeleton import spec


class TestPostprocessFiles(unittest.TestCase):
    def test_deserialize_empty_data(self):
        postprocess_files = spec.PostprocessFiles()
        postprocess_files.deserialize(data={})
        self.assertEqual(len(postprocess_files._regex_to_postprocessor_list), 0)

    def test_deserialize_single_regex(self):
        postprocess_files = spec.PostprocessFiles()
        postprocess_files.deserialize(data={
            r'[a-z]+': {}
        })
        self.assertEqual(len(postprocess_files._regex_to_postprocessor_list), 1)
        self.assertEqual(postprocess_files._regex_to_postprocessor_list[0][0],
                         re.compile(r'[a-z]+'))
        self.assertEqual(postprocess_files._regex_to_postprocessor_list[0][1],
                         {})

    def test_deserialize_single_regex_multiple_files(self):
        postprocess_files = spec.PostprocessFiles()
        postprocess_files.deserialize(data={
            r'[a-z]+': OrderedDict([
                ('postprocessor1', {}),
                ('postprocessor2', {'a': 10}),
            ])
        })
        self.assertEqual(len(postprocess_files._regex_to_postprocessor_list), 1)
        postprocessor_map = postprocess_files._regex_to_postprocessor_list[0][1]
        self.assertIn('postprocessor1', postprocessor_map)
        self.assertIn('postprocessor2', postprocessor_map)
        self.assertEqual(postprocessor_map['postprocessor1'], {})
        self.assertEqual(postprocessor_map['postprocessor2'], {'a': 10})

    def test_postprocess_file_no_regex_match(self):
        postprocess_files = spec.PostprocessFiles()
        postprocess_files.deserialize(data={
            r'^.+\.py$': OrderedDict([
                ('append_text', {'text': 'test'})
            ])
        })
        self.assertEqual(
            postprocess_files.postprocess_file(filename='test.txt',
                                               content='Original'),
            'Original')

    def test_postprocess_file_has_regex_match(self):
        postprocess_files = spec.PostprocessFiles()
        postprocess_files.deserialize(data={
            r'^.+\.py$': OrderedDict([
                ('append_text', {'text': 'test'})
            ])
        })
        self.assertEqual(
            postprocess_files.postprocess_file(filename='test.py',
                                               content='Original'),
            'Originaltest')

    def test_postprocess_file_multiple_postprocessors(self):
        postprocess_files = spec.PostprocessFiles()
        postprocess_files.deserialize(data={
            r'^.+\.py$': OrderedDict([
                ('append_text', {'text': 'suffix'}),
                ('prepend_text', {'text': 'prefix'}),
            ])
        })
        self.assertEqual(
            postprocess_files.postprocess_file(filename='test.py',
                                               content='Original'),
            'prefixOriginalsuffix')

    def test_validate_spec_invalid_postprocessor_name(self):
        postprocess_files = spec.PostprocessFiles()
        postprocess_files.deserialize(data={
            r'^.+\.py$': OrderedDict([
                ('invalidstuff', {}),
            ])
        })
        with self.assertRaisesRegex(exceptions.SpecValidationError,
                                    'mock: Invalid postprocessor name'):
            postprocess_files.validate_spec(path='mock')

    def test_validate_spec_valid_postprocessor_name(self):
        postprocess_files = spec.PostprocessFiles()
        postprocess_files.deserialize(data={
            r'^.+\.py$': OrderedDict([
                ('append_text', {}),
            ])
        })
        postprocess_files.validate_spec(path='mock')  # No SpecValidationError
