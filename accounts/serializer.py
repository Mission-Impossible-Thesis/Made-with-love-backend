# from rest_framework import serializers

# from . import models

# class SignupSerializer(serializers.ModelSerializer):

#         class Meta:
#             model = models.Seller
#             fields = ( 'email', 'name', 'password','location','phonenumber','is_active')
#             extra_kwargs = {'password': {'write_only': True}}

#         def create(self, validated_data):
#         """Create and return a new user."""

#             user = models.Seller(
#                 email=validated_data['email'],
#                 location=validated_data['location'],
#                 phonenumber=validated_data['phonenumber'],
                
#                 )

#             user.set_password(validated_data['password'])
#             user.save()

#             return user


from rest_framework import status, exceptions
from django.http import HttpResponse
from rest_framework.authentication import get_authorization_header, BaseAuthentication
from users.models import User
import jwt
import json


# class TokenAuthentication(BaseAuthentication):

#     model = None

#     def get_model(self):
#         return User

#     def authenticate(self, request):
#         auth = get_authorization_header(request).split()
#         if not auth or auth[0].lower() != b'token':
#             return None

#         if len(auth) == 1:
#             msg = 'Invalid token header. No credentials provided.'
#             raise exceptions.AuthenticationFailed(msg)
#         elif len(auth) > 2:
#             msg = 'Invalid token header'
#             raise exceptions.AuthenticationFailed(msg)

#         try:
#             token = auth[1]
#             if token=="null":
#                 msg = 'Null token not allowed'
#                 raise exceptions.AuthenticationFailed(msg)
#         except UnicodeError:
#             msg = 'Invalid token header. Token string should not contain invalid characters.'
#             raise exceptions.AuthenticationFailed(msg)

#         return self.authenticate_credentials(token)

#     def authenticate_credentials(self, token):
#         model = self.get_model()
#         payload = jwt.decode(token, "SECRET_KEY")
#         email = payload['email']
#         userid = payload['id']
#         msg = {'Error': "Token mismatch",'status' :"401"}
#         try:
            
#             user = User.objects.get(
#                 email=email,
#                 id=userid,
#                 is_active=True
#             )
            
#             if not user.token['token'] == token:
#                 raise exceptions.AuthenticationFailed(msg)
               
#         except jwt.ExpiredSignature or jwt.DecodeError or jwt.InvalidTokenError:
#             return HttpResponse({'Error': "Token is invalid"}, status="403")
#         except User.DoesNotExist:
#             return HttpResponse({'Error': "Internal server error"}, status="500")

#         return (user, token)

#     def authenticate_header(self, request):
#         return 'Token'