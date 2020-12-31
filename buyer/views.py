from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework import permissions
import json as JSON
from django.core.serializers import json
#importinf models of tables 
from accounts.models import Item
from accounts.models import Seller
from accounts.models import Buyer
from accounts.models import Category
from accounts.models import Order
import stripe 
stripe.api_key = 'sk_test_51I2FktCNmtNvriYQevst0uXD1j9WE53OaXVTFUAkDx8KaA6wZDyhEn71yvOJyMFvuR4opzUvEMJimQPXaLp9a4sw00IiZ4D7oD'


class orderItem(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data = self.request.data  
        print('innnn')
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


# class checkOutItem(APIView):
#     permission_classes = (permissions.AllowAny,)

#     def post(self, request, format=None):
#         data = self.request.data  
#         print('innnn')
#         order = data['order']
#         item_id = data['item_id']
        
#         phonenumber = order['phoneNumber']
#         print(phonenumber)
#         quantity=order['quantity']
#         location = order['location']
#         store_id=data['store_id']
#         date=data['date']
#         obj = Buyer.objects.get(phonenumber = phonenumber)
#         print(obj.buyer_id)
#         orders= Order.objects.create(buyer_id = obj.buyer_id, quantity=quantity, store_id=store_id, item_id=item_id,phonenumber=phonenumber, order_date=date, location=location )
#         return Response ({'success':'Order Submited'})




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
        
        


class payment(APIView):
    def post(request):

         test_payment_intent = stripe.PaymentIntent.create(
         amount=1000, currency='pln', 
         payment_method_types=['card'],
         receipt_email='test@example.com')
         return Response(status=status.HTTP_200_OK, data=test_payment_intent)
