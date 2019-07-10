from django import template
from axiodl import sitesettings

register = template.Library()


@register.simple_tag
def is_site_locked():
    return sitesettings.is_site_locked()


@register.simple_tag
def get_site_name():
    return sitesettings.configuration.site_name

@register.simple_tag
def get_site_slogan():
    return sitesettings.configuration.site_slogan
