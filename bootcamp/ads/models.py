from django.db import models
from . import httputil
import os
import asyncio
from asgiref.sync import async_to_sync, sync_to_async
import json
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
        host = os.environ.get('REVIEW_HOST', '')

        return host+'/api/v1/multireviewDetail/'+self.contact+'/'

    def contactRatingState(self):
        pass
        try:
            #await httputil.getresMain(self.contact)....
            #asyncio.run(httputil.getresMain(self.contact))ni

            #return httputil.getres(self.contact)
            res = asyncio.run(httputil.getresMain(self.contact))
            return res
        except:
            return ''
