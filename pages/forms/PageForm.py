from django import forms
from django.contrib import admin
from martor.fields import MartorFormField
from ..models import Page


class PageForm(forms.ModelForm):
    page_name = forms.CharField(label='Page Name', max_length=100, required=True)
    description = forms.CharField(label='Page Description', max_length=200, required=True)
    content = MartorFormField()
    is_mainpage = forms.BooleanField(label='Is Main Page?', required=False)
    logo = forms.ImageField()

    class Meta:
        model = Page
        fields = ['page_name', 'description', 'content', 'logo', 'is_mainpage']


class PageFormAdmin(admin.ModelAdmin):
    form = PageForm
