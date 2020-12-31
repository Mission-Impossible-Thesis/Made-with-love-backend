from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework import permissions
from django.http import HttpResponse
import json as JSON
import jwt
from django.core.serializers import json
#importinf models of tables 
from accounts.models import Item
from accounts.models import Seller
from accounts.models import Buyer
from accounts.models import Category
from accounts.models import Order

class orderItem(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        data = self.request.data  
        print(request.data,"request")
        order = data['order']
        item_id = data['item_id']
        # print(item_id,'iiiddddd')
        phonenumber = order['phoneNumber']
        print(phonenumber)
        quantity=order['quantity']
        location = order['location']
        store_id=data['store_id']
        date=data['date']
        obj = Buyer.objects.get(buyer_id = store_id)
        item= Item.objects.get(item_id = item_id)
        price= item.price
        print('price', price)
        total = price * int(quantity)
        print(total)
        orders= Order.objects.create(buyer_id = obj.buyer_id, quantity=quantity, store_id=store_id, item_id=item_id,phonenumber=phonenumber, order_date=date, location=location, price = total )
        return Response ({'success':'Order Submited'})
class getCategoryItems(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, cat):
        # data = self.request.data  
        print(cat)
        if cat == 'food':
            category = 100
        if cat == 'clothes':
            category = 200
        if cat == 'babyproducts':
            print(cat)
            category = 400
        if cat == 'accessories':
            category = 300
        obj = Item.objects.filter(category = category)
        json_serializer = json.Serializer()
        json_serialized = json_serializer.serialize(obj)
        data= JSON.loads(json_serialized)
        # print(json_serialized)
        return Response (data)
        # print(json_serialized)
        # print(JSON.loads(json_serialized))
        # myData = []
        # class MyClass:
        #      id = 5
        #      info = ""
        # obj1 = MyClass()
        # for x in data:
        #     obj1.id=x['pk']
        #     obj1.info=x['fields']
        #     # setattr(x, 'id', x['pk'])
        #     # x['fields'].id = x['pk']
        #     myData.append(obj1)
        # print(myData)
        
class  buyerPassword(APIView):
     permission_classes = (permissions.AllowAny,)
     def post(self, request,format=None):
         data = self.request.data
         token = request.META.get('HTTP_AUTHORIZATION')
         tole = jwt.decode(token, "SECRET_KEY")['email']
         password = data['oldPassword']
         newPassword = data['newPassword']
         user = Buyer.objects.get(email= tole)
         print(user.password )
         s = 'gh@f$#$@&4hjhgjh'
         e = '786huyh8%3h'
         r ="".join(user.password.split(s))
         t = "".join(r.split(e))
         print (t)
         
         if password == t:
             s = 'gh@f$#$@&4hjhgjh'
             e = '786huyh8%3h'
             length = (len(newPassword)/2)
             iy = int(length)
             print(length)
             firstpart = newPassword[0:iy]
             seconedpart = newPassword[iy:len(newPassword)]
             x =newPassword[0] + s + firstpart[1:int(len(firstpart)/2)] + s + firstpart[int(len(firstpart)/2):] + seconedpart[:int(len(seconedpart)/2)] + e + seconedpart[int(len(seconedpart)/2):]
             Buyer.objects.filter(email= tole).update(password =x )
             return HttpResponse({"success":"password changed"} ,status="200")
         else:
            return HttpResponse({"Unauthorized":"password incorrect"} ,status="400")
        
class  buyerUsername(APIView):
     permission_classes = (permissions.AllowAny,)
     def post(self, request,format=None):
         data = self.request.data
         token = request.META.get('HTTP_AUTHORIZATION')
         tole = jwt.decode(token, "SECRET_KEY")['email']
         username= data['userName']
         Buyer.objects.filter(email= tole).update(username =username )
         return HttpResponse({"success":"username changed"} ,status="200")

class  buyerLocation(APIView):
     permission_classes = (permissions.AllowAny,)
     def post(self, request,format=None):
         data = self.request.data
         token = request.META.get('HTTP_AUTHORIZATION')
         tole = jwt.decode(token, "SECRET_KEY")['email']
         location= data['location']
         Buyer.objects.filter(email= tole).update(location =location )
         return HttpResponse({"success":"location changed"} ,status="200")
         
class getAll(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        print(token)
        if not token:
             return HttpResponse({"Unauthorized":"Unauthorized"} ,status="401")
        elif token:
                try:
                    tole = jwt.decode(token, "SECRET_KEY")
                    print(tole['email'],'hijuhuyu')
                    email = tole['email']
                    obj11 = Buyer.objects.filter(email = email)
                    if obj11:
                        json_serializer = json.Serializer()
                        json_serialized = json_serializer.serialize(obj11)
                        data1= JSON.loads(json_serialized)
                        return Response (data1)
                except jwt.DecodeError:
                    return HttpResponse({"Unauthorized":"Unauthorized"} ,status="401")