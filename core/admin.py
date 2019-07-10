from django.contrib import admin
from .models import Page, Link
from .forms.PageForm import PageFormAdmin

fields = ['image_tag']

admin.site.register(Page, PageFormAdmin)
admin.site.register(Link)
