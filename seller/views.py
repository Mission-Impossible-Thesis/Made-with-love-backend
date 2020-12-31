from django.shortcuts import render
# Create your views here.
import json as JSON
from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework import permissions
from django.shortcuts import render
from accounts.models import Item
from accounts.models import Seller
from django.core.serializers import json
# import jwt,json
#importinf models of tables 
from accounts.models import Item
from accounts.models import Seller
from accounts.models import Buyer
from accounts.models import Category
from accounts.models import Order
class getCategoryStore (APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, cat):
        # data = self.request.data  
        print(cat)
        obj = Seller.objects.filter(category = cat)
        json_serializer = json.Serializer()
        json_serialized = json_serializer.serialize(obj)
        data= JSON.loads(json_serialized)
        # print(data)
        return Response (data)
class addItem(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        data = self.request.data
        print(data)
        productName = data['product']
        description = data['description']
        price = data['price']
        category = data['category']
        image = data['url']
        store1 = data['user']
        if category == "clothes":
            gender = data['gender']
            size = data['size']
            category_id = Category.objects.get(category_id =200)
            store = Seller.objects.get(store_id =store1)
            s = store.store_id
            item = Item.objects.create (productname = productName, store_id=s, description=description, price=price, gender=gender, size=size, image=image, category=category_id)
            return Response ({'success': 'Add Item'})
        if(category == 'food'):
            types = data['type']
            store = Seller.objects.get(store_id =store1)
            s = store.store_id
            category_id = Category.objects.get(category_id =100)
            item = Item.objects.create (productname = productName,store_id=s, description=description, price=price,types=types, image=image, category_id=category_id)
            return Response ({'success': 'Add Item'})
        if category == 'accessories':
            material = data['material']
            store = Seller.objects.get(store_id =store1)
            s = store.store_id
            category_id = Category.objects.get(category_id =300)
            item = Item.objects.create (productname = productName,store_id=s, description=description, price=price, image=image, material=material, category=category_id)
            return Response ({'success': 'Add Item'})
        if category == 'baby products':
            gender = data['gender']
            store = Seller.objects.get(store_id =store1)
            s = store.store_id
            category_id = Category.objects.get(category_id =400)
            item = Item.objects.create (productname = productName,store_id=s, description=description, price=price, gender=gender, image=image, category=category_id)
            return Response ({'success': 'Add Item'})
        # category_id = data['category_id']
        # store_id = data['store_id']
        item = Item.objects.create (productname = productName,store_id=s, description=description, price=price, gender=gender,types=types, size=size, image=image, material=material)
        item.save()
        return Response ({'success': 'Add Item'})

#to get items for seller
class getItems(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request,pk, format=None):
         print('eeeeeeeeeeeeeeeeeeeeeeeeee')
         obj = Item.objects.filter(store_id=pk)
         json_serializer = json.Serializer()
         json_serialized = json_serializer.serialize(obj)
         print(json_serialized,"iteeeeeems" )
         return Response(json_serialized)


#to get items for visitor
class getItemsVisit(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request,pk, format=None):
         print('eeeeeeeeeeeeeeeeeeeeeeeeee')
         obj = Item.objects.filter(store_id=pk)
         json_serializer = json.Serializer()
         json_serialized = json_serializer.serialize(obj)
         print(json_serialized,"iteeeeeems" )
         return Response(json_serialized)


#to get info for seller profile for visitor
class sellerVisit(APIView):
    permission_classes = (permissions.AllowAny,)         
    def get(self, request,pk, format=None):
        print(pk)
        obj1 = Seller.objects.filter(store_id=pk)
        json_serializer = json.Serializer()
        json_serialized1 = json_serializer.serialize(obj1)
        # print(json_serialized )
        myData = []
        print(pk,">>>>11111111111111")
        obj = Item.objects.filter(store_id=pk)
        json_serializer = json.Serializer()
        json_serialized = json_serializer.serialize(obj)
        # print(json_serialized )
        myData.append(json_serialized1)
        myData.append(json_serialized)
        print("mydataaa",myData,"dataaend")
        # dat =   JSON.dumps(myData)
        return Response(json_serialized1)         
class SnippetDetailSeller(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = (permissions.AllowAny,)
    # def get(self,request,  pk):
    #     try:
    #         return Snippet.objects.get(pk=pk)
    #     except Snippet.DoesNotExist:
    #         raise Http404
    # def get(self, request,pk, format=None):
    #      print('eeeeeeeeeeeeeeeeeeeeeeeeee')
    #      obj = Seller.objects.filter(pk=pk)
    #      json_serializer = json.Serializer()
    #      json_serialized = json_serializer.serialize(obj)
    #      print(json_serialized )
    #      return Response(json_serialized)
    

    # to get info for the seller
    def get(self, request,pk, format=None):
        print(pk)
        #   data = self.request.data 
        # store_Name = data['store_Name'] 
        # description = data['description'] 
        # location = data['location'] 
        # delivery_date = data[' delivery_date '] 
        # image = data['image']
        # category_id = data['category_id']
        # store_id = data['store_id'] 
        # serializer = SnippetSerializer(snippet)
        obj1 = Seller.objects.filter(pk=pk)
        json_serializer = json.Serializer()
        json_serialized1 = json_serializer.serialize(obj1)
        # print(json_serialized )
        myData = []
        print(pk,">>>>11111111111111")
        obj = Item.objects.filter(store_id=pk)
        json_serializer = json.Serializer()
        json_serialized = json_serializer.serialize(obj)
        # print(json_serialized )
        myData.append(json_serialized1)
        myData.append(json_serialized)
        print("mydataaa",myData,"dataaend")
        # dat =   JSON.dumps(myData)
        return Response(json_serialized1)

#to update one item
class updateItem(APIView):
    permission_classes = (permissions.AllowAny,) 
    def post(self, request, pk, format=None):
        obj = Item.objects.get(pk=pk)
        data = self.request.data 
        print(data)

        productName = data['productName'] 
        description = data['description'] 
        price = data['price']
        category = data['category']
        image = data['url'] 

        if category == "clothes":
            gender = data['gender'] 
            size = data['size'] 
            category_id = Category.objects.get(category_id =200)
            Item.objects.save (productname = productName, description=description, price=price, gender=gender, size=size, image=image, category=200)
           
            return Response ({'success': 'Item Editeeed'})
        if(category == 'food'):
            types = data['type'] 
            category_id = Category.objects.get(category_id =100) 
            Item.objects.save (productname = productName, description=description, price=price,types=types, image=image, category_id=100)
            item.save()
            return Response ({'success': 'Item Editeeed'})
        if category == 'accessories':
            material = data['material'] 
            category_id = Category.objects.get(category_id =300)
            Item.objects.save (productname = productName, description=description, price=price, image=image, material=material, category=300)
            item.save()
            return Response ({'success': 'Item Editeeed'})
        if category == 'baby products':
            gender = data['gender']
            category_id = Category.objects.get(category_id =400)
            Item.objects.save (productname = productName, description=description, price=price, gender=gender, image=image, category=400)
            return Response ({'success': 'Item Editeeed'})

        # category_id = data['category_id']
        # store_id = data['store_id'] 
        # item = Item.objects.create (productname = productName, description=description, price=price,  image=image)
        # item.save()
        return Response ({'success': 'Item Editeeeed'})
    # def put(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     serializer = SnippetSerializer(snippet, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # def delete(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     snippet.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
        # item = Item.objects.create (productname = productName, description=description, price=price, gender=gender,types=types, size=size, image=image, material=material)
        # item.save()
        
class getListOrder (APIView):
     permission_classes = (permissions.AllowAny,)
     def get(self, request, pk):
         print(pk)
        #  print(store_id)
         obj = Order.objects.filter(pk=pk)
         json_serializer = json.Serializer()
         json_serialized = json_serializer.serialize(obj)
         data= JSON.loads(json_serialized)
         print(data,'dataaaaaa')
         for x in data:
            print(x['fields']['buyer'],'buyeeeeeer')
            obj1 = Buyer.objects.get(buyer_id = x['fields']['buyer'])
            print(obj1.username)
            x['fields']['buyer'] = obj1.username
         for x in data:
            print(x['fields']['item'])
            obj1 = Item.objects.get(item_id = x['fields']['item'])
            # obj2 = Item.objects.get(item_id = x['fields']['item'])

            print(obj1.productname)
            print(x['fields'], 'xxxxxxxx')
            print(x['fields']['quantity'], 'quaaan')
            y= x['fields']['quantity']
            print(x['fields']['quantity'], 'yyyyyy')
            print(obj1.price,'priiiiiiiiiiiiiiice')
            x['fields']['item'] = obj1.productname 
            # print(obj1.quantity,'quantity')
            print(obj1.price*y,'multiiiiii')
            x['fields']['price'] = obj1.price*y
 

        #  for y in data:
        #    print(y['fields']['item'])
        #     # obj1 = Item.objects.get(item_id = x['fields']['item'])
        #    obj2 = Item.objects.get(item_id = x['fields']['item'])

        #     # print(obj1.productname)
        #    print(obj2.price,'priiiiiiiiiiiiiiice')
        #     # x['fields']['item'] = obj1.productname 
        #    x['fields']['item'] = obj2.price 
            
                
         return Response (data)
        #  obj = Buyer.objects.get(phonenumber = phonenumber)
        #  print(obj.buyer_id)
         
        #  return Response (data)

#to delete one item
class deleteItem(APIView):
    permission_classes = (permissions.AllowAny,)  

    def delete(self, request, pk, format=None):
        Item.objects.filter(pk=pk).delete()
        print('Deleeeete')
        return Response('Deleteeeed')
