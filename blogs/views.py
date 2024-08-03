from django.shortcuts import render
from rest_framework import viewsets
from .models import blogsModel
from .serializers import blogSerializer

# Create your views here.
class blogsViewsets(viewsets.ModelViewSet):
    queryset            = blogsModel.objects.all()
    serializer_class    = blogSerializer