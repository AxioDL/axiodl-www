from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.BoardListView.as_view(), name='board.index'),
    url(r'^(?P<pk>\d+)/$', views.TopicListView.as_view(), name='board.topics'),
    url(r'^(?P<pk>\d+)/new/$', views.new_topic, name='board.new.topic'),
    url(r'^(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', views.PostListView.as_view(), name='board.topic.posts'),
    url(r'^(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$', views.reply_topic, name='board.reply.topic'),
    url(r'^(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/posts/(?P<post_pk>\d+)/edit/$',
        views.PostUpdateView.as_view(), name='board.edit.post'),
]
