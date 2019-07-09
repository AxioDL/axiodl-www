from django.contrib import admin
from .models import Board, Category
from .forms import BoardForm


class BoardInline(admin.TabularInline):
    model = Board
    verbose_name = 'Child Board'
    verbose_name_plural = 'Child Boards'


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        BoardInline,
    )

