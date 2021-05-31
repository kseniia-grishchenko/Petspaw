from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from random import random

from .models import Breed, Image, Favourite, Vote
from .serializers import BreedSerializer, ImageSerializer, FavouriteSerializer, VoteSerializer


class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    @action(detail=False, methods=["GET"])
    def search(self, request):
        order_by = str(request.query_params.get("order", "random"))
        limit = int(request.query_params.get("limit", 100))
        images = Image.objects.all().order_by("breed__name" if order_by == "asc" else "-breed__name")[:limit]
        if order_by == "random":
            images = sorted(images, key=lambda x: random())
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FavouriteViewSet(viewsets.ModelViewSet):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

    @action(detail=False, methods=["GET"])
    def likes(self, request):
        likes = Vote.objects.filter(value=1)
        serializer = VoteSerializer(likes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["GET"])
    def dislikes(self, request):
        dislikes = Vote.objects.filter(value=0)
        serializer = VoteSerializer(dislikes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
