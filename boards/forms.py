from django import forms
from martor.fields import MartorFormField
from .models import Topic, Post, Board


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['name', 'description', 'parent']


class NewTopicForm(forms.ModelForm):
    message = MartorFormField(
        max_length=4000,
        help_text='The max length of the text is 4000.')

    class Meta:
        model = Topic
        fields = ['subject', 'message']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', ]
