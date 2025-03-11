from django.utils.safestring import mark_safe
from django.template import Library

import markdown


register = Library()


@register.filter(name='markdown')
def convert_text_to_markdown(text: str) -> str:
    """Converts text from common format to markdown"""
    return mark_safe(markdown.markdown(text))
