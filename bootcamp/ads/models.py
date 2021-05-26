from django.db import models
from . import httputil

# Create your models here.
class adsgnModel(models.Model):
    title = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    price = models.FloatField()
    currency = models.CharField(max_length=20)
    category=  models.CharField(max_length=20)
    createdAt = models.DateTimeField(auto_now_add=True)
    modifiedAt = models.DateTimeField(auto_now=True)
    purchasedOn = models.DateTimeField(blank=True, null=True)

    def reviewsUrl(self):
        return '127.0.0.1:8000/api/v1/multireviewDetail/'+self.contact+'/'

    def contactRatingState(self):
        pass
        return httputil.getres(self.contact)
