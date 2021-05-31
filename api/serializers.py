from rest_framework import serializers
from .models import *


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    breed = BreedSerializer(many=False, read_only=True)

    class Meta:
        model = Image
        fields = '__all__'


class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = '__all__'


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'
