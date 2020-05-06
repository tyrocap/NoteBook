from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass


class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=300, blank=True, null=True)
    primary_isbn13 = models.CharField(max_length=50, blank=True, null=True)
    preview_link_google = models.CharField(max_length=300, blank=True, null=True)
    page_count = models.IntegerField(blank=True, null=True)
    average_rating = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    rating_count = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('notes_page', args=[str(self.id)])


class Note(models.Model):
    note_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    note_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    note_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    note_date = models.DateTimeField(auto_now_add=True)
    note_body = models.TextField(max_length=255)

    def __str__(self):
        return self.note_body[:25]

