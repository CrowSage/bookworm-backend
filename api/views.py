from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import UserBook, User
from .serializers import UserBookSerializer


# Create your views here.
@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):
    username = request.data.get("username")
    email = request.data.get("email", "")
    password = request.data.get("password")

    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already taken!"}, status=400)

    User.objects.create_user(username=username, password=password, email=email)
    return Response({"message": "User Created Successfully!"}, status=201)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def library(request):
    books = UserBook.objects.filter(user=request.user)

    if not books.exists():
        return Response([])

    serializer = UserBookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_book(request):
    serializer = UserBookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response({"message": "Book added to library!"}, status=201)
    return Response(serializer.errors, status=400)

    return Response({"message": "Book added to library!"}, status=201)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_book(request, pk):

    try:
        book = UserBook.objects.get(pk=pk, user=request.user)
    except UserBook.DoesNotExist:
        return Response({"error": "Book not found"}, status=404)

    try:
        book.status = request.data.get("status", book.status)
        book.date_started = request.data.get("date_started", book.date_started)
        book.date_finished = request.data.get("date_finished", book.date_finished)
        book.rating = request.data.get("rating", book.rating)
        book.review = request.data.get("review", book.review)
        book.save()
        serializer = UserBookSerializer(book)
        return Response(serializer.data)

    except Exception as e:
        print(e)
        return Response({"error": str(e)}, status=400)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_book(request, pk):

    try:
        book = UserBook.objects.get(pk=pk, user=request.user)
    except UserBook.DoesNotExist:
        return Response({"error": "Book not found"}, status=404)

    try:
        book.delete()
        return Response({"message": "Book removed from library"}, status=204)
    except Exception as e:

        return Response({"error": str(e)}, status=400)
