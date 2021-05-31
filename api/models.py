from django.db import models
from django.contrib.auth.models import User


class Breed(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    temperament = models.TextField(null=True, blank=True)
    life_span = models.CharField(max_length=200, null=True, blank=True)
    origin = models.CharField(max_length=200, null=True, blank=True)
    weight = models.CharField(max_length=200, null=True, blank=True)
    country_code = models.CharField(max_length=20, null=True, blank=True)
    height = models.CharField(max_length=200, null=True, blank=True)
    bred_for = models.CharField(max_length=200, null=True, blank=True)
    breed_group = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name if self.name else "No name"


class Image(models.Model):
    url = models.CharField(max_length=200, null=True, blank=True)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.url


class Favourite(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    sub_id = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image


class Vote(models.Model):
    LIKE = 'like'
    DISLIKE = 'dislike'
    value = models.IntegerField(
        choices=[
            (1, LIKE),
            (0, DISLIKE)
        ]
    )
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    sub_id = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    country_code = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.image
