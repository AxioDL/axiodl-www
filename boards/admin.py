from django.contrib import admin
import nested_admin
from .models import Board, Category, Topic, Post


class BoardInline(nested_admin.NestedStackedInline):
    model = Board
    verbose_name = 'Child Board'
    verbose_name_plural = 'Child Boards'


class PostInline(nested_admin.NestedStackedInline):
    model = Post
    verbose_name = 'Topic'
    verbose_name_plural = 'Topics'


class TopicsInline(nested_admin.NestedStackedInline):
    model = Topic
    verbose_name = 'Topic'
    verbose_name_plural = 'Topics'
    inlines = (PostInline, )


@admin.register(Board)
class BoardAdmin(nested_admin.NestedModelAdmin):
    inlines = (BoardInline, TopicsInline,)
    list_display = ('name',
                    'description',
                    'category',
                    'parent',)
    list_select_related = ('category',
                           'parent',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        BoardInline,
    )

