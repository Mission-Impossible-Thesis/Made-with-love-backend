from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
import jwt,json
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
import jwt
from .models import Seller
from django.http import HttpResponse
import json 
import codecs
from rest_framework import status, exceptions
from django.http import HttpResponse
from rest_framework.authentication import get_authorization_header, BaseAuthentication
from django.http import HttpResponse


from .models import Buyer
from .models import Category


# import jwt
#  key = "secret"
#   encoded = jwt.encode({"some": "payload"}, key, algorithm="HS256")
#  print(encoded)
#  jwt.decode(encoded, key, algorithms="HS256")
# {'some': 'payload'}





class signupSeller(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data = self.request.data  
        print(data)
        email = data['email']
        password = data['password']
        store_name = data['storeName']
        location = data['location']
        category = data['category']
        description = data['description']
        delivery_time= data ['delieveryTime']
        image = data ['url']
        #check if email exsists
        obj = Seller.objects.filter(email = email)
        tr1 = Seller.objects.filter(email = email)

        if obj or tr1:
            return Response ({'error':"Email already exist"})
        else:
            user = Seller.objects.create_user(email = email, store_name = store_name , password = password, description=description, delivery_time=delivery_time, image=image, location=location, category=category)
            # user.save()
            return Response ({'success':'Seller registered'})


class signupBuyer(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data = self.request.data  
        email = data['email']
        password = data['password']
        username = data['userName']
        phonenumber = data['phoneNumber']
        location=data['location']
        #check if email exsists
        obj = Buyer.objects.filter(email = email)
        tr1 = Seller.objects.filter(email = email)
       

        if obj or tr1:
            return Response ({'error':"Email already exist"})
        else:
            user =Buyer.objects.create_user(email=email, username=username , location=location, phonenumber=phonenumber, password=password, is_active = True)
            return Response ({'success':"Buyer registered"})



class Login(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        if not request.data:
            return Response({'Error': "Please provide username/password"}, status="400")
        email = request.data['email']
        password = request.data['password']
        try:
            print('hello')

            Seller.objects.get(email=email)
           
            user = Buyer.objects.get(email=email)
            
           
        except Buyer.DoesNotExist:
            print('fgfg')
            userSeller = Seller.objects.get(email=email)
            password = self.request.data['password']
            s = 'gh@f$#$@&4hjhgjh'
            e = '786huyh8%3h'
            r ="".join(userSeller.password.split(s))
            t = "".join(r.split(e))
            if t == self.request.data['password']:
                payload = {
                    'email': userSeller.email,
            }
            tok = jwt.encode(payload, "SECRET_KEY")
            jwt_token = {'token': jwt.encode(payload, "SECRET_KEY"),"id_store":userSeller.store_id, "type":"seller"}
            return Response(jwt_token)
        except Seller.DoesNotExist:
            userBuyer = Buyer.objects.get(email=email)
            password = self.request.data['password']
            s = 'gh@f$#$@&4hjhgjh'
            e = '786huyh8%3h'
            r ="".join(userBuyer.password.split(s))
            t = "".join(r.split(e))
            if t == self.request.data['password']:
                payload = {
                    'email': userBuyer.email
                }
            jwt_token = {'token': jwt.encode({
                    'email': userBuyer.email
                }, "SECRET_KEY"),"id_store":userBuyer.buyer_id, "type":"buyer"}
            return Response(jwt_token)
        else :
            return Response(
            json.dumps({'Error': "Invalid credentials"}),
            status=400,
            content_type="application/json"
            )

# class Login(APIView):
#     permission_classes = (permissions.AllowAny,)

class Login(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        if not request.data:
            return Response({'Error': "Please provide username/password"}, status="400")
        email = request.data['email']
        password = request.data['password']
        try:
            print('hello')
            Seller.objects.get(email=email)
            user = Buyer.objects.get(email=email)
        except Buyer.DoesNotExist:
            userSeller = Seller.objects.get(email=email)
            password = self.request.data['password']
            s = 'gh@f$#$@&4hjhgjh'
            e = '786huyh8%3h'
            r ="".join(userSeller.password.split(s))
            t = "".join(r.split(e))
            if t == self.request.data['password']:
                payload = {
                    'email': userSeller.email,
            }
            tok = jwt.encode(payload, "SECRET_KEY")
            jwt_token = {'token': jwt.encode(payload, "SECRET_KEY"),"id":userSeller.store_id, "type":"seller"}
            return Response(jwt_token)
        except Seller.DoesNotExist:
            userBuyer = Buyer.objects.get(email=email)
            password = self.request.data['password']
            s = 'gh@f$#$@&4hjhgjh'
            e = '786huyh8%3h'
            r ="".join(userBuyer.password.split(s))
            t = "".join(r.split(e))
            if t == self.request.data['password']:
                payload = {
                    'email': userBuyer.email
                }
            jwt_token = {'token': jwt.encode({
                    'email': userBuyer.email
                }, "SECRET_KEY"),"id_store":userBuyer.buyer_id, "type":"buyer"}
            return Response(jwt_token)
        else :
            return Response(
            json.dumps({'Error': "Invalid credentials"}),
            status=400,
            content_type="application/json"
            )
