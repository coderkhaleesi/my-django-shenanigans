from django.urls import path
from . import views

app_name = 'todo_list'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('delete/<id>', views.delete, name='delete'),
    path('cross_off/<id>', views.crossOff, name='cross_off'),
    path('uncross/<id>', views.uncross, name='uncross'),
    path('edit/<id>', views.edit, name='edit'),
]