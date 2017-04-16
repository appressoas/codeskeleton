import os

import yaml

from codeskeleton import template
from codeskeleton.spec.abstract_spec_object import AbstractSpecObject
from codeskeleton.spec.variables import Variables


class AbstractToplevel(AbstractSpecObject):
    """
    Abstract base class for parsers/data structures for an entire spec file.
    """
    @classmethod
    def from_file(cls, yaml_file_path):
        base_directory = os.path.dirname(yaml_file_path)
        with open(yaml_file_path, encoding='utf-8') as f:
            data = yaml.load(f.read())
        toplevel = cls(base_directory=base_directory)
        toplevel.deserialize(data)
        return toplevel

    def __init__(self, base_directory, id=None, title=None, description=None, variables=None):
        """

        Args:
            base_directory: Base directory where the files for the spec template files are located.
                Normally the directory where the spec file is located.
            id: The ID of the spec. Used to uniquely identify the spec.
            title (optional): Short user friendly description of what the spec creates.
            description (optional): Long user friendly description of what the spec creates.
            variables (codeskeleton.spec.variables.Variables): Variable definitions for the spec.
        """
        self.base_directory = base_directory
        self.id = id
        self._title = title
        self.description = description
        self.variables = variables or Variables()

    @property
    def title(self):
        return self._title or self.id

    def has_title(self):
        return bool(self._title)

    def deserialize(self, data):
        """
        Deserialize the provided data.

        Args:
            data (dict): A dict like object with one of the following key/value pairs:

                - ``id``: A string with the ID of the tree spec.
                - ``title`` (optional): String with a short user friendly description of what
                  this tree spec creates.
                - ``description`` (optional): String with a long user friendly description of
                  what this tree spec creates.
                - ``variables`` (optional): Data on a format that can be parsed by
                  :meth:`codeskeleton.spec.variables.Variables.deserialize`.
        """
        self.id = data.get('id', None)
        self._title = data.get('title', None)
        self.description = data.get('description', None)
        self.variables = Variables()
        self.variables.deserialize(data.get('variables', {}))

    def make_template_environment(self):
        """
        Make a jinja2 template environment for this tree.

        See :func:`codeskeleton.template.make_environment`.
        """
        return template.make_environment(base_directory=self.base_directory,
                                         variables=self.variables.values_as_dict())

    def validate_spec(self):
        self.variables.validate_spec(path='variables')
