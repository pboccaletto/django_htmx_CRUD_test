from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.index_create, name='index_create'),
    path('read/', views.index_read, name='index_read'),
    path('update/', views.index_update, name='index_update'),
    path('delete/', views.index_delete, name='index_delete'),
]