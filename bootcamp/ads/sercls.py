
from .models import adsgnModel
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import serializers

class reviewSerializer(serializers.ModelSerializer):
    reviewsUrl = serializers.ReadOnlyField()
    contactRatingState = serializers.ReadOnlyField()
    class Meta:
        model = adsgnModel
        fields = ('id','title', 'price', 'contact', 'contactRatingState',
                  'currency', 'category', 'purchasedOn','createdAt', 'modifiedAt', 'reviewsUrl'  )

