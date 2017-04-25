from .registry import POSTPROCESSOR_REGISTRY


def prepend_text(content, text=''):
    return '{}{}'.format(text, content)


POSTPROCESSOR_REGISTRY.register(postprocessor_name='prepend_text',
                                function=prepend_text)
