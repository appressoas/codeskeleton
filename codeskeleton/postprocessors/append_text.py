from .registry import POSTPROCESSOR_REGISTRY


def append_text(content, text=''):
    return '{}{}'.format(content, text)


POSTPROCESSOR_REGISTRY.register(postprocessor_name='append_text',
                                function=append_text)
