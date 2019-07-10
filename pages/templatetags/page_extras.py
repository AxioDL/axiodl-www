from django import template
from django.template.defaultfilters import safe
import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

from ..models import Page, Link

register = template.Library()


@register.simple_tag
def get_main_page(*args, **kwargs):
    return Page.objects.get(is_mainpage=True)


@register.simple_tag
def get_pages(*args, **kwargs):
    return Page.objects.all()


@register.simple_tag
def get_links(*args, **kwargs):
    return Link.objects.all()


@register.simple_tag
def has_perm(user, perm):
    return user.has_perm(perm)


@register.simple_tag
def is_app_installed(app):
    from django.apps import apps
    return apps.is_installed(app)


class HighlightRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % \
                   mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = HtmlFormatter()
        return highlight(code, lexer, formatter)


@register.filter
def hilight(value):
    renderer = HighlightRenderer()
    markdown = mistune.Markdown(renderer=renderer)
    print(markdown(value))
    return markdown(value)


@register.simple_tag
def generate_twitter_card(site, title, description, img_url='', creator='', is_large_image=False):
    if is_large_image and img_url != '':
        card = '<meta name="twitter:card" content="summary_large_image" />\n'
    else:
        card = '<meta name="twitter:card" content="summary" />\n'

    card += ('<meta name="twitter:title" content="{0}" />\n'
             '<meta name="twitter:description" content="{1}" />\n').format(site, title, description)

    if img_url != '':
        card += '<meta name="twitter:image" content="{}" />\n'.format(img_url)

    return safe(card)
