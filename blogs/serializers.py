from rest_framework import serializers
from .models import blogsModel

class blogSerializer(serializers.ModelSerializer):
    class Meta:
        model   = blogsModel
        fields  = '__all__'