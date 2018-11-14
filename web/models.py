from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Listing(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    vehicle = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=500, null=True)
    lat = models.FloatField(max_length=25)
    long = models.FloatField(max_length=25)

    COLOUR_CHOICE = (
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Green', 'Green'),
        ('Silver', 'Silver'),
        ('Black', 'Black')
    )

    colour = models.CharField(max_length=50, choices=COLOUR_CHOICE, null=True)

    def __str__(self):
        return f'{self.user} - {self.vehicle}'

    def get_absolute_url(self):
        return reverse('listing-detail', args=[str(self.id)])


class ListingImage(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.url

    def ret_str(self):
        return self.url
