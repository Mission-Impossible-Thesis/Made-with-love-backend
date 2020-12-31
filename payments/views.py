from django.shortcuts import render
import stripe
from accounts.models import Order
from madewithlove import settings
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response 







class PaymentView(APIView):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    permission_classes = (permissions.AllowAny,)
 
    def post(self, request, *args, **kwargs):
        #  order = Order.objects.get(user=self.request.user, ordered=False)
         token = request.data["token"]["id"]
         print(token,'tokeeeeeen')
         a="tok_1I3RymCNmtNvriYQ4O5ZQrKs tokeeeeeen"
         print(request.data)
        #  quantity=order['quantity']
        #  location = order['location']
        #  store_id=data['store_id']
        #  date=data['date']
        #  obj = Buyer.objects.get(buyer_id = store_id)
        #  item= Item.objects.get(item_id = item_id)
        #  price= item.price
        #  print('price', price)
         total = request.data['token']['total'] 
         stripe.Charge.create(
            amount=total,
            currency="usd",
            source=token,
            description="My First Test Charge (created for API docs)",
            receipt_email= request.data["token"]["email"]

         )
         return Response('ok')
