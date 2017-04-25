import re

from . import registry

split_regex = re.compile(r'[_ -]+')


def camelcase(value):
    """
    Camel-case a value.

    Args:
        value (str): The value to camel-case.

    Examples:

        Lets say we have a variable named ``project_name`` with
        ``example_project`` as value. The result of::

            {{{ project_name|camelcase }}}

        would be ``ExampleProject``.

    Returns:
        str: The camel cased value.
    """
    value = str(value)
    return ''.join([word.lower().capitalize() for word in split_regex.split(value)])


registry.FILTER_REGISTRY.register('camelcase', camelcase)
