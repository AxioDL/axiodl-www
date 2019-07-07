from django.conf.urls import url, include
from django.urls import path
from django.contrib.auth.decorators import permission_required
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('pages/create/', views.create_page, name='pages.create.page'),
    path('pages/<str:slug>/', views.view_page, name='pages.view.page'),
    path('pages/<str:slug>/delete/', views.delete_page, name='pages.delete.page'),
    path('pages/<str:slug>/edit/',
         permission_required('pages.edit_page')(views.PageUpdateView.as_view()), name='pages.edit.page'),
]
