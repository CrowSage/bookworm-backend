from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserBook(models.Model):
    class Status(models.TextChoices):
        READING = "reading", "Reading"
        COMPLETED = "completed", "Completed"
        WANT_TO_READ = "want_to_read", "Want to Read"
        Dnf = "dnf", "Did not finished"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=500)
    thumbnail = models.URLField(blank=True, null=True)
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.WANT_TO_READ
    )
    date_started = models.DateField(null=True)
    date_finished = models.DateField(null=True)

    rating = models.IntegerField(null=True, blank=True)
    review = models.TextField(null=True, blank=True)

    date_added = models.DateTimeField(auto_now_add=True)
