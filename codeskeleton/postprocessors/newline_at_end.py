from .registry import POSTPROCESSOR_REGISTRY


def newline_at_end(content):
    content = content.rstrip()
    content = '{}\n'.format(content)
    return content


POSTPROCESSOR_REGISTRY.register(postprocessor_name='newline_at_end',
                                function=newline_at_end)
