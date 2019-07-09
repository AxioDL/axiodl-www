from django.contrib import admin
from .models import Page
from .forms.PageForm import PageForm, PageFormAdmin


fields = ['image_tag']

admin.site.register(Page, PageFormAdmin)
