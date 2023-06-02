from django.urls import path

from multitenant.library import views

urlpatterns = [
    path("", views.index, name="index"),
    path("books/", views.books, name="books"),
    path("authors/", views.authors, name="authors"),
    path("rentals/", views.rentals, name="rentals"),
]
