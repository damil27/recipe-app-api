from rest_framework import serializers

from core.models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']

    def create(self, validated_data):
        """Create a new recipe"""
        return Recipe.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Update an existing recipe"""
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

