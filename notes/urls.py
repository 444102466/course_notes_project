from django.urls import path
from . import views

app_name = "notes"
urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("<int:note_id>/", views.detail, name="detail"),
    path("<int:note_id>/edit/", views.edit, name="edit"),
    path("<int:note_id>/confirm-delete/", views.confirm_delete, name="confirm_delete"),
    path("<int:note_id>/delete/", views.delete_note, name="delete_note"),
]