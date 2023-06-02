from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    __str__ = lambda self: f"Book: {self.title}"


class Author(models.Model):
    name = models.CharField(max_length=255)
    notes = models.TextField()
    books = models.ManyToManyField(Book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    get_name = lambda self: self.name

    __str__ = lambda self: f"Author: {self.name}"


class Rental(models.Model):
    user = models.ForeignKey(User, related_name="rentals", on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name="rentals", on_delete=models.CASCADE)
    rental_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    __str__ = lambda self: f"Rental: {self.book.title} by {self.user.username}"
