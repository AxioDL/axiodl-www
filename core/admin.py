from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path
from .models import Page, Link
from .forms.PageForm import PageFormAdmin

fields = ['image_tag']


@admin.register(Link)
class MyModelAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('my_view/', self.my_view),
        ]
        return my_urls + urls

    def my_view(self, request):
        # ...
        context = dict(
            # Include common variables for rendering the admin template.
            self.admin_site.each_context(request),
        )
        return TemplateResponse(request, "admin/preferences/preferences.html", context)


admin.site.register(Page, PageFormAdmin)
#admin.site.register(Link)
