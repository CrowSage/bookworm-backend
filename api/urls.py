from django.urls import path
from .views import register, add_book, library, update_book, delete_book

urlpatterns = [
    path("register/", view=register, name="register"),
    path("library/", view=library, name="library"),
    path("library/add/", view=add_book, name="add-book"),
    path("library/<int:pk>/update/", view=update_book, name="update-book"),
    path("library/<int:pk>/delete/", view=delete_book, name="delete-book"),
]
