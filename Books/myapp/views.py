from django.shortcuts import render
from rest_framework import viewsets
from .models import BookModel
from .serializers import BookSerilizers
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookSerilizers
    permission_classes = [IsAuthenticated]