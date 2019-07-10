from django import forms
from django.contrib import admin
from martor.fields import MartorFormField
from ..models import Page


class PageForm(forms.ModelForm):
    content = MartorFormField()
    slug = forms.SlugField(disabled=True, required=False)

    class Meta:
        model = Page
        fields = ['page_name', 'description', 'content', 'logo', 'is_mainpage', 'hidden', 'slug']


class PageFormAdmin(admin.ModelAdmin):
    form = PageForm
