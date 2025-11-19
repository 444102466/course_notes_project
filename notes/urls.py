from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.note_create, name='note_create'),
    path('<int:pk>/', views.note_detail, name='note_detail')



]