from rest_framework.views import APIView
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework.response import Response
from django.utils.encoding import force_bytes
from . import serializers
from django.contrib.auth import authenticate, logout
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.http import JsonResponse
from . models import AdditionalInfoModel
from rest_framework import status

# Create your views here.
# registration
class userRegistration(APIView):
    serializer = serializers.userRegistrationSerializer

    def post(self, request):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            print(user)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print("uid: ", uid)
            print("token: ", token)
            return Response({'data': 'User created successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors)
    
# login
class UserLogin(APIView):
    def post(self, request):
        serializer = serializers.loginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)

            if user:
                token, _ = Token.objects.get_or_create(user=user)

                try:
                    additional_info = AdditionalInfoModel.objects.get(user=user)
                except AdditionalInfoModel.DoesNotExist:
                    return Response({'error': 'Additional information not found for the user'}, status=status.HTTP_404_NOT_FOUND)

                additional_info_serializer = serializers.additionalInfoSerializer(additional_info)

                response_data = {
                    'token': token.key,
                    'user': {
                        'id': user.id,
                        'username': user.username,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        'email': user.email,
                    },
                    'additional_info': additional_info_serializer.data
                }

                return Response(response_data, status=status.HTTP_200_OK)

            else:
                return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# logout
def UserLogOut(request,id, token):
    try:
        user = User.objects.get(id=id)
        userToken = Token.objects.get(user=user).key
        if user:
            if(token == userToken):
                currentUser = Token.objects.get(user=user)
                logout(request)
                currentUser.delete()
                # print('logout success')
                return JsonResponse({'status':'success'}, status=200)
            else:
                # print('token does not exist')
                return JsonResponse({'status':'token does not exist'})
    except User.DoesNotExist or Token.DoesNotExist:
            # print('invalid user')
            return JsonResponse({'status':'invalid user'})