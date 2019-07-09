from django.db import models, transaction
from django.utils.text import slugify
from django.conf import settings
from django.utils.html import mark_safe
from martor.models import MartorField

from www.fields import UniqueBooleanField


class Page(models.Model):
    page_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='page', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name='+', on_delete=models.CASCADE)
    is_mainpage = UniqueBooleanField(verbose_name='Main Page')
    hidden = models.BooleanField(default=False, blank=True)
    description = models.CharField(max_length=200)
    content = MartorField(null=True, blank=True)
    logo = models.ImageField(upload_to='images', null=True, blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.page_name

    @transaction.atomic
    def save(self, *args, **kwargs):
        print('Page!')
        self.slug = slugify(self.page_name)
        super(Page, self).save(*args, **kwargs)

    def image_tag(self):
        return mark_safe('<img src="/media/images/%s" width="150" height="150" />' % self.logo)

    image_tag.short_description = 'Image'

