from django import template
import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

from ..models import Page
register = template.Library()


@register.simple_tag
def get_main_page(*args, **kwargs):
    return Page.objects.get(is_mainpage=True)

@register.simple_tag
def get_pages(*args, **kwargs):
    return Page.objects.all()


@register.simple_tag
def has_perm(user, perm):
    return user.has_perm(perm)


@register.simple_tag
def is_app_installed(app):
    from django.apps import apps
    return apps.is_installed(app)
