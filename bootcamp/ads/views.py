from django.shortcuts import render

# Create your views here.


from .models import adsgnModel
from .sercls import reviewSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class reviewList(generics.ListCreateAPIView ):
    queryset = adsgnModel.objects.all()
    serializer_class = reviewSerializer



class reviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = adsgnModel.objects.all()
    serializer_class = reviewSerializer
