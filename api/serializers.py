from rest_framework import serializers
from .models import UserBook
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]


class UserBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBook
        fields = [
            "id",
            "user",
            "book_id",
            "title",
            "authors",
            "thumbnail",
            "status",
            "date_started",
            "date_finished",
            "rating",
            "review",
            "date_added",
        ]
