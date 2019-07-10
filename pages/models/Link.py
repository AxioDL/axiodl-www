from django.db import models


class Link(models.Model):
    text = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.text
