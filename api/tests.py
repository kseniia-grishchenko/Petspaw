from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from .models import Breed, Image, Vote, Favourite
from .serializers import BreedSerializer, ImageSerializer, VoteSerializer, FavouriteSerializer

BREED_URL = reverse("breed-list")


def detail_breed_url(breed_id):
    """Return recipe detail url"""
    return reverse('breed-detail', args=[breed_id])


class BreedTests(TestCase):
    """Test unauthenticated recipe API access"""

    @staticmethod
    def create_breed(name):
        return Breed.objects.create(
            name=name
        )

    def setUp(self):
        self.client = APIClient()
        self.breeds = [
            self.create_breed("A"),
            self.create_breed("B"),
            self.create_breed("C"),
        ]

    def test_list(self):
        """Test breeds successfully retrieved"""
        res = self.client.get(BREED_URL)

        breeds = Breed.objects.all()
        serializer = BreedSerializer(breeds, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_get(self):
        res = self.client.get(detail_breed_url(self.breeds[0].id))

        breed = Breed.objects.get(id=self.breeds[0].id)
        serializer = BreedSerializer(breed, many=False)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create(self):
        res = self.client.post(BREED_URL, {"name": "D"})

        breed = Breed.objects.get(name="D")
        serializer = BreedSerializer(breed, many=False)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.data, serializer.data)

    def test_delete(self):
        res = self.client.delete(detail_breed_url(self.breeds[0].id))

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

        def get_breed():
            Breed.objects.get(id=self.breeds[0].id)

        self.assertRaises(Breed.DoesNotExist, get_breed)
