from django.shortcuts import render
from multitenant.library.models import Book, Author, Rental
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    ctx = {
        "books": Book.objects.count(),
        "authors": Author.objects.count(),
        "rentals": Rental.objects.count(),
        "users": User.objects.count(),
    }
    return render(request, "index.html", ctx)


def books(request):
    books = Book.objects.prefetch_related("authors")
    return render(request, "books.html", context={"books": books})


def authors(request):
    authors = Author.objects.all()
    return render(request, "authors.html", context={"authors": authors})


def rentals(request):
    return render(request, "rentals.html")
