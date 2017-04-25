from collections import OrderedDict

import re

from codeskeleton import exceptions
from codeskeleton import postprocessors
from codeskeleton.spec.abstract_spec_object import AbstractSpecObject


class PostprocessFiles(AbstractSpecObject):
    def __init__(self, postprocess_files=None):
        self._regex_to_postprocessor_list = []
        if postprocess_files:
            self._append_from_map(postprocess_files_map=postprocess_files)

    def _append(self, uncompiled_regex, postprocessor_map):
        self._regex_to_postprocessor_list.append(
            (re.compile(uncompiled_regex), postprocessor_map))

    def _append_from_map(self, postprocess_files_map):
        postprocess_files = postprocess_files_map or {}
        for uncompiled_regex, postprocessor_map in postprocess_files.items():
            self._append(uncompiled_regex=uncompiled_regex,
                         postprocessor_map=postprocessor_map)

    def deserialize(self, data):
        self._regex_to_postprocessor_list = []
        self._append_from_map(postprocess_files_map=data)

    def postprocess_file(self, filename, content):
        for regex, postprocessor_map in self._regex_to_postprocessor_list:
            if regex.match(filename):
                for postprocessor_name, kwargs in postprocessor_map.items():
                    content = postprocessors.POSTPROCESSOR_REGISTRY.postprocess(
                        postprocessor_name=postprocessor_name,
                        content=content,
                        kwargs=kwargs)
        return content

    def validate_spec(self, path):
        for regex, postprocessor_map in self._regex_to_postprocessor_list:
            for postprocessor_name in postprocessor_map:
                if postprocessor_name not in postprocessors.POSTPROCESSOR_REGISTRY:
                    raise exceptions.SpecValidationError(
                        path=path,
                        message='Invalid postprocessor name: {!r}. Must be one of: {}'.format(
                            postprocessor_name, ', '.join(postprocessors.POSTPROCESSOR_REGISTRY.namelist())))

    def __len__(self):
        return len(self._regex_to_postprocessor_list)
