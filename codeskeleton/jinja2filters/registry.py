class FilterRegistry(object):
    """
    Registry of Jinja2 filters available when processing templates.
    """
    def __init__(self):
        self._filters = {}

    def register(self, filter_name, function):
        """
        Register a filter function.

        Args:
            filter_name (str): The name of the filter.
            function: The filter function.
        """
        self._filters[filter_name] = function

    def as_dict(self):
        return self._filters


#: The filter registry. Use this to access the filter registry
#: (do not create a new :class:`.FilterRegistry` object.
FILTER_REGISTRY = FilterRegistry()
