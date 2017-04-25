class PostprocessorRegistry(object):
    """
    Registry of validators for
    :class:`codeskeleton.spec.variable.Variable`.
    """
    def __init__(self):
        self.postprocessor_map = {}

    def register(self, postprocessor_name, function):
        """
        Register a postprocessor function.

        Args:
            postprocessor_name (str): The name of the postprocessor.
            function: The postprocessor function. The postprocessor function
                must raise :exc:`codeskeleton.exceptions.ValueValidationError`
                if validation fails.
        """
        self.postprocessor_map[postprocessor_name] = function

    def postprocess(self, postprocessor_name, content, kwargs):
        """
        Postprocess some content.

        Args:
            postprocessor_name (str): Name of the postprocessor to execute.
            content (str): The content to postprocess.
            kwargs (dict): Kwargs for the postprocessor callable.

        Raises:
            codeskeleton.exceptions.ValueValidationError: If validation fails.
        """
        return self.postprocessor_map[postprocessor_name](content=content, **kwargs)

    def __contains__(self, postprocessor_name):
        """
        Returns ``True`` if we have a postprocessor with the provided ``postprocessor_name`` in the registry.
        """
        return postprocessor_name in self.postprocessor_map

    def namelist(self):
        """
        Get the names of all postprocessor_map in the registry as a list of strings.
        """
        return list(self.postprocessor_map.keys())


#: The postprocessor registry. Use this to access the postprocessor registry
#: (do not create a new :class:`.PostprocessorRegistry` object.
POSTPROCESSOR_REGISTRY = PostprocessorRegistry()
