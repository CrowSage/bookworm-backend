from rest_framework import serializers
from .models import UserBook
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]


class UserBookSerializer(serializers.ModelSerializer):
    status = serializers.CharField(required=False)

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

    def validate_title(self, value):
        if len(value) > 255:
            return value[:255]
        return value

    def validate_authors(self, value):
        if len(value) > 500:
            return value[:500]
        return value

