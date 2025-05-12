from rest_framework import serializers
from .models import BookModel

class BookSerilizers(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = '__all__'