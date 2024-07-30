from rest_framework import serializers
from .models import AdditionalInfoModel
from .constants import ROLE
from django.contrib.auth.models import User

class additionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model   = AdditionalInfoModel
        fields  = '__all__'


class userRegistrationSerializer(serializers.ModelSerializer):
    profile_picture     = serializers.FileField(required=False, allow_null=True)
    confirm_password    = serializers.CharField(required=True)
    address             = serializers.CharField(max_length=20)
    role                = serializers.ChoiceField(choices=ROLE)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'profile_picture','address', 'role','password', 'confirm_password']


    def create(self, validated_data):
        username            = validated_data['username']
        first_name          = validated_data['first_name']
        last_name           = validated_data['last_name']
        email               = validated_data['email']
        profile_picture     = validated_data['profile_picture']
        address             = validated_data['address']
        role                = validated_data['role']
        password            = validated_data['password']
        confirm_password    = validated_data['confirm_password']

        if password != confirm_password:
             raise serializers.ValidationError({"error": "Password doesn't match"})
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"error": "Email already exists"})

        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        user.save() 

        additional_info = {'user':user, 'profile_picture':profile_picture,'address':address, 'role': role}
        AdditionalInfoModel.objects.create(**additional_info)

        return user


class loginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)