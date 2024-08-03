from django.shortcuts import render
from rest_framework import viewsets
from .models import blogsModel
from .serializers import blogSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Create your views here.
class blogsViewsets(viewsets.ModelViewSet):
    queryset            = blogsModel.objects.all()
    serializer_class    = blogSerializer

class doctorsPost(APIView):
    def get(self, request, id=None, format=None):
        if id is not None:
            print(id)
            model = blogsModel.objects.filter(author=id)
            serializer = blogSerializer(model, many=True)
            return Response(serializer.data)
        else:
            model = blogsModel.objects.all()
            serializer = blogSerializer(model, many=True)
            return Response(serializer.data)