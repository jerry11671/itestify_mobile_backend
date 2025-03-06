from rest_framework import serializers

from .models import TextTestimony


class TextTestimonySerializer(serializers.ModelSerializer):
    class Meta:
        model = TextTestimony
        fields = ["title", "category", "content", "uploaded_by"]
        
    def create(self, validated_data):
        return TextTestimony.objects.create(**validated_data)