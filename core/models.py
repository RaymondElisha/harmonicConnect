# core/models.py
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add other profile fields


class EntertainmentServiceProvider(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    # Add fields for the service provider


class Client(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    # Add fields for the client

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    # Add other fields as needed

    def __str__(self):
        return self.title


class Review(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    # Add fields for the review
