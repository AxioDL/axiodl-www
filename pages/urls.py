from django.conf.urls import url, include
from django.urls import path
from django.contrib.auth.decorators import permission_required
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    url(r'^pages/create/$', views.create_page, name='pages.create.page'),
    url(r'^pages/list/$', views.PageListView.as_view(), name='pages.list'),
    url(r'^pages/(?P<slug>[^/]+)/$', views.view_page, name='pages.view.page'),
    url(r'^pages/(?P<slug>[^/]+)/delete/$', views.PageDeleteView.as_view(), name='pages.delete.page'),
    url(r'^pages/(?P<slug>[^/]+)/edit/$',
         permission_required('pages.edit_page')(views.PageUpdateView.as_view()), name='pages.edit.page'),
]
